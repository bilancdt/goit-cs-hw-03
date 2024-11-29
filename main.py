from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Підключення до MongoDB
uri = "mongodb+srv://bilancdt:Ace12345@cluster0.hgkpi.mongodb.net/?retryWrites=true&w=majority"
try:
    client = MongoClient(uri, server_api=ServerApi('1'))
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit()

# Створення бази даних та колекції
db = client["cats_db"]
collection = db["cats"]

# --- Create ---
def create_cat(name, age, features):
    """Створює нового кота."""
    try:
        cat = {"name": name, "age": age, "features": features}
        collection.insert_one(cat)
        print(f"Cat {name} added successfully!")
    except Exception as e:
        print(f"Error creating cat: {e}")

# --- Read ---
def read_all_cats():
    """Виводить усіх котів у базі."""
    try:
        cats = collection.find()
        print("All Cats:")
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Error reading cats: {e}")

def read_cat_by_name(name):
    """Виводить інформацію про кота за ім'ям."""
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"No cat found with the name {name}")
    except Exception as e:
        print(f"Error reading cat: {e}")

# --- Update ---
def update_cat_age(name, new_age):
    """Оновлює вік кота за ім'ям."""
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count > 0:
            print(f"Age of {name} updated to {new_age}.")
        else:
            print(f"No cat found with the name {name}.")
    except Exception as e:
        print(f"Error updating cat age: {e}")

def add_feature_to_cat(name, feature):
    """Додає характеристику до списку кота за ім'ям."""
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": feature}})
        if result.modified_count > 0:
            print(f"Feature '{feature}' added to {name}.")
        else:
            print(f"No cat found with the name {name}.")
    except Exception as e:
        print(f"Error updating cat features: {e}")

# --- Delete ---
def delete_cat_by_name(name):
    """Видаляє кота за ім'ям."""
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Cat {name} deleted.")
        else:
            print(f"No cat found with the name {name}.")
    except Exception as e:
        print(f"Error deleting cat: {e}")

def delete_all_cats():
    """Видаляє всіх котів у базі."""
    try:
        result = collection.delete_many({})
        print(f"{result.deleted_count} cats deleted.")
    except Exception as e:
        print(f"Error deleting all cats: {e}")

# --- Виконання ---
if __name__ == "__main__":
    create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    create_cat("murzik", 5, ["сірий", "любить рибу", "грає з іграшками"])
    create_cat("oldboy", 15, ["пенсіонер", "любить кітікет", "просто релаксує"])
    create_cat("bon", 4, ["сіам", "забіяка", "ганяє сусідських собак і людей"])
    create_cat("nafania", 70, ["брудний", "міфічна істота", "виходить вночі"])

    print("\n--- Read All Cats ---")
    read_all_cats()

    print("\n--- Read Cat by Name ---")
    read_cat_by_name("barsik")

    print("\n--- Update Cat Age ---")
    update_cat_age("barsik", 4)

    print("\n--- Add Feature to Cat ---")
    add_feature_to_cat("barsik", "любить спати на дивані")

    print("\n--- Delete Cat by Name ---")
    delete_cat_by_name("murzik")

    print("\n--- Delete All Cats ---")
    delete_all_cats()
