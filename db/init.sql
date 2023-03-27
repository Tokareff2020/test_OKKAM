CREATE TABLE respondent_table(
    id INTEGER PRIMARY KEY,
    Date INTEGER,
    respondent INTEGER,
    Sex INTEGER,
    CHECK(Sex > 0), CHECK(Sex < 3),
    Age INTEGER,
    Weight FLOAT);
COPY respondent_table from '/db/db_dump.csv' DELIMITER ';' CSV HEADER;
