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

class QuizGame:
    def __init__(self):
        self.quizzes = self.create_default_quizzes()
        self.best_score = 0

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_valid_number(
                "메뉴를 선택하세요: ",
                1,
                5
            )

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.show_quiz_list()
            elif choice == "4":
                self.show_score()
            elif choice == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다.")

    def create_default_quizzes(self):
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

        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다!")

    def add_quiz(self):
        print("퀴즈 추가 기능은 아직 구현 전입니다.")

    def show_quiz_list(self):
        print("퀴즈 목록 기능은 아직 구현 전입니다.")

    def show_score(self):
        print(f"현재 최고 점수: {self.best_score}점")

if __name__ == "__main__":
    game = QuizGame()
    game.run()