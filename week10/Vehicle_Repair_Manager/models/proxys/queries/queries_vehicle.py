create_vehicle_table = """
CREATE TABLE IF NOT EXISTS vehicle (
ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
CATEGORY VARCHAR(20),
MAKE TEXT NOT NULL,
MODEL VARCHAR(50) NOT NULL,
REGISTER_NUMBER TEXT UNIQUE NOT NULL,
GEAR_BOX TEXT NOT NULL,
OWNER INTEGER NOT NULL,
FOREIGN KEY (OWNER) REFERENCES client(BASE_ID)
)
"""

insert_vehicle = """
INSERT INTO vehicle (CATEGORY, MAKE, MODEL, REGISTER_NUMBER, GEAR_BOX, OWNER)
VALUES (:category, :make, :model, :register_number, :gear_box, :owner)
"""

delete_vehicle = """
DELETE FROM vehicle
WHERE id=?
"""

get_vehicles_for_client = """
SELECT vehicle.*
FROM vehicle
JOIN client
ON vehicle.OWNER=client.BASE_ID
JOIN base_user
ON client.BASE_ID=base_user.ID
WHERE client.BASE_ID=?
"""

update_vehicle = """
UPDATE vehicle
SET CATEGORY=:category, MAKE=:make, MODEL=:model,
    REGISTER_NUMBER=:register_number, GEAR_BOX=:gear_box
WHERE ID=:id
"""

query_vehicle = """
SELECT *
FROM vehicle
WHERE ID=?
"""
