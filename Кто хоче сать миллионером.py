question = "Что разбудило спящую красавицу?"

right_answer = "Поцелуй принца"
answer1 = "Шумные соседи"
answer2 = "Будильник"
answer3 = "Телефон"

print(question)
print("-" * 40)
print(right_answer)
print(answer1)
print(answer2)
print(answer3)


user_answer = input("Введите ответ: ")
if user_answer == right_answer:
  print("Вы ответили правильно")
else:
  print("Ответ неверный")
  print("Правильный ответ:")
  print(right_answer)

