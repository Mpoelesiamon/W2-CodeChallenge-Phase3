class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)
        customer.reviews.append(self)
        restaurant.reviews.append(self)

    def rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    def __repr__(self):
        return f"Review: {self.rating} stars for {self.restaurant.name} by {self.customer.full_name()}"

    def __str__(self):
        return self.__repr__()
