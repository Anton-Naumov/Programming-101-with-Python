SELECT (SUM(pc.speed) + SUM(laptop.speed)) / (COUNT(pc.speed) + count(laptop.speed)) as AVERAGE_SPEED
  FROM pc, laptop;

SELECT product.maker, AVG(laptop.screen)
  FROM product
  LEFT JOIN laptop
    ON product.MODEL=laptop.MODEL
  GROUP BY product.maker;

SELECT (SUM(p_LP) + SUM(p_PC)) / (COUNT(p_LP) + COUNT(p_PC))
  FROM (SELECT price as p_LP
	  FROM laptop
	  JOIN product
	    ON laptop.MODEL=product.MODEL
	  WHERE product.MAKER="B"
	),
       (SELECT price as p_PC
	  FROM pc
	  JOIN product
	    ON pc.MODEL=product.MODEL
	  WHERE product.MAKER="B"
	);