# Wehelp Week5 works

## task 2  Create database and table in your MySQL server

* ### Create a new database named website.
  ```
  create database website;
  ```
* ### Create a new table named member, in the website database, designed as below:
  ```
  use website;
  CREATE TABLE member (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    username varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    follower_count int unsigned NOT NULL DEFAULT 0,
    time datetime NOT NULL DEFAULT(CURRENT_TIME())
  );
  ```
## task3 SQL CRUD

* ### INSERT a new row to the member table where name, username and password must
  ```
  INSERT INTO member(name, username, password)
  VALUES('test', 'test', 'test');
  ```
* ### be set to test. INSERT additional 4 rows with arbitrary data.
  ```
  INSERT INTO member(name, username, password)
  VALUES('A', 'AAA', 123);
  INSERT INTO member(name, username, password)
  VALUES('B', 'bbb', 456);
  INSERT INTO member(name, username, password)
  VALUES('C', 'ccc', 789);
  INSERT INTO member(name, username, password)
  VALUES('D', 'ddd', 012);
  ```
* ### SELECT all rows from the member table.
  ```
  SELECT *   
  FROM member;
  ```
* ### SELECT all rows from the member table, in descending order of time.
  ```
  SELECT * 
  FROM member
  ORDER BY time DESC;
  ```
* ### SELECT total 3 rows, second to fourth, from the member table, in descending order of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
  ```
  SELECT *   
  FROM member
  ORDER BY time DESC
  LIMIT 1, 3;
  ```
* ### SELECT rows where username equals to test.
  ```
  SELECT * 
  FROM member
  WHERE username = 'test';
  ```
* ### SELECT rows where name includes the es keyword.
  ```
  SELECT * 
  FROM member 
  WHERE name LIKE '%es%';
  ```
* ### SELECT rows where both username and password equal to test.
  ```
  SELECT * 
  FROM member 
  WHERE name = 'test' AND password = 'test';
  ```
* ### UPDATE data in name column to test2 where username equals to test.
  ```
  UPDATE member
  SET name = 'test2'
  WHERE username = 'test';
  ```

## task4 SQL Aggregation Functions
 * ### SELECT how many rows from the member table.
   ```
   SELECT COUNT(*)
   FROM member;
   ```
 * ### SELECT the sum of follower_count of all the rows from the member table.
    ##### pretreat update 4 follower_count to 4 item 
   ```
   UPDATE member
   SET follower_count = 1
   WHERE = 1
   UPDATE member
   SET follower_count = 2
   WHERE = 2
   UPDATE member
   SET follower_count = 3
   WHERE = 3
   UPDATE member
   SET follower_count = 4
   WHERE = 4
   ```
     ##### SELECT the sum of follower_count of all the rows from the member table. 
   ```
   SELECT SUM(follower_count) 
   FROM member;  
   ```
 * ### SELECT the average of follower_count of all the rows from the member table.
   ```
   SELECT AVG(follower_count)
   FROM member;
   ```
 * ### SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table
   ```
   SELECT AVG(follower_count)
   FROM (
	 SELECT follower_count
	 FROM member
	 ORDER BY follower_count DESC
	 LIMIT 2
	 ) AS queryparameter;
   ```
## task5 SQL JOIN
  * Create a new table named message, in the website database. designed as below:
    ```
    CREATE TABLE message (
			id bigint AUTO_INCREMENT,
	 		member_id bigint NOT NULL,
	 		content varchar(255) NOT NULL,
	 		like_count int unsigned NOT NULL DEFAULT 0,
			time datetime NOT NULL DEFAULT (CURRENT_TIME()),
			PRIMARY KEY(id),
			FOREIGN KEY(member_id) REFERENCES member(id)
		);
    ```
    ##### update 5 data
    ```
    INSERT INTO message(member_id, content, like_count)
		VALUES (5, 'IPA', 5);
		INSERT INTO message(member_id, content, like_count)
		VALUES (4, 'ALE', 6);
		INSERT INTO message(member_id, content, like_count)
		VALUES (3, 'BOCK', 7);
		INSERT INTO message(member_id, content, like_count)
		VALUES (2, 'DUNKEL', 8);
		INSERT INTO message(member_id, content, like_count)
		VALUES (1, 'KOLSCH', 9);
    ```
  * SELECT all messages, including sender names. We have to JOIN the member table to get that.
    ```
    SELECT * 
		FROM message
		INNER JOIN member ON message.member_id = member.id;
    ```
  * SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
    ```
    SELECT * 
		FROM message
		INNER JOIN member ON message.member_id = member.id
		WHERE username = 'test';
    ```
  * Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
    ```
    SELECT AVG(like_count) 
		FROM message
		INNER JOIN member ON message.member_id = member.id
		WHERE username = 'test';
    ```
  * Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
    ```
    SELECT AVG(like_count) 
		FROM message
		INNER JOIN member ON message.member_id = member.id
		GROUP BY username; 
    ```
