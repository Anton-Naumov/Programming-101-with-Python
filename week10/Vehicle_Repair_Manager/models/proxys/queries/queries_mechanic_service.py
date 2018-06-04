create_mechanic_service_table = """
CREATE TABLE IF NOT EXISTS mechanic_service (
ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
MECHANIC_ID INTEGER NOT NULL,
SERVICE_ID INTEGER,
FOREIGN KEY (MECHANIC_ID) REFERENCES mechanic(BASE_ID)
FOREIGN KEY (SERVICE_ID) REFERENCES service(ID)
)
"""

insert_mechanic_service = """
INSERT INTO mechanic_service (MECHANIC_ID, SERVICE_ID)
VALUES (:mechanic_id, :service_id)
"""

create_service_table = """
CREATE TABLE IF NOT EXISTS service (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NAME VARCHAR(50) UNIQUE NOT NULL
)
"""

insert_service = """
INSERT INTO service (NAME)
VALUES (?)
"""

update_service_to_mechanic = """
UPDATE mechanic_service
SET SERVICE_ID=?
WHERE ID=?
"""

remove_service_from_mechanic_service = """
UPDATE mechanic_service
SET SERVICE_ID=NULL
WHERE ID=?
"""

query_service = """
SELECT *
FROM service
WHERE NAME=?
"""

query_all_services = """
SELECT NAME
FROM service
"""
