from lib.Client import Client
from lib.Shipment import Shipment


# Разработать консольное приложение для отслеживания клиентом посылки из маркетплейса
# v Клиент авторизуется в системе, может заказать доставку (4 посылки)
# v Для посылки выбирается вес и размер в зависимости от чего определяется цена
#   доставки (каждые 100 гр веса 6 рублей, габариты - маленький +15 рублей, средний  +20 рублей)
# * Клиент видит статус посылки и можетотслеживать его (статусы: заказ собирается, в сортировочном центре, в пути)


def main():
    print("1 - регистрация, 2 - авторизация")
    result = input()

    if result == "1":
        create_client()
    elif result == "2":
        login_client()
    else:
        main()


def create_client():
    username = input("Username: ")
    password = input("Password: ")

    client = Client(username, password)
    if client.create():
        print("Аккаунт успешно создан")
        main()
    else:
        print("Ошибка создания")
        create_client()


def login_client():
    username = input("Логин: ")
    password = input("Пароль: ")

    client = Client(username, password)
    if client.login():
        print("Вы успешно вошли")
        login_menu(username, password)
    else:
        print("Ошибка входа")
        login_client()


def login_menu(username, password):
    client = Client(username, password)
    edit_menu_item = " 4 - изменить заказ," if client.login()["is_admin"] else ""
    print(f"1 - сделать заказ, 2 - отследить заказ, 3 - список моих заказов,{edit_menu_item} 0 - выйти")
    result = input()
    if result == "1":
        create_order(username, password)
    elif result == "2":
        track_order(username, password)
    elif result == "3":
        all_orders(username, password)
    elif result == "4":
        edit_order(username, password)
    elif result == "0":
        main()
    else:
        login_menu(username, password)


def edit_order(username, password):
    client = Client(username, password)
    if client.login()["is_admin"]:
        shipment = Shipment(client)
        id = int(input("Введите номер заказа: "))

        order = shipment.track_order(id)
        if order:
            print(f"Номер заказа: {order['id']}, cтоимость заказа: {order['price']}, статус: {order['status']}")
            status = input("Введите новый статус заказа: ")
            shipment.edit_order(id, status)
            login_menu(username, password)
    else:
        login_menu(username, password)


def create_order(username, password):
    shipment = Shipment(Client(username, password))
    weight = int(input("Вес (6 рублей за каждые 100 гр.): "))
    size = int(input("Размер [маленький (0) +15 рублей, средний (1) +20 рублей]: "))
    order = shipment.create(weight, size)
    if order:
        print(
            f"Заказ успешно создан, номер заказа: {order['id']}, cтоимость заказа: {order['price']}, статус: {order['status']}")
        login_menu(username, password)
    else:
        print("Ошибка создания заказа")
        create_order(username, password)


def track_order(username, password):
    shipment = Shipment(Client(username, password))
    id = int(input("Введите номер заказа: "))

    order = shipment.track_order(id)
    print(f"Номер заказа: {order['id']}, cтоимость заказа: {order['price']}, статус: {order['status']}")
    login_menu(username, password)


def all_orders(username, password):
    shipment = Shipment(Client(username, password))

    print("Все заказы:")
    for order in shipment.all_orders():
        print(f"Номер заказа: {order['id']}, cтоимость заказа: {order['price']}, статус: {order['status']}")
    login_menu(username, password)


if __name__ == '__main__':
    main()
