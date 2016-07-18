.read sp16data.sql
.read fa15data.sql

-- Q2
CREATE TABLE obedience AS
  select seven, hilfinger FROM students;

-- Q3
CREATE TABLE smallest_int AS
  select time, smallest FROM students WHERE smallest > 12 ORDER BY smallest LIMIT 20;

-- Q4
CREATE TABLE greatstudents AS
  select a.date, a.number, a.pet, a.color, b.color FROM students AS a, fa15students AS b WHERE a.date = b.date AND a.number = b.number AND a.pet = b.pet;

-- Q5
CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b WHERE a.time < b.time AND a.pet = b.pet AND a.song = b.song;;

-- Q6
CREATE TABLE fa15favnum AS
  SELECT number, COUNT(*) AS count FROM fa15students GROUP BY number ORDER BY count DESC LIMIT 1;

CREATE TABLE fa15favpets AS
  SELECT pet, COUNT(*) AS count FROM fa15students GROUP BY pet ORDER BY count DESC LIMIT 10;

CREATE TABLE sp16favpets AS
   SELECT pet, COUNT(*) AS count FROM students GROUP BY pet ORDER BY count DESC LIMIT 10;

CREATE TABLE sp16dragon AS
  SELECT pet, COUNT(*) FROM students WHERE pet = 'dragon';

CREATE TABLE sp16alldragons AS
  SELECT pet, COUNT(*) FROM students WHERE pet LIKE '%dragon%';

CREATE TABLE obedienceimage AS
  select seven, hilfinger, COUNT(*) FROM students WHERE seven = '7'  GROUP BY hilfinger;

-- Q7
CREATE TABLE pairs AS
  with
    helper(cur) as (
        SELECT 0 UNION
        SELECT cur + 1 FROM helper
            WHERE cur < 42
    )
    SELECT a.cur AS x, b.cur AS y FROM helper AS a, helper AS b WHERE a.cur <= b.cur;

