UPDATE dbo.TeamSeason
SET
	games = 3,
	wins = 3,
	losses = 0,
	ties = 0,
	winning_percentage = CAST((2 * 3 + 0) as float) / (2 * 3),
	points_for = 43 + 37 + 13,
	points_against = 0 + 0 + 0
WHERE team_id = 1

UPDATE dbo.TeamSeason
SET
	games = 3,
	wins = 3,
	losses = 0,
	ties = 0,
	winning_percentage = CAST((2 * 3 + 0) as float) / (2 * 3),
	points_for = 32 + 51 + 28,
	points_against = 6 + + 7
WHERE team_id = 2

UPDATE dbo.TeamSeason
SET
	games = 3,
	wins = 3,
	losses = 0,
	ties = 0,
	winning_percentage = CAST((2 * 3 + 0) as float) / (2 * 3),
	points_for = 48 + 42 + 7,
	points_against = 0 + 0 + 0
WHERE team_id = 3

UPDATE dbo.TeamSeason
SET
	games = 2,
	wins = 1,
	losses = 0,
	ties = 1,
	winning_percentage = CAST((2 * 1 + 1) as float) / (2 * 2),
	points_for = 0 + 33,
	points_against = 0 + 3
WHERE team_id = 4

UPDATE dbo.TeamSeason
SET
	games = 2,
	wins = 1,
	losses = 0,
	ties = 1,
	winning_percentage = CAST((2 * 1 + 1) as float) / (2 * 2),
	points_for = 0 + 12,
	points_against = 0 + 0
WHERE team_id = 5

UPDATE dbo.TeamSeason
SET
	games = 2,
	wins = 0,
	losses = 1,
	ties = 1,
	winning_percentage = CAST((2 * 0 + 1) as float) / (2 * 2),
	points_for = 0 + 0,
	points_against = 0 + 7
WHERE team_id = 6

UPDATE dbo.TeamSeason
SET
	games = 3,
	wins = 0,
	losses = 3,
	ties = 0,
	winning_percentage = CAST((2 * 0 + 0) as float) / (2 * 3),
	points_for = 0 + 0 + 0,
	points_against = 14 + 37 + 14
WHERE team_id = 7

UPDATE dbo.TeamSeason
SET
	games = 3,
	wins = 2,
	losses = 0,
	ties = 1,
	winning_percentage = CAST((2 * 2 + 1) as float) / (2 * 3),
	points_for = 14 + 0 + 44,
	points_against = 0 + 0 + 0
WHERE team_id = 8

UPDATE dbo.TeamSeason
SET
	games = 3,
	wins = 3,
	losses = 0,
	ties = 0,
	winning_percentage = CAST((2 * 3 + 0) as float) / (2 * 3),
	points_for = 20 + 25 + 7,
	points_against = 0 + 7 + 0
WHERE team_id = 9

UPDATE dbo.TeamSeason
SET
	games = 2,
	wins = 1,
	losses = 1,
	ties = 0,
	winning_percentage = CAST((2 * 1 + 0) as float) / (2 * 2),
	points_for = 40 + 0,
	points_against = 14 + 12
WHERE team_id = 10

UPDATE dbo.TeamSeason
SET
	games = 2,
	wins = 0,
	losses = 2,
	ties = 0,
	winning_percentage = CAST((2 * 0 + 0) as float) / (2 * 2),
	points_for = 0 + 0,
	points_against = 26 + 44
WHERE team_id = 11

UPDATE dbo.TeamSeason
SET
	games = 1,
	wins = 0,
	losses = 1,
	ties = 0,
	winning_percentage = CAST((2 * 0 + 0) as float) / (2 * 1),
	points_for = 0,
	points_against = 45
WHERE team_id = 12

UPDATE dbo.TeamSeason
SET
	games = 3,
	wins = 2,
	losses = 0,
	ties = 1,
	winning_percentage = CAST((2 * 2 + 1) as float) / (2 * 3),
	points_for = 10 + 66 + 0,
	points_against = 0 + 0 + 0
WHERE team_id = 13

UPDATE dbo.TeamSeason
SET
	games = 4,
	wins = 3,
	losses = 1,
	ties = 0,
	winning_percentage = CAST((2 * 3 + 0) as float) / (2 * 4),
	points_for = 48 + 45 + 26 + 0,
	points_against = 0 + 0 + 0 + 7
WHERE team_id = 14

SELECT
	team.name as team,
	season.year as season,
	league.short_name as league,
	games,
	wins,
	losses,
	ties,
	winning_percentage,
	points_for,
	points_against
FROM dbo.TeamSeason AS team_season
	INNER JOIN dbo.Team as team
		ON team_season.team_id = team.id
	INNER JOIN dbo.Season as season
		ON team_season.season_id = season.id
	INNER JOIN dbo.League as league
		ON team_season.league_id = league.id
WHERE season_id = 1
ORDER BY
	winning_percentage DESC,
	wins DESC,
	losses ASC,
	team.name ASC
