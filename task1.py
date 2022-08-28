name = input("Введіть ім'я: ").capitalize()
day = input("Введіть день, дуже прошу: ")
if not day.isdigit():
    print("ДЕНЬ - це ЧИСЛО!!!!")
else:
    print(f"Good day {name}! {day} is a perfect day to learn some python.")