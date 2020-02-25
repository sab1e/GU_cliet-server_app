"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": [
        {
            "item": "printer",
            "quantity": "10",
            "price": "6700",
            "buyer": "Ivanov I.I.",
            "date": "24.09.2017"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        }
    ]
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json

FILE_NAME = 'orders.json'


def write_order_to_json(file_name, item, quantity, price, buyer, date):
    """Добавление данных о заказе в существующий файл заказов в формате JSON"""
    with open(file_name) as f_n:
        obj = json.load(f_n)

    order = dict(item=item, quantity=quantity, price=price,
                 buyer=buyer, date=date)
    obj['orders'].append(order)

    with open(file_name, 'w') as f_n:
        json.dump(obj, f_n, sort_keys=True, indent=4)


if __name__ == '__main__':
    write_order_to_json(FILE_NAME, 'printer', '10', '6700', 'Ivanov I.I.',
                        '24.09.2017')
    write_order_to_json(FILE_NAME, 'scaner', '20', '10000', 'Petrov P.P.',
                        '11.01.2018')
