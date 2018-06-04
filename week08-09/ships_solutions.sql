SELECT outcomes.SHIP
  FROM outcomes
  JOIN ships
    ON outcomes.SHIP=ships.NAME
  JOIN battles
    ON outcomes.BATTLE=battles.NAME
  WHERE SUBSTR(battles.DATE,1,4)="1942";

SELECT ships.NAME
  FROM ships
  LEFT JOIN outcomes
    ON outcomes.SHIP=ships.NAME
  WHERE outcomes.SHIP IS NULL;