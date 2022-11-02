--  creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, CONSTRAINT cities_pk PRIMARY KEY (id), state_id INT NOT NULL, CONSTRAINT child_ibfk_1 FOREIGN KEY (state_id) REFERENCES states(id));