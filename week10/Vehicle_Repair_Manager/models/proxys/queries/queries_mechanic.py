create_mechanic_table = """
CREATE TABLE IF NOT EXISTS mechanic (
BASE_ID INTEGER NOT NULL PRIMARY KEY,
TITLE VARCHAR(20),
FOREIGN KEY (BASE_ID) REFERENCES base_user(ID)
)
"""

insert_mechanic = """
INSERT INTO mechanic
VALUES (?, ?)
"""

query = """
SELECT user.*, mechanic.TITLE
FROM mechanic
JOIN base_user as user
ON mechanic.BASE_ID=user.ID
WHERE user.ID=? OR user.USER_NAME=? OR user.EMAIL=? OR user.PHONE_NUMBER=?
"""

query_all = """
SELECT *
FROM mechanic
JOIN base_user
ON mechanic.BASE_ID=base_user.ID
"""
