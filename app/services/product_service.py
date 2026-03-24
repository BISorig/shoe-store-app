from app.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_all_products(self):
        return self.repository.get_all_products()

    def update_product(self, data: dict, product_id: int):
        return self.repository.update_product(data, product_id)
    
    def create_product(self, data: dict):
        if data["image_path"] is None:
            data["image_path"] = "picture.png"
        return self.repository.create_product(data)

    def delete_product(self, product_id: int):
        return self.repository.delete_product(product_id)
