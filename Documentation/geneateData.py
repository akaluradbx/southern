import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Generate 100 customers
with open('customer.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['customer_id', 'first_name', 'last_name', 'email', 'city'])
    for i in range(1, 101):
        first = fake.first_name()
        last = fake.last_name()
        writer.writerow([i, first, last, f"{first.lower()}.{last.lower()}@email.com", fake.city()])

# Generate 50 products
categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']
with open('product.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['product_id', 'product_name', 'category', 'price'])
    for i in range(1, 51):
        category = random.choice(categories)
        product = fake.word().capitalize() + " " + fake.word().capitalize()
        writer.writerow([i, product, category, round(random.uniform(5, 100), 2)])

# Generate 1000 orders
with open('order.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['order_id', 'customer_id', 'product_id', 'order_date', 'quantity'])
    for i in range(1, 1001):
        writer.writerow([
            i,
            random.randint(1, 100),
            random.randint(1, 50),
            (datetime(2025, 1, 1) + timedelta(days=random.randint(0, 179))).strftime('%Y-%m-%d'),
            random.randint(1, 10)
        ])

