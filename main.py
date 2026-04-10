import json
import socket
import datetime
import key

FILE = "resources.json"


def load_resources():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_resources(data):
    with open(FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def auth():
    while input("Введите ключ доступа: ") != key.KEY:
        print("Неверный ключ, попробуйте снова")


def add_resource(data):
    print("Добавить ресурс")
    name = input("Введите название ресурса: ").strip()

    try:
        count = int(input("Введите количество: "))
    except ValueError:
        print("Введите число")
        return

    for r in data:
        if r["name"] == name:
            r["count"] += count
            save_resources(data)
            return

    data.append({"name": name, "count": count})
    save_resources(data)


def show_stats():
    data = load_resources()
    total = sum(r["count"] for r in data)

    print("Загружаю статистику!")
    print(data)
    print(f"Общее количество ресурсов: {total}")


def reset(data):
    data.clear()
    save_resources(data)
    print("Список ресурсов очищен!")


def info():
    print(f"Дата: {datetime.datetime.now()}")
    print("Автор: mrsashaman")
    print("Версия 2")
    print("Последнее обновление: 10.04.2026")


def main():
    hostname = socket.gethostname()
    data = load_resources()

    print("*****************LOADING*****************")
    print(f"Приветствую вас, {hostname}!")

    auth()

    while True:
        print("\nMinecraft Resource Counter".center(30, "*"))
        print("1. Добавить ресурс")
        print("2. Показать статистику")
        print("3. Сбросить счётчик")
        print("4. Информация")
        print("5. Выход")

        choice = input("Выбор: ").strip()

        if choice == "1":
            add_resource(data)
        elif choice == "2":
            show_stats()
        elif choice == "3":
            reset(data)
        elif choice == "4":
            info()
        elif choice == "5":
            break
        else:
            print("Введите число от 1 до 5")


if __name__ == "__main__":
    main()
