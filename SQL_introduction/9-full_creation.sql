-- create table second_table if i does not exist
CREATE TABLE IF NOT EXISTS second_table(
    id INT,
    name VARCHAR(256),
    score INT
);

-- create john entry
INSERT INTO second_table VALUES (1, "John", 10);
-- create alex entry
INSERT INTO second_table VALUES (2, "Alex", 3);
-- create bob entry
INSERT INTO second_table VALUES (3, "Bob", 14);
-- create george entry
INSERT INTO second_table VALUES (4, "George", 8);
