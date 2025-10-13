SET QUOTED_IDENTIFIER OFF;
GO
USE ProFootballDb
GO
IF SCHEMA_ID(N'dbo') IS NULL EXECUTE(N'CREATE SCHEMA dbo');
GO

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 1,
		'St. Paul Ideals', 0, 'Rock Island Independents', 48,
		'Rock Island Independents', 48, 'St. Paul Ideals', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 2,
		'Wheeling Stogies', 0, 'Akron Pros', 43,
		'Akron Pros', 43, 'Wheeling Stogies', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 2,
		'Muncie Flyers', 0, 'Rock Island Independents', 45,
		'Rock Island Independents', 45, 'Muncie Flyers', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 2,
		'Columbus Panhandles', 0, 'Dayton Triangles', 14,
		'Dayton Triangles', 14, 'Columbus Panhandles', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 2,
		'Moline Universal Tractors', 0, 'Decatur Staleys', 20,
		'Decatur Staleys', 20, 'Moline Universal Tractors', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 2,
		'All Buffalo', 0, 'Rochester Jeffersons', 10,
		'Rochester Jeffersons', 10, 'All Buffalo', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 2,
		'Pitcairn Quakers', 0, 'Canton Bulldogs', 48,
		'Canton Bulldogs', 48, 'Pitcairn Quakers', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 2,
		'West Buffalo', 6, 'Buffalo All-Americans', 32,
		'Buffalo All-Americans', 32, 'West Buffalo', 6,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 3,
		'Hammond Pros', 0, 'Rock Island Independents', 26,
		'Rock Island Independents', 26, 'Hammond Pros', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 3,
		'Fort Porter', 0, 'Rochester Jeffersons', 66,
		'Rochester Jeffersons', 66, 'Fort Porter', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	is_playoff, notes
)
	VALUES (
		1, 3,
		'Cleveland Tigers', 0, 'Dayton Triangles', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 3,
		'Cleveland Panthers', 14, 'Detroit Heralds', 40,
		'Detroit Heralds', 40, 'Cleveland Panthers', 14,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	is_playoff, notes
)
	VALUES (
		1, 3,
		'Chicago Tigers', 0, 'Chicago Cardinals', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 3,
		'All Buffalo', 0, 'Buffalo All-Americans', 51,
		'Buffalo All-Americans', 51, 'All Buffalo', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 3,
		'Kewanee Walworths', 7, 'Decatur Staleys', 25,
		'Decatur Staleys', 25, 'Kewanee Walworths', 7,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 3,
		'Toledo Maroons', 0, 'Canton Bulldogs', 42,
		'Canton Bulldogs', 42, 'Toledo Maroons', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 3,
		'Columbus Panhandles', 0, 'Akron Pros', 37,
		'Akron Pros', 37, 'Columbus Panhandles', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 4,
		'Moline Universal Tractors', 3, 'Chicago Cardinals', 33,
		'Chicago Cardinals', 33, 'Moline Universal Tractors', 3,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 4,
		'Detroit Heralds', 0, 'Chicago Tigers', 12,
		'Chicago Tigers', 12, 'Detroit Heralds', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 4,
		'McKeesport Olympics', 7, 'Buffalo All-Americans', 28,
		'Buffalo All-Americans', 28, 'McKeesport Olympics', 7,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 4,
		'Hammond Pros', 0, 'Dayton Triangles', 44,
		'Dayton Triangles', 44, 'Hammond Pros', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 4,
		'Cincinnati Celts', 0, 'Akron Pros', 13,
		'Akron Pros', 13, 'Cincinnati Celts', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 4,
		'Columbus Panhandles', 0, 'Fort Wayne Friars', 14,
		'Fort Wayne Friars', 14, 'Columbus Panhandles', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	is_playoff, notes
)
	VALUES (
		1, 4,
		'Utica K. of C.', 0, 'Rochester Jeffersons', 0,
		0, ''
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 4,
		'Decatur Staleys', 7, 'Rock Island Independents', 0,
		'Decatur Staleys', 7, 'Rock Island Independents', 0,
		0, 'First American pro football game ever won by the visiting team'
	)

INSERT INTO dbo.Game (
	season_id, week,
	guest_name, guest_score, host_name, host_score,
	winner_name, winner_score, loser_name, loser_score,
	is_playoff, notes
)
	VALUES (
		1, 4,
		'Cleveland Tigers', 0, 'Canton Bulldogs', 7,
		'Canton Bulldogs', 7, 'Cleveland Tigers', 0,
		0, ''
	)

SELECT * FROM dbo.Game
