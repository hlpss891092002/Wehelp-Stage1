# Wehelp Week5 works

## task 2 Create database and table in your MySQL server

- ### Create a new database named website.
  ```
  create database website;
  ```
  ![taks2-1 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task2%20-1.png)
- ### Create a new table named member, in the website database, designed as below:
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
  ![taks2-2 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task2-2-1use%20website.png)
  ![taks2-2 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task2-2-2CREATE%20TABLE%20member.png)

## task3 SQL CRUD

- ### INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.
  ```
  INSERT INTO member(name, username, password)
  VALUES('test', 'test', 'test');
  INSERT INTO member(name, username, password)
  VALUES('A', 'AAA', 123);
  INSERT INTO member(name, username, password)
  VALUES('B', 'bbb', 456);
  INSERT INTO member(name, username, password)
  VALUES('C', 'ccc', 789);
  INSERT INTO member(name, username, password)
  VALUES('D', 'ddd', 012);
  ```
  ![taks3-1 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task3-1%20INSERT.png)
- ### SELECT all rows from the member table.
  ```
  SELECT *
  FROM member;
  ```
  ![taks3-2 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task3-2%20SELECT%20ALL%20.png)
- ### SELECT all rows from the member table, in descending order of time.
  ```
  SELECT *
  FROM member
  ORDER BY time DESC;
  ```
  ![taks3-3 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task3-3%20SELECT%20ALL%20%20ORDER%20BY%20DESC%20.png)
- ### SELECT total 3 rows, second to fourth, from the member table, in descending order of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
  ```
  SELECT *
  FROM member
  ORDER BY time DESC
  LIMIT 1, 3;
  ```
  ![taks3-4 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task3-4%20SELECT%202-4%20rows%20%20ORDER%20BY%20DESC%20.png)
- ### SELECT rows where username equals to test.
  ```
  SELECT *
  FROM member
  WHERE username = 'test';
  ```
  ![taks3-5 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task3-5%20rows%20where%20username%20equals%20to%20test%20.png)
- ### SELECT rows where name includes the es keyword.
  ```
  SELECT *
  FROM member
  WHERE name LIKE '%es%';
  ```
  ![taks3-6 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task3-6%20SELECT%20includes%20the%20es%20keyword%20.png)
- ### SELECT rows where both username and password equal to test.
  ```
  SELECT *
  FROM member
  WHERE username = 'test' AND password = 'test';
  ```
  ![taks3-7 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task3-7%20%20SELECT%20rows%20where%20both%20username%20and%20password%20equal%20to%20test%20.png)
- ### UPDATE data in name column to test2 where username equals to test.
  ```
  UPDATE member
  SET name = 'test2'
  WHERE username = 'test';
  ```
  ![taks3-8 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task3-8%20UPDATE%20test2%20in%20name%20column%20%20where%20username%20%20equal%20to%20test%20.png)

## task4 SQL Aggregation Functions

- ### SELECT how many rows from the member table.
  ```
  SELECT COUNT(*)
  FROM member;
  ```
  ![taks4-1 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task4-1%20SELECT%20how%20many%20rows%20from%20the%20member%20table.png)
- ### SELECT the sum of follower_count of all the rows from the member table.
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
  ![taks4-2-1 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task4-2%20pretreat.png)
  ![taks4-2-2 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task4-2%20pretreat-2.png)
  ##### SELECT the sum of follower_count of all the rows from the member table.
  ```
  SELECT SUM(follower_count)
  FROM member;
  ```
  ![taks4-2-3 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task4-2SELECT%20the%20sum%20of%20follower_count%20of%20all%20the%20rows%20from%20the%20member%20table.png)
- ### SELECT the average of follower_count of all the rows from the member table.
  ```
  SELECT AVG(follower_count)
  FROM member;
  ```
  ![taks4-3 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task4-3%20SELECT%20the%20average%20of%20follower_count%20of%20all%20the%20rows%20from%20the%20member%20table..png)
- ### SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table
  ```
  SELECT AVG(follower_count)
  FROM (
   SELECT follower_count
   FROM member
   ORDER BY follower_count DESC
   LIMIT 2
   ) AS queryparameter;
  ```
  ![taks4-4 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task4-4%20SELECT%20the%20average%20of%20follower_count%20of%20the%20first%202%20rows%2C%20in%20descending%20order%20of%20follower_count%2C%20from%20the%20member%20table.png)

## task5 SQL JOIN

- Create a new table named message, in the website database. designed as below:
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
  ![taks5-1-1 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task5-1%20Create%20a%20new%20table%20named%20message.png)
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
  ![taks5-1-2 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task5-1.1%20update%205%20data.png)
- SELECT all messages, including sender names. We have to JOIN the member table to get that.
  ```
  SELECT *
  	FROM message
  	INNER JOIN member ON message.member_id = member.id;
  ```
  ![taks5-2 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task5-2%20%20SELECT%20all%20messages%2C%20including%20sender%20names.png)
- SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
  ```
  SELECT *
  	FROM message
  	INNER JOIN member ON message.member_id = member.id
  	WHERE username = 'test';
  ```
  ![taks5-3 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task5-3%20%20SELECT%20all%20messages%2C%20including%20sender%20names%2C%20where%20sender%20username%20equals%20to%20test.png)
- Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
  ```
  SELECT AVG(like_count)
  	FROM message
  	INNER JOIN member ON message.member_id = member.id
  	WHERE username = 'test';
  ```
  ![taks5-4 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task5-4%20%20Use%20SELECT%2C%20SQL%20Aggregation%20Functions%20with%20JOIN%20statement%2C%20get%20the%20average%20like%20count%20of%20messages%20where%20sender%20username%20equals%20to%20test..png)
- Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
  ```
  SELECT AVG(like_count)
  	FROM message
  	INNER JOIN member ON message.member_id = member.id
  	GROUP BY username;
  ```
  ![taks5-5 img](https://github.com/hlpss891092002/Wehelp-Stage1/blob/main/week5/screenshoot/task5-5%20Use%20SELECT%2C%20SQL%20Aggregation%20Functions%20with%20JOIN%20statement%2C%20get%20the%20average%20like%20count%20of%20messages%20GROUP%20BY%20sender%20username..png)
