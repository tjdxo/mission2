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
            choice = input("선택: ").strip()

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
            "Python에서 문자열 자료형은?",
            ["int", "str", "bool", "list"],
            2
            ),
            Quiz(
                "조건문에 사용하는 키워드는?",
                ["for", "if", "def", "class"],
                2
            ),
            Quiz(
                "리스트를 만들 때 사용하는 기호는?",
                ["()", "{}", "[]", "<>"],
                3
            ),
            Quiz(
                "함수를 정의할 때 사용하는 키워드는?",
                ["function", "def", "func", "make"],
                2
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

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0

        print("\n퀴즈를 시작합니다!")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{index}번 문제]")
            quiz.display()

            user_input = input("정답 번호를 입력하세요: ").strip()

            if not user_input.isdigit():
                print("숫자를 입력해야 합니다. 오답 처리됩니다.")
                continue

            user_answer = int(user_input)

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