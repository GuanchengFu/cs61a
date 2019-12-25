.read lab12.sql

-- Q5
CREATE TABLE greatstudents AS
  SELECT a.date, a.color, a.pet, a.number, b.number
  FROM students AS a, fa17students AS b
  WHERE a.date = b.date
  AND a.color = b.color
  AND a.pet = b.pet;

-- Q6
CREATE TABLE sevens AS
  SELECT a.seven
  FROM students AS a, checkboxes as b
  WHERE a.number = 7
  AND b.'7' = "True"
  AND a.time = b.time;

-- Q7
CREATE TABLE fa17favnum AS
  SELECT number, COUNT(*) AS count FROM fa17students GROUP BY number
  ORDER BY count DESC limit 1;


CREATE TABLE fa17favpets AS
  SELECT pet, COUNT(*) AS count from fa17students GROUP BY pet
  ORDER BY count DESC, pet
  limit 10;


CREATE TABLE sp18favpets AS
  SELECT pet, COUNT(*) AS count from students GROUP BY pet
  ORDER BY count DESC, pet
  limit 10;


CREATE TABLE sp18dog AS
  SELECT pet, COUNT(*) as count from students 
  where pet = "dog"
  group by pet;


CREATE TABLE sp18alldogs AS
  SELECT "dog" as name, COUNT(*) as count from students 
  where pet LIKE '%dog%';


CREATE TABLE obedienceimages AS
  SELECT seven, denero, COUNT(*)
  from students
  where seven = '7'
  group by denero;

-- Q8
CREATE TABLE smallest_int_count AS
  SELECT smallest, COUNT(*) AS count from students
  group by smallest
  order by smallest;
