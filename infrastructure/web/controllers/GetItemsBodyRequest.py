class GetItemsBodyRequest:
    def __init__(self, audience: str = '', category: str = ''):
        self.audience = audience.lower()
        self.category = category.lower()

    def validate(self):
        return self.audience and self.category
