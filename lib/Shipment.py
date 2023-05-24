from lib.DBconn import con


class Shipment:
    def __init__(self, client):
        self.client = client

    def create(self, weight, size):
        client = self.client.login()
        if client:
            weight_additional_price = 15 if weight == 0 else 20
            price = weight_additional_price + (weight // 100) * 6

            connection = con()
            with connection.cursor() as cursor:
                cursor.execute(
                    f"INSERT INTO shipments (client_id, weight, size, price, status) VALUES ('{client['id']}', '{weight}', '{size}', '{price}', 'Заказ собирается');")
                connection.commit()
                connection.close()
                return self.track_order(cursor.lastrowid)

    def track_order(self, id):
        connection = con()
        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM shipments WHERE id = '{id}';")
            order = cursor.fetchone()
            connection.close()
            return order

    def all_orders(self):
        client = self.client.login()
        if client:
            connection = con()
            with connection.cursor() as cursor:
                cursor.execute(
                    f"SELECT * FROM shipments WHERE client_id = '{client['id']}';")
                orders = cursor.fetchmany()
                connection.close()
                return orders

    def edit_order(self, id, status):
        client = self.client.login()
        if client:
            connection = con()
            with connection.cursor() as cursor:
                cursor.execute(
                    f"UPDATE `shipments` SET `status`='{status}' WHERE `client_id` = '{id}';")
                connection.commit()
                connection.close()
