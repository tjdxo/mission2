# Python Quiz Game

Python으로 구현한 콘솔 기반 퀴즈 게임입니다.  
사용자는 메뉴를 통해 퀴즈를 풀고, 퀴즈를 추가하고, 등록된 퀴즈 목록과 점수를 확인할 수 있습니다.

---

## 프로젝트 개요

이 프로젝트는 Python 기본 문법과 객체지향 구조를 연습하기 위한 콘솔 기반 퀴즈 게임입니다.

주요 학습 목표는 다음과 같습니다.

- 클래스와 메서드를 활용한 프로그램 구조화
- 리스트를 활용한 퀴즈 데이터 관리
- 사용자 입력 처리
- 예외 처리
- Git 브랜치 기반 작업 흐름 실습
- README 작성 및 트러블 슈팅 기록

---

## 주요 기능

### 1. 퀴즈 풀기

등록된 퀴즈를 순서대로 풀 수 있습니다.  
사용자는 보기 번호를 입력하여 정답을 선택합니다.

### 2. 퀴즈 추가

사용자가 직접 문제, 보기, 정답 번호를 입력하여 퀴즈를 추가할 수 있습니다.

### 3. 퀴즈 목록 보기

현재 등록된 퀴즈 목록을 확인할 수 있습니다.

### 4. 점수 확인

퀴즈 풀이 결과 점수를 확인할 수 있습니다.

### 5. 프로그램 종료

프로그램을 종료합니다.

---

## 실행 방법

### 1. 저장소 클론

```bash
git clone 저장소_URL
```

### 2. 프로젝트 폴더로 이동

```bash
cd 프로젝트_폴더명
```

### 3. 프로그램 실행

```bash
python main.py
```

환경에 따라 아래 명령어를 사용할 수도 있습니다.

```bash
python3 main.py
```

---

## 메뉴 구성

```text
===== Quiz Game =====
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록 보기
4. 점수 확인
5. 종료
```

---

## 예외 처리

사용자 입력에서 발생할 수 있는 예외를 구분하여 처리했습니다.

입력값 검증은 공통 메서드인 `get_valid_number()`에서 담당합니다.  
메뉴 선택과 정답 입력 모두 숫자 입력을 사용하기 때문에 하나의 메서드로 공통 처리했습니다.

```python
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
```

---

## 예외 처리 기준

| 예외 상황 | 예시 입력 | 처리 방식 |
|---|---|---|
| 빈 입력 | Enter | 빈 입력 안내 메시지 출력 후 재입력 |
| 숫자가 아닌 입력 | `abc`, `가나다` | 숫자가 아니라는 안내 메시지 출력 후 재입력 |
| 범위를 벗어난 숫자 | `0`, `9` | 입력 가능 범위 안내 메시지 출력 후 재입력 |

---

## 입력 검증 메서드 사용 예시

### 메뉴 선택에서 사용

메뉴는 1번부터 5번까지 있으므로 최소값은 `1`, 최대값은 `5`로 설정했습니다.

```python
choice = self.get_valid_number("메뉴를 선택하세요: ", 1, 5)
```

메뉴 선택 처리 코드는 다음과 같습니다.

```python
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
```

---

### 정답 입력에서 사용

퀴즈의 보기 개수에 따라 정답 번호의 최대값이 달라질 수 있으므로 `len(quiz.choices)`를 사용했습니다.

```python
user_answer = self.get_valid_number(
    "정답 번호를 입력하세요: ",
    1,
    len(quiz.choices)
)
```

---

## 실행 예시

```text
===== Quiz Game =====
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록 보기
4. 점수 확인
5. 종료

메뉴를 선택하세요:
입력값이 비어 있습니다. 숫자를 입력해주세요.

메뉴를 선택하세요: abc
숫자가 아닌 값입니다. 1부터 5 사이의 숫자를 입력해주세요.

메뉴를 선택하세요: 9
범위를 벗어났습니다. 1부터 5 사이의 숫자를 입력해주세요.

메뉴를 선택하세요: 1
퀴즈를 시작합니다!
```

---

## Git 브랜치 작업 흐름

이번 프로젝트에서는 기능 단위로 브랜치를 만들어 작업했습니다.

### 브랜치 생성

```bash
git switch -c feature/example
```

### 변경 사항 확인

