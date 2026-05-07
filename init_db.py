from db import get_connection


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        created_at TEXT DEFAULT CURRENT_TIMESTAMP,

        status TEXT DEFAULT 'new',

        source_url TEXT,

        event_label TEXT,
        event_date_from TEXT,
        event_date_to TEXT,
        event_date_label TEXT,

        participant_full_name TEXT,
        birth_date TEXT,
        pesel TEXT,

        participant_phone TEXT,

        address TEXT,
        city_postal_code TEXT,

        guardian_full_name TEXT,
        guardian_phone TEXT,
        guardian_email TEXT,

        referrer_full_name TEXT,

        notes TEXT,

        raw_payload TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        updated_at TEXT,

        full_name TEXT NOT NULL,

        email TEXT NOT NULL UNIQUE,

        password_hash TEXT,

        role TEXT NOT NULL DEFAULT 'client',

        is_active INTEGER NOT NULL DEFAULT 0,

        activated_at TEXT,
        last_login_at TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS account_tokens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        created_at TEXT DEFAULT CURRENT_TIMESTAMP,

        user_id INTEGER NOT NULL,

        token TEXT NOT NULL UNIQUE,

        token_type TEXT NOT NULL,

        expires_at TEXT NOT NULL,

        used_at TEXT,

        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_users_email
    ON users(email)
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_account_tokens_token
    ON account_tokens(token)
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_account_tokens_user_type
    ON account_tokens(user_id, token_type)
    """)

    conn.commit()
    conn.close()

    print("Database initialized.")


if __name__ == "__main__":
    init_db()