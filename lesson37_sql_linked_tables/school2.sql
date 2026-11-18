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