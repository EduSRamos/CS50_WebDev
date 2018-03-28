---------------------------->> 0. Installation (not part of lecture)
-- https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04


---------------------------->> 1. CREATE a Table

CREATE TABLE flights ( -- create a new table called flight
    -- what type of information will my table hold?
    -- <name> + <type> + <constraint>
    -- "PRIMARY KEY": primary way I'll reference a flight
    -- "NOT NULL": must have a value (you can make it non-mandatory)
    --      database will refuse an entry without this field
    id SERIAL PRIMARY KEY, -- PARADIGM: make it easier to reference entries
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
); -- semi-colon signals the end of the command

-- Once I have a SQL database up and running (e.g., in this case you need to
-- start a Postgre server - locally on your computer or find databases that are
-- hosted online)

-- >> psql : let's you enter PostgreSQL commands
--      >> sudo -i -u postgres
--      >> postgres@eduardo-XPS13:~$ createdb lecture3
--      >> postgres@eduardo-XPS13:~$ psql lecture3
--      >> lecture3=# <paste code above to create table>
--          >> CREATE TABLE (success message)
--      >> lecture3=# \d (check creation of table)
--      >> lecture3=# \q (leave)

-- Connect to a database online
--      >> psql <url>   - database online

---------------------------->> 2. Constraints
-- NOT NULL
-- UNIQUE (e.g., user names)
-- PRIMARY KEY
-- DEFAULT
--      give columns a default value
-- CHECK
--      e.g., I want my columns to have values that are less than 50
-- ...


---------------------------->> 3. INSERT
-- The next command could be in a single line, but for clarity has been broken
-- down.
-- (origin, ...) specifies the names of the columns I want to add info
INSERT INTO flights
    (origin, destination, duration) -- 'id' will increment on its own - serial
    VALUES ('New York', 'London', 415); -- same order of columns

-- >> lecture3=# <paste code above to insert>
--      >> INSERT 0 1 (automatic message)

INSERT INTO flights (origin, destination, duration)
    VALUES ('Shanghai', 'Paris', 760);
INSERT INTO flights (origin, destination, duration)
    VALUES ('Istanbul', 'Tokyo', 700);
INSERT INTO flights (origin, destination, duration)
    VALUES ('New York', 'Paris', 435);
INSERT INTO flights (origin, destination, duration)
    VALUES ('Moscow', 'Paris', 245);
INSERT INTO flights (origin, destination, duration)
    VALUES ('Lima', 'New York', 455);


---------------------------->> 4. SELECT
SELECT * FROM flights; -- '*' means 'select everything' (all columns)
SELECT origin, destination FROM flights; -- just these columns
SELECT * FROM flights WHERE id = 3;
SELECT * FROM flights WHERE origin = 'New York';
SELECT * FROM flights WHERE duration > 500;
SELECT * FROM flights WHERE destination = 'Paris' AND duration > 500;
SELECT * FROM flights WHERE destination = 'Paris' OR duration > 500;
SELECT AVG(duration) FROM flights WHERE destination='New York';
SELECT COUNT(*) FROM flights WHERE origin = 'New York'; -- number of entries
SELECT MIN(duration) FROM flights;
    SELECT * FROM flights WHERE duration = 245; -- ok
    -- SELECT * FROM flights WHERE duration = MIN(duration); -- erro
SELECT * FROM flights WHERE origin IN ('New York', 'Lima'); -- range of values
SELECT * FROM flights WHERE origin LIKE '%a%'; -- % = any text; origins with 'a'

---------------------------->> 4.1. Functions
-- SUM, COUNT, MIN, MAX, AVG, ...


---------------------------->> 5. UPDATE
UPDATE flights
    SET duration = 430
    WHERE origin = 'New York' AND destination = 'London';


---------------------------->> 6. DELETE
DELETE FROM flights
    WHERE id = 1;

-- obs.: serial numbers don't fill in, i.e., the next entry won't get id=1, they
-- just keep adding up.


---------------------------->> 7. Other useful clauses
