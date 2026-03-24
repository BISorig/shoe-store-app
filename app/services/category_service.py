class CategoryService:
    def __init__(self, repo):
        self.repository = repo

    def get_all_categories(self):
        return self.repository.get_all_categories()