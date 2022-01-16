-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXIST Users;

CREATE TABLE "Users" (
	"fullName"	TEXT NOT NULL,
	"Email"	TEXT NOT NULL,
	"Ciudad"	TEXT NOT NULL
);
