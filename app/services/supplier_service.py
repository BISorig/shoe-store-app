from app.repositories.supplier_repository import SupplierRepository


class SupplierService:
    def __init__(self, repository: SupplierRepository):
        self.repository = repository

    def get_all_suppliers(self):
        return self.repository.get_all_suppliers()
