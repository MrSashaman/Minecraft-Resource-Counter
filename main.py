import json
import key
import socket

hostname = socket.gethostname()

print("Minecraft Resource Counter")

resources = []
try:
    with open("resources.json", "r") as f:
        resources = json.load(f)
except FileNotFoundError:
    resources = []


def auth():
    while True:
        if input("Введите ключ доступа: ") == key.KEY:
            break
        else:
            print("Неверный ключ, попробуйте снова")

def addresource():
    print("Добавить ресурс")
    name = input("Введите название ресурса: ")
    count = int(input("Введите количество: "))
    found = False

    for resource in resources:
        if resource["name"] == name:
            resource["count"] += count
            found = True
            break

    if not found:
        resources.append({
            "name": name,
            "count": count
        })

    # сохраняем ПОСЛЕ изменений
    with open("resources.json", "w") as f:
        json.dump(resources, f)


def showstats():
    total = 0
    print("Загружаю статистику!")

    with open("resources.json", "r") as f:
        loaded_data = json.load(f)

    print(loaded_data)

    for resource in loaded_data:
        total += resource["count"]

    print(f"Общее количество ресурсов: {total}")







print("*****************LOADING*****************")
print(f"Приветствую вас, {hostname}!")

auth()

while True:
    print("\nMinecraft Resource Counter".center(30, "*"))
    print("1.Добавить ресурс")
    print("2.Показать статистику")
    print("3.Сбросить счётчик")

    print("4. Выход")

    choice = input("Выбор: ")
    if choice == "1":
        addresource()
    elif choice == "2":
        showstats()

    elif choice == "3":
        resources.clear()
        with open("resources.json", "w") as f:
            json.dump(resources, f)
        print("Список ресурсов очищен!")
    elif choice == "4":
        break
    else:
        print("Введите 1, 2 или 3")





