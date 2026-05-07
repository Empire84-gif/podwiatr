import secrets

from datetime import datetime, timedelta

from werkzeug.security import generate_password_hash

from db import get_connection


ADMIN_NAME = "Administrator"
ADMIN_EMAIL = "office@handkeholding.com"
ADMIN_PASSWORD = "admin12345"


def now_text():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_admin():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id
    FROM users
    WHERE lower(email) = ?
    LIMIT 1
    """, (ADMIN_EMAIL.lower(),))

    existing_user = cursor.fetchone()

    if existing_user:
        print("Admin already exists.")
        conn.close()
        return

    password_hash = generate_password_hash(ADMIN_PASSWORD)

    cursor.execute("""
    INSERT INTO users (
        full_name,
        email,
        password_hash,
        role,
        is_active,
        activated_at,
        updated_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        ADMIN_NAME,
        ADMIN_EMAIL.lower(),
        password_hash,
        "admin",
        1,
        now_text(),
        now_text()
    ))

    conn.commit()
    conn.close()

    print("Admin created.")
    print("")
    print("Email:")
    print(ADMIN_EMAIL)
    print("")
    print("Password:")
    print(ADMIN_PASSWORD)


if __name__ == "__main__":
    create_admin()