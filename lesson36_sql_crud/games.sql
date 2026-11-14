CREATE TABLE "games" (
	"id"	INTEGER NOT NULL,
	"title"	TEXT NOT NULL,
	"genre"	TEXT NOT NULL,
	"price"	INTEGER NOT NULL,
	"release_year"	INTEGER NOT NULL,
	"rating"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)

INSERT INTO games (title, genre, price, release_year, rating)
VALUES
    ('GTA V', 'Экшен', 2500, 2013, 9),
    ('Cyberpunk 2077', 'RPG', 3500, 2020, 8),
    ('Minecraft', 'Песочница', 1800, 2011, 10),
    ('Red Dead Redemption 2', 'Экшен', 3200, 2018, 10),
    ('The Witcher 3', 'RPG', 1500, 2015, 9),
    ('Counter-Strike 2', 'Шутер', 0, 2023, 8),
    ('Hogwarts Legacy', 'RPG', 4200, 2023, 8),
    ('Far Cry 5', 'Экшен', 2200, 2018, 7),
    ('Battlefield 2042', 'Шутер', 5500, 2021, 4),
    ('Assassins Creed Unity', 'Экшен', 1200, 2014, 6);

SELECT * FROM games

UPDATE games SET price=4000 WHERE id=1

DELETE FROM games WHERE id=1

SELECT * FROM games WHERE genre='Экшен' AND price<3000

SELECT * FROM games WHERE release_year>2020 OR rating>=9

SELECT * FROM games WHERE price>=1000 AND price<=3000
ORDER BY price DESC