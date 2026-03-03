from datetime import datetime, timedelta


# начало
name = input("👋 Привет! Как тебя зовут? ")
print(f"\n{name}, давай отследим твоё настроение за месяц ✨")
print("Оценивай от 1 до 5, где 1 — очень плохо, 5 — отлично")

# списки для оценок и дат
mood_scores = []
dates = []

# сегодняшняя дата
start_date = datetime.now()

# данные за 31 день
for day in range(1, 32):
    score = int(input(f"День {day}: "))
    mood_scores.append(score)
    current_date = start_date - timedelta(days=31 - day)
    dates.append(current_date.strftime("%d.%m"))

# выводим эмодзи
print("\n📊 Твоё настроение в смайликах:")
for score in mood_scores:
    if score == 5:
        print("😊", end=" ")
    elif score == 4:
        print("🙂", end=" ")
    elif score == 3:
        print("😐", end=" ")
    elif score == 2:
        print("😕", end=" ")
    else:
        print("😢", end=" ")

# выводим по дням с датами и точками
print("\n\n📅 Оценки по дням:")
for i in range(31):
    print(f"{dates[i]}: {mood_scores[i]} {'•' * mood_scores[i]}")

#  список
print("\nТвои оценки:", mood_scores)

#  статистика
total = sum(mood_scores)
average = total / len(mood_scores)

print(f"📈 Средний балл: {average:.1f}")
print(f"😊 Лучший день: {max(mood_scores)}")
print(f"😢 Худший день: {min(mood_scores)}")

# разбиваем по дням
print("\n📊 Разбивка по дням:")
print(f"😊 Отличных (5): {mood_scores.count(5)}")
print(f"🙂 Хороших  (4): {mood_scores.count(4)}")
print(f"😐 Нормальных (3): {mood_scores.count(3)}")
print(f"😕 Так себе (2): {mood_scores.count(2)}")
print(f"😢 Плохих   (1): {mood_scores.count(1)}")

# итог по месяцу
if average >= 4:
    print("✨ Отличный месяц! Ты сияешь!")
elif average >= 3:
    print("🙂 Неплохой месяц, но есть куда расти")
else:
    print("😶 Месяц был тяжёлым. Выдохни и отдохни")

# сохраняем в файл
with open("mood_history.txt", "w", encoding="utf-8") as file:
    file.write(f"Оценки: {mood_scores}\n")
    file.write(f"Средний балл: {average:.1f}\n")
    file.write(f"Лучший день: {max(mood_scores)}\n")
    file.write(f"Худший день: {min(mood_scores)}\n")

print("\n📁 Результаты сохранены в mood_history.txt")
