BEGIN TRANSACTION;
CREATE TABLE records(id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate text);
DELETE FROM "sqlite_sequence";
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text,           phone text, website text, regdate text);
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-2222-2222','Lee.com','2022-04-10 19:48:44');
INSERT INTO "users" VALUES(4,'Cho','Cho@naver.com','010-2222-2222','Cho.com','2022-04-10 19:48:44');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@naver.com','010-2222-2222','Yoo.com','2022-04-10 19:48:44');
COMMIT;
