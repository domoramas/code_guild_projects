#grading

score = int(input("Enter your score:"))

if score in range(90,101):
    letter_grade = "A"
elif score in range(80,90):
    letter_grade = "B"
elif score in range(70,80):
    letter_grade = "C"
elif score in range(60,70):
    letter_grade = "D"
else:
    letter_grade = "F"
plus_minus = score % 10
if score == 100:
    print(letter_grade + "+")
if score < 60:
    print(letter_grade)
elif plus_minus > 7:
    print(letter_grade + "+")
elif plus_minus < 3:
    print(letter_grade + "-")
else:
    print(letter_grade)