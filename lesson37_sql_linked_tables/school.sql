CREATE TABLE "subjects" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"teacher_name"	TEXT NOT NULL,
	"hours_per_week"	INTEGER NOT NULL,
	"is_mandatory"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)

UPDATE subjects SET is_mandatory=1 WHERE id=26

DELETE FROM subjects WHERE id=23

SELECT * FROM subjects 

SELECT SUM(hours_per_week) FROM subjects 
WHERE is_mandatory=1

SELECT MAX(hours_per_week) FROM subjects

SELECT * FROM subjects WHERE hours_per_week BETWEEN 2  AND 4
AND is_mandatory=1
ORDER BY hours_per_week DESC


SELECT MAX(hours_per_week) FROM subjects

SELECT * FROM subjects WHERE hours_per_week=5

SELECT * FROM subjects 
WHERE 
hours_per_week=(SELECT MAX(hours_per_week) FROM subjects)

SELECT * FROM subjects 
