create_repair_hour_table = """
CREATE TABLE IF NOT EXISTS repair_hour (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
DATE TEXT NOT NULL,
START_HOUR TEXT NOT NULL,
VEHICLE INTEGER,
BILL REAL NOT NULL,
MECHANIC_SERVICE INTEGER UNIQUE NOT NULL,
FOREIGN KEY (VEHICLE) REFERENCES vehicle(ID)
FOREIGN KEY (MECHANIC_SERVICE) REFERENCES mechanic_service(ID)
)
"""

insert_repair_hour = """
INSERT INTO repair_hour (DATE, START_HOUR, VEHICLE, BILL, MECHANIC_SERVICE)
VALUES (:date, :start_hour, NULL, :bill, :mechanic_service)
"""

list_all_free_hours = """
SELECT ID, DATE, START_HOUR
FROM repair_hour
WHERE VEHICLE IS NULL
"""

list_all_busy_hours = """
SELECT repair_hour.ID, repair_hour.DATE, repair_hour.START_HOUR
FROM repair_hour
JOIN mechanic_service
ON repair_hour.MECHANIC_SERVICE=mechanic_service.ID
JOIN mechanic
ON mechanic_service.MECHANIC_ID=mechanic.BASE_ID
WHERE VEHICLE IS NOT NULL AND mechanic.BASE_ID=?
"""

list_all_free_hours_for_mechanic = """
SELECT repair_hour.ID, repair_hour.DATE, repair_hour.START_HOUR
FROM repair_hour
JOIN mechanic_service
ON repair_hour.MECHANIC_SERVICE=mechanic_service.ID
JOIN mechanic
ON mechanic_service.MECHANIC_ID=mechanic.BASE_ID
WHERE VEHICLE IS NULL AND mechanic.BASE_ID=?
"""

list_all_free_hours_for_mechanic_for_date = """
SELECT repair_hour.ID, repair_hour.DATE, repair_hour.START_HOUR
FROM repair_hour
JOIN mechanic_service
ON repair_hour.MECHANIC_SERVICE=mechanic_service.ID
JOIN mechanic
ON mechanic_service.MECHANIC_ID=mechanic.BASE_ID
WHERE VEHICLE IS NULL AND DATE=? AND mechanic.BASE_ID=?
"""

list_all_busy_hours_for_date = """
SELECT repair_hour.ID, repair_hour.DATE, repair_hour.START_HOUR
FROM repair_hour
JOIN mechanic_service
ON repair_hour.MECHANIC_SERVICE=mechanic_service.ID
JOIN mechanic
ON mechanic_service.MECHANIC_ID=mechanic.BASE_ID
WHERE VEHICLE IS NOT NULL AND DATE=? AND mechanic.BASE_ID=?
"""

list_all_free_hours_for_date = """
SELECT ID, DATE, START_HOUR
FROM repair_hour
WHERE VEHICLE IS NULL AND DATE=?
"""

list_repair_hours_for_client = """
SELECT repair_hour.ID, repair_hour.DATE, repair_hour.START_HOUR, repair_hour.BILL, vehicle.*
FROM (SELECT *
      FROM repair_hour
      WHERE repair_hour.VEHICLE IS NOT NULL) as repair_hour
JOIN vehicle
ON repair_hour.VEHICLE=vehicle.ID
JOIN client
ON vehicle.OWNER=client.BASE_ID
WHERE client.BASE_ID=?
"""

save_repair_hour = """
UPDATE repair_hour
SET VEHICLE=?
WHERE ID=?
"""

update_repair_hour_by_id = """
UPDATE repair_hour
SET START_HOUR=:start_hour, BILL=:bill
WHERE ID=:id
"""

delete_repair_hour = """
UPDATE repair_hour
SET VEHICLE=NULL
WHERE ID=?
"""

query_repair_hour = """
SELECT *
FROM repair_hour
WHERE ID=?
"""
