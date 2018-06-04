create_client_table = """
CREATE TABLE IF NOT EXISTS client (
BASE_ID INTEGER NOT NULL PRIMARY KEY,
FOREIGN KEY (BASE_ID) REFERENCES base_user(ID)
)
"""

insert_client_in_table = """
INSERT INTO client
VALUES (:id)
"""

query = """
SELECT user.*
FROM client
JOIN base_user as user
ON client.BASE_ID=user.ID
WHERE user.ID=? OR user.USER_NAME=? OR user.EMAIL=? OR user.PHONE_NUMBER=?
"""
