SELECT STARNAME, MOVIEYEAR
  FROM starsin
  GROUP BY STARNAME
    HAVING MIN(MOVIEYEAR);
    
SELECT moviestar.NAME, MIN(starsin.MOVIEYEAR) - SUBSTR(moviestar.BIRTHDATE,1,4) as DEBUT
  FROM starsin
  JOIN moviestar
    ON starsin.STARNAME=moviestar.NAME
  GROUP BY moviestar.NAME;

SELECT studio.NAME, studio.ADDRESS, AVG(movie.LENGTH)
   FROM studio
   LEFT JOIN movie
     ON movie.STUDIONAME=studio.NAME
   GROUP BY studio.NAME;