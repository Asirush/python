from database_module import DataBase

if __name__ == "__main__":
    db = DataBase("user1", "12345", 5432)
    db2 = DataBase("user2", "56789", 3360)

    print()