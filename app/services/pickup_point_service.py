from app.repositories.pickup_point_repository import PickupPointRepository


class PickupPointService:
    def __init__(self, repository: PickupPointRepository):
        self.repository = repository

    def get_all_pickup_points(self):
        return self.repository.get_all_pickup_points()
