-- create a new table 'secon_table'

CREATE TABLE IF not exists second_table(id INT,name VARCHAR(256), score INT);
INSERT INTO second_table(ID, NAME, SCORE)
VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
