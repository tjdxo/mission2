import json
import os


class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print(self.question)
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def check_answer(self, user_answer):
        return self.answer == user_answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["question"],
            data["choices"],
            int(data["answer"])
        )


class QuizGame:
    STATE_FILE = "state.json"

    def __init__(self):
        self.quizzes = []
        self.score = 0
        self.total_answered = 0
        self.best_score = 0
        self.load_state()

    def reset_state_to_default(self):
        self.quizzes = self.get_default_quizzes()
        self.score = 0
        self.total_answered = 0
        self.best_score = 0

    def save_state(self):
        data = {
            "quizzes": [
                quiz.to_dict()
                for quiz in self.quizzes
            ],
            "score": self.score,
            "total_answered": self.total_answered,
            "best_score": self.best_score
        }

        temp_file = self.STATE_FILE + ".tmp"

        try:
            with open(temp_file, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
                file.flush()
                os.fsync(file.fileno())

            os.replace(temp_file, self.STATE_FILE)
            return True

        except KeyboardInterrupt:
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except OSError:
                    pass

            raise

        except OSError as error:
            print(f"데이터 저장 중 오류가 발생했습니다: {error}")

            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except OSError:
                    pass

            return False

    def safe_save_on_exit(self):
        try:
            self.save_state()

        except KeyboardInterrupt:
            print("저장 중 중단되었습니다. 기존 state.json은 유지됩니다.")

        except OSError as error:
            print(f"종료 중 데이터 저장에 실패했습니다: {error}")

    def load_state(self):
        try:
            with open(self.STATE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("state.json의 최상위 데이터는 dict 형식이어야 합니다.")

            quizzes_data = data.get("quizzes", [])

            if not isinstance(quizzes_data, list):
                raise ValueError("quizzes 데이터는 list 형식이어야 합니다.")

            self.quizzes = [
                Quiz.from_dict(quiz_data)
                for quiz_data in quizzes_data
            ]

            self.score = int(data.get("score", 0))
            self.total_answered = int(data.get("total_answered", 0))
            self.best_score = int(data.get("best_score", 0))

        except FileNotFoundError:
            print("state.json 파일이 없어 기본 데이터로 시작합니다.")

            self.reset_state_to_default()
            self.save_state()

        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            print("state.json 파일을 읽는 중 오류가 발생했습니다.")
            print(f"오류 내용: {error}")
            print("기본 데이터로 초기화합니다.")

            self.reset_state_to_default()
            self.save_state()

        except OSError as error:
            print(f"state.json 파일 읽기 중 오류가 발생했습니다: {error}")
            print("기본 데이터로 프로그램을 시작합니다.")

            self.reset_state_to_default()

    def run(self):
        try:
            while True:
                self.show_menu()
                choice = self.get_valid_number(
                    "메뉴를 선택하세요: ",
                    1,
                    5
                )

                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_quiz_list()
                elif choice == 4:
                    self.show_score()
                elif choice == 5:
                    print("프로그램을 종료합니다.")
                    break

        except KeyboardInterrupt:
            print("\n\nCtrl+C가 입력되어 프로그램을 종료합니다.")
            self.safe_save_on_exit()

        except EOFError:
            print("\n\n입력 스트림이 종료되어 프로그램을 종료합니다.")
            self.safe_save_on_exit()

    def get_default_quizzes(self):
        return [
            Quiz(
                "소프트웨어 생명주기 모형 중 순차적으로 진행되는 모델은?",
                ["나선형", "폭포수", "애자일", "프로토타입"],
                2
            ),
            Quiz(
                "데이터베이스에서 기본키의 특징으로 맞는 것은?",
                ["중복 가능", "NULL 가능", "유일성", "정렬 전용"],
                3
            ),
            Quiz(
                "OSI 7계층 중 전송 계층에 해당하는 프로토콜은?",
                ["TCP", "IP", "HTTP", "FTP"],
                1
            ),
            Quiz(
                "객체지향 프로그래밍의 특징이 아닌 것은?",
                ["캡슐화", "상속", "다형성", "절차지향"],
                4
            ),
            Quiz(
                "다음 중 데이터베이스에서 DDL에 해당하는 SQL 명령어는?",
                ["SELECT", "INSERT", "CREATE", "UPDATE"],
                3
            )
        ]

    def show_menu(self):
        print("=" * 40)
        print("🎯 나만의 퀴즈 게임 🎯")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def get_valid_number(self, prompt, min_value, max_value):
        while True:
            user_input = input(prompt).strip()

            if user_input == "":
                print("입력값이 비어 있습니다. 숫자를 입력해주세요.")
                continue

            try:
                number = int(user_input)
            except ValueError:
                print(f"숫자가 아닌 값입니다. {min_value}부터 {max_value} 사이의 숫자를 입력해주세요.")
                continue

            if number < min_value or number > max_value:
                print(f"범위를 벗어났습니다. {min_value}부터 {max_value} 사이의 숫자를 입력해주세요.")
                continue

            return number

    def get_required_text(self, prompt, empty_message):
        while True:
            text = input(prompt).strip()

            if text == "":
                print(empty_message)
                continue

            return text

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0

        print("\n퀴즈를 시작합니다!")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{index}번 문제]")
            quiz.display()

            user_answer = self.get_valid_number(
                "정답 번호를 입력하세요: ",
                1,
                len(quiz.choices)
            )

            if quiz.check_answer(user_answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print("\n퀴즈가 종료되었습니다.")
        print(f"점수: {score} / {len(self.quizzes)}")

        self.score = score
        self.total_answered = len(self.quizzes)

        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다!")

        self.save_state()

    def add_quiz(self):
        print("\n퀴즈 추가")

        question = self.get_required_text(
            "문제를 입력하세요: ",
            "문제는 비워둘 수 없습니다."
        )

        choices = []

        for index in range(1, 5):
            choice = self.get_required_text(
                f"{index}번 보기를 입력하세요: ",
                "보기는 비워둘 수 없습니다."
            )
            choices.append(choice)

        answer = self.get_valid_number(
            "정답 번호를 입력하세요: ",
            1,
            len(choices)
        )

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        self.save_state()

        print("퀴즈가 추가되었습니다.")

    def show_quiz_list(self):
        print("\n퀴즈 목록")

        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{index}] {quiz.question}")

            for choice_index, choice in enumerate(quiz.choices, start=1):
                print(f"  {choice_index}. {choice}")

            print(f"  정답: {quiz.answer}번")

    def show_score(self):
        print(f"현재 최고 점수: {self.best_score}점")


if __name__ == "__main__":
    game = QuizGame()
    game.run()