class ManufacturerService:
    def __init__(self, repo):
        self.repository = repo

    def get_all_manufacturers(self):
        return self.repository.get_all_manufacturers()
