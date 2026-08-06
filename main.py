def show_menu():
    print("=" * 40)
    print("🎯 나만의 퀴즈 게임 🎯")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)

while True:
    show_menu()
    choice = input("선택: ").strip()

    if choice == "1":
        print("퀴즈 풀기 기능")
    elif choice == "2":
        print("퀴즈 추가 기능")
    elif choice == "3":
        print("퀴즈 목록 기능")
    elif choice == "4":
        print("점수 확인 기능")
    elif choice == "5":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다.")

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