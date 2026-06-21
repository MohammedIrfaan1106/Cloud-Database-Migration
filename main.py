
from migration import migrate_data

while True:
    print("\n=== CLOUD DATABASE MIGRATION ===")
    print("1. Migrate Data")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        migrate_data()
    elif choice == "2":
        break
