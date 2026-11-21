CREATE TABLE "teachers" (
	"id"	INTEGER NOT NULL,
	"full_name"	TEXT NOT NULL,
	"birth_date"	TEXT NOT NULL,
	"experience"	INTEGER NOT NULL,
	"phone_number"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)

CREATE TABLE "subjects" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"teacher_id"	INTEGER NOT NULL,
	"hours_per_week"	INTEGER NOT NULL,
	"is_mandatory"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("teacher_id") REFERENCES "teachers"("id") ON DELETE RESTRICT
)

SELECT * FROM subjects AS s
JOIN teachers AS t
ON s.teacher_id = t.id


SELECT * FROM subjects WHERE hours_per_week = (SELECT DISTINCT(hours_per_week) FROM subjects ORDER BY hours_per_week DESC  LIMIT 1 OFFSET 1)

SELECT * FROM subjects WHERE hours_per_week IN (SELECT DISTINCT(hours_per_week) FROM subjects ORDER BY hours_per_week DESC LIMIT 3) AND is_mandatory=1

SELECT 
s.id, 
s.name AS subject_name, 
t.full_name AS teacher_name, 
t.experience AS teacher_experience, 
s.hours_per_week, 
s.is_mandatory 
FROM subjects AS s
JOIN teachers AS t ON s.teacher_id=t.id
WHERE s.hours_per_week<=3 AND s.is_mandatory=0 AND t.experience<=10
ORDER BY t.experience ASC
