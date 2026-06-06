import sqlite3

# ---------- CONNECT ----------
def connect():
    return sqlite3.connect("app.db")


# ---------- CREATE DATABASE ----------
def create_database():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
    """)

    conn.commit()
    conn.close()
    print("Database created successfully")


# ---------- CREATE (ADD USER) ----------
def add_user(name, age):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))

    conn.commit()
    conn.close()
    print("User added")


# ---------- READ (GET USERS) ----------
def get_users():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()
    return users


# ---------- UPDATE USER ----------
def update_user(user_id, name, age):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET name=?, age=? WHERE id=?",
        (name, age, user_id)
    )

    conn.commit()
    conn.close()
    print("User updated")


# ---------- DELETE USER ----------
def delete_user(user_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))

    conn.commit()
    conn.close()
    print("User deleted")


# ---------- TESTING (OPTIONAL) ----------
if __name__ == "__main__":
    create_database()

    add_user("Ali", 23)
    add_user("Sara", 21)

    print(get_users())

    update_user(1, "Ali Khan", 25)

    print(get_users())

    delete_user(2)

    print(get_users())