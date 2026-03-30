from app.repositories.order_repository import OrderRepository


class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def get_all_orders(self):
        return self.repository.get_all_orders()

    def create_order(self, data: dict):
        return self.repository.create_order(data)

    def update_order(self, order_id: int, data: dict):
        return self.repository.update_order(order_id, data)

    def delete_order(self, order_id: int):
        return self.repository.delete_order(order_id)
