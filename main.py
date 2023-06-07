# 예제 1: 간단한 if 문

x = 5
if x > 3:
    print("x는 3보다 큽니다.")

예제 2: if else 문
age = 18
if age >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# 예제 3 중접된 if else
score = 85
if score >= 90:
    print("A 학점")
else:
    if score >= 80:
        print("B 학점")
    else:
        if score >= 70:
            print("C 학점")
        else:
            print("D 학점")


# 예제 4: if elif
marks = 75
if marks >= 90:
    print("A 등급")
elif marks >= 80:
    print("B 등급")
elif marks >= 70:
    print("C 등급")
else:
    print("D 등급")

a = int(input("Enter Number Greater then 2:"))
if a > 2:
    print("Correct!! you have Entered: ", a)
else:
    print("Wrong!! you have Entered: ", a)

day = input("요일을 입력하세요: ")
if day == "Mon":
    print("오늘은 월요일")
elif day == "Tue":
    print("화요일")
elif day == "Wed":
    print("수요일")
else:
    print("휴일")

