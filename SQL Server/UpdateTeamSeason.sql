UPDATE dbo.TeamSeason
SET
	games = 3,
	wins = 3,
	losses = 0,
	ties = 0,
	winning_percentage = CAST((2 * 3 + 0) as float) / (2 * 3),
	points_for = 43 + 37 + 13,
	points_against = 0 + 0 + 0
WHERE team_name = 'Akron Pros'

UPDATE dbo.TeamSeason
SET
	games = 3,
	wins = 3,
	losses = 0,
	ties = 0,
	winning_percentage = CAST((2 * 3 + 0) as float) / (2 * 3),
	points_for = 32 + 51 + 28,
	points_against = 6 + + 7
WHERE team_name = 'Buffalo All-Americans'

UPDATE dbo.TeamSeason
SET
	games = 3,
	wins = 3,
	losses = 0,
	ties = 0,
	winning_percentage = CAST((2 * 3 + 0) as float) / (2 * 3),
	points_for = 48 + 42 + 7,
	points_against = 0 + 0 + 0
WHERE team_name = 'Canton Bulldogs'

UPDATE dbo.TeamSeason
SET
	games = 2,
	wins = 1,
	losses = 0,
	ties = 1,
	winning_percentage = CAST((2 * 1 + 1) as float) / (2 * 2),
	points_for = 0 + 33,
	points_against = 0 + 3
WHERE team_name = 'Chicago Cardinals'

UPDATE dbo.TeamSeason
SET
	games = 2,
	wins = 1,
	losses = 0,
	ties = 1,
	winning_percentage = CAST((2 * 1 + 1) as float) / (2 * 2),
	points_for = 0 + 12,
	points_against = 0 + 0
WHERE team_name = 'Chicago Tigers'

UPDATE dbo.TeamSeason
SET
	games = 2,
	wins = 0,
	losses = 1,
	ties = 1,
	winning_percentage = CAST((2 * 0 + 1) as float) / (2 * 2),
	points_for = 0 + 0,
	points_against = 0 + 7
WHERE team_name = 'Cleveland Tigers'

UPDATE dbo.TeamSeason
SET
	games = 3,
	wins = 0,
	losses = 3,
	ties = 0,
	winning_percentage = CAST((2 * 0 + 0) as float) / (2 * 3),
	points_for = 0 + 0 + 0,
	points_against = 14 + 37 + 14
WHERE team_name = 'Columbus Panhandles'

UPDATE dbo.TeamSeason
SET
	games = 3,
	wins = 2,
	losses = 0,
	ties = 1,
	winning_percentage = CAST((2 * 2 + 1) as float) / (2 * 3),
	points_for = 14 + 0 + 44,
	points_against = 0 + 0 + 0
WHERE team_name = 'Dayton Triangles'

UPDATE dbo.TeamSeason
SET
	games = 3,
	wins = 3,
	losses = 0,
	ties = 0,
	winning_percentage = CAST((2 * 3 + 0) as float) / (2 * 3),
	points_for = 20 + 25 + 7,
	points_against = 0 + 7 + 0
WHERE team_name = 'Decatur Staleys'

UPDATE dbo.TeamSeason
SET
	games = 2,
	wins = 1,
	losses = 1,
	ties = 0,
	winning_percentage = CAST((2 * 1 + 0) as float) / (2 * 2),
	points_for = 40 + 0,
	points_against = 14 + 12
WHERE team_name = 'Detroit Heralds'

UPDATE dbo.TeamSeason
SET
	games = 2,
	wins = 0,
	losses = 2,
	ties = 0,
	winning_percentage = CAST((2 * 0 + 0) as float) / (2 * 2),
	points_for = 0 + 0,
	points_against = 26 + 44
WHERE team_name = 'Hammond Pros'

UPDATE dbo.TeamSeason
SET
	games = 1,
	wins = 0,
	losses = 1,
	ties = 0,
	winning_percentage = CAST((2 * 0 + 0) as float) / (2 * 1),
	points_for = 0,
	points_against = 45
WHERE team_name = 'Muncie Flyers'

UPDATE dbo.TeamSeason
SET
	games = 3,
	wins = 2,
	losses = 0,
	ties = 1,
	winning_percentage = CAST((2 * 2 + 1) as float) / (2 * 3),
	points_for = 10 + 66 + 0,
	points_against = 0 + 0 + 0
WHERE team_name = 'Rochester Jeffersons'

UPDATE dbo.TeamSeason
SET
	games = 4,
	wins = 3,
	losses = 1,
	ties = 0,
	winning_percentage = CAST((2 * 3 + 0) as float) / (2 * 4),
	points_for = 48 + 45 + 26 + 0,
	points_against = 0 + 0 + 0 + 7
WHERE team_name = 'Rock Island Independents'

SELECT * FROM dbo.TeamSeason WHERE season_year = 1920
