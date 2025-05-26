# app/mock_data.py
from datetime import datetime, timedelta
import random
import faker

fake = faker.Faker()


def generate_mock_data(n=100):
    subjects = ["Economy", "Technology", "Health", "Education", "Energy"]
    data = []

    for i in range(n):
        item = {
            "id": i,
            "title": fake.sentence(nb_words=6),
            "subject": random.choice(subjects),
            "description": fake.text(max_nb_chars=200),
            "link": fake.url(),
            "date": (datetime.now() - timedelta(days=random.randint(0, 1000))).isoformat(),
        }
        data.append(item)
    return data


MOCK_DATA = generate_mock_data()
