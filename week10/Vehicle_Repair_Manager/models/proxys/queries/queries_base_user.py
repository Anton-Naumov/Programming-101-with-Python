drop_base_user_table = """
DROP TABLE IF EXISTS base_user
"""

create_base_user_table = """
CREATE TABLE IF NOT EXISTS base_user (
ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
USER_NAME  VARCHAR(20) UNIQUE NOT NULL,
EMAIL VARCHAR(20) UNIQUE NOT NULL,
PHONE_NUMBER VARCHAR(20) UNIQUE NOT NULL,
ADDRESS TEXT
);
"""

insert_in_base_user = """
INSERT INTO base_user (USER_NAME, EMAIL, PHONE_NUMBER, ADDRESS)
VALUES (:user_name,:email,:phone_number,:address);
"""

query = """
SELECT *
FROM base_user
WHERE ID=? OR USER_NAME=? OR EMAIL=? OR PHONE_NUMBER=?
"""
