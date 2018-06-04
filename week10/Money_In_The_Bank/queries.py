create_query = """CREATE TABLE IF NOT EXISTS clients (
id SERIAL PRIMARY KEY,
username VARCHAR(128) UNIQUE,
password VARCHAR(128),
balance REAL DEFAULT 0,
message TEXT,
email TEXT NOT NULL UNIQUE
)"""

change_balance_by_id = """
UPDATE clients
SET balance = %s
WHERE id = %s
"""

drop_query = """
DROP TABLE IF EXISTS clients;
"""

update_message = """
UPDATE clients
SET message = %s
WHERE id = %s
"""

change_password = """
UPDATE clients
SET password = %s
WHERE id = %s
"""

insert_sql = """
INSERT INTO clients (username, password, email)
VALUES (%s, %s, %s)
"""

select_query = """
SELECT id, username, balance, message, email
FROM clients
"""

select_query_by_name = """
SELECT id, username, balance, message, email
FROM clients
WHERE username = %s
LIMIT 1
"""

get_password_by_username = """
SELECT password, email
FROM clients
WHERE username = %s
LIMIT 1
"""

select_query_by_name_and_password = """
SELECT id, username, balance, message, email
FROM clients
WHERE username = %s AND password = %s
LIMIT 1
"""
