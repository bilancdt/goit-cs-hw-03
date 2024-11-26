from faker import Faker
import psycopg2

fake = Faker()

# Підключення DB
conn = psycopg2.connect(
    dbname="postgres", 
    user="postgres",
    password="mypass12345",
    host="localhost",
    port=5432
)

cur = conn.cursor()

# Заповнення таблиці status
statuses = ['new', 'in progress', 'completed']
cur.executemany("INSERT INTO status (name) VALUES (%s) ON CONFLICT DO NOTHING", [(status,) for status in statuses])

# users
users = [(fake.name(), fake.unique.email()) for _ in range(10)]
cur.executemany("INSERT INTO users (fullname, email) VALUES (%s, %s)", users)

# tasks
tasks = [
    (fake.sentence(nb_words=4), fake.text(), fake.random_int(min=1, max=len(statuses)), fake.random_int(min=1, max=10))
    for _ in range(20)
]
cur.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", tasks)

# Підтвердж. 
conn.commit()
cur.close()
conn.close()

print("Database seeded successfully!")
