from customer import Customer
from restaurant import Restaurant
from review import Review

customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Doe")

restaurant1 = Restaurant("Best Burgers")
restaurant2 = Restaurant("Pizza Palace")

review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant2, 5)

print(customer1.full_name())
print(restaurant2.average_star_rating())
print(Review.all())