```bash
git status
```

### 커밋

```bash
git add main.py
git commit -m "Feat: 퀴즈 기능 추가"
```

### 원격 저장소에 Push

```bash
git push -u origin feature/example
```

### main 브랜치로 병합

```bash
git switch main
git merge --no-ff feature/example -m "Merge: 기능 브랜치 병합"
git push origin main
```

---

## 커밋 메시지 규칙

| 타입 | 의미 |
|---|---|
| Feat | 새로운 기능 추가 |
| Fix | 버그 수정 |
| Refactor | 기능 변화 없는 코드 구조 개선 |
| Docs | 문서 수정 |
| Chore | 설정, 기타 작업 |

예시:

```bash
git commit -m "Feat: 퀴즈 풀이 기능 구현"
git commit -m "Fix: 메뉴 선택 입력 타입 오류 수정"
git commit -m "Docs: README 트러블 슈팅 추가"
```

---

## Troubleshooting

### 문제: 메뉴 번호를 입력해도 메뉴가 실행되지 않음

#### 상황

메뉴 선택 입력을 처리하기 위해 `get_valid_number()` 메서드를 만들었습니다.

이 메서드는 사용자 입력을 받은 뒤 `int()`를 사용해서 숫자형으로 변환합니다.

```python
number = int(user_input)
return number
```

하지만 기존 메뉴 조건문은 문자열과 비교하고 있었습니다.

```python
elif choice == '4':
    self.show_score()
elif choice == '5':
    print("프로그램을 종료합니다.")
    break
```

이 때문에 사용자가 `4`를 입력해도 실제 `choice` 값은 정수 `4`였고, 조건문에서는 문자열 `'4'`와 비교하고 있어서 메뉴가 실행되지 않았습니다.

```python
4 == '4'  # False
```

---

#### 원인

입력값의 자료형이 서로 달랐기 때문입니다.

| 값 | 자료형 |
|---|---|
| `4` | int |
| `'4'` | str |

`get_valid_number()`에서 입력값을 정수로 변환했기 때문에 조건문에서도 정수와 비교해야 했습니다.

---

#### 해결 방법

기존 문자열 비교 코드를 정수 비교 코드로 수정했습니다.

수정 전:

```python
elif choice == '4':
    self.show_score()
elif choice == '5':
    print("프로그램을 종료합니다.")
    break
```

수정 후:

```python
elif choice == 4:
    self.show_score()
elif choice == 5:
    print("프로그램을 종료합니다.")
    break
```

최종 메뉴 분기 코드는 다음과 같습니다.

```python
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
```

---

#### 배운 점

사용자 입력은 기본적으로 문자열로 들어옵니다.

```python
user_input = input("메뉴를 선택하세요: ")
```

하지만 `int()`로 변환하면 정수형이 됩니다.

```python
choice = int(user_input)
```

따라서 입력값을 변환한 뒤에는 조건문에서도 같은 자료형끼리 비교해야 합니다.

잘못된 비교:

```python
choice == '1'
```

올바른 비교:

```python
choice == 1
```

이번 문제를 통해 입력값 검증 로직을 공통 메서드로 분리할 때, 반환값의 자료형까지 함께 고려해야 한다는 점을 알게 되었습니다.

---

## 실행 화면 캡처

실행 결과를 보여주기 위해 캡처 이미지를 추가할 수 있습니다.

예시 폴더 구조:

```text
quiz-game/
├── main.py
├── README.md
└── images/
    └── exception-handling.png
```

README에 이미지를 넣는 방법:

```md
![예외 처리 실행 화면](images/exception-handling.png)
```

캡처는 필수는 아니지만, 예외 처리가 실제로 동작하는 화면을 보여줄 수 있기 때문에 추가하면 좋습니다.

추천 캡처:

- 빈 입력 처리 화면
- 숫자가 아닌 입력 처리 화면
- 범위를 벗어난 숫자 입력 처리 화면
- 정상적으로 메뉴가 실행되는 화면

---

## 향후 개선할 점

- 퀴즈 데이터를 JSON 파일로 저장하기
- 프로그램 종료 후에도 점수 기록 유지하기
- 카테고리별 퀴즈 기능 추가하기
- 난이도별 퀴즈 분류하기
- GitHub Pull Request 방식으로 브랜치 병합 실습하기