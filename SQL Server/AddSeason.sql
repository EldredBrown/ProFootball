-- --------------------------------------------------
-- Entity Designer DDL Script for SQL Server 2005, 2008, 2012 and Azure
-- --------------------------------------------------
-- Date Created: 02/06/1985 17:18:59
-- Generated from EDMX file: D:\Documents\BitBucket\CST 4X2 - SeniorProject\FootballApplication\FootballApplicationWeb\Models\FootballDataModel.edmx
-- --------------------------------------------------

SET QUOTED_IDENTIFIER OFF;
GO
USE ProFootballDb
GO
IF SCHEMA_ID(N'dbo') IS NULL EXECUTE(N'CREATE SCHEMA dbo');
GO

-- --------------------------------------------------
-- Populating all tables
-- --------------------------------------------------

-- Populating table 'Season'
INSERT INTO dbo.Season VALUES (1985)

-- Populating table 'League'
INSERT INTO dbo.League VALUES ('NFL', 'National Football League', 1923, NULL)
INSERT INTO dbo.League VALUES ('AFL', 'American Football League', 1960, 1969)

-- Populating table 'Conference'
INSERT INTO dbo.Conference VALUES ('AFC', 'American Football Conference', 'NFL', 1970, NULL)
INSERT INTO dbo.Conference VALUES ('NFC', 'National Football Conference', 'NFL', 1970, NULL)

-- Populating table 'Division'
INSERT INTO dbo.Division VALUES ('AFC Central', 'NFL', 'AFC', 1970, NULL)
INSERT INTO dbo.Division VALUES ('NFC Central', 'NFL', 'NFC', 1970, NULL)

-- Populating table 'Team'
INSERT INTO dbo.Team VALUES ('Houston Oilers')
INSERT INTO dbo.Team VALUES ('Los Angeles Raiders')
INSERT INTO dbo.Team VALUES ('San Diego Chargers')
INSERT INTO dbo.Team VALUES ('St. Louis Cardinals')

-- Populating table 'LeagueSeason'
INSERT INTO dbo.LeagueSeason (league_name, season_year) VALUES ('NFL', 1985)

-- Populating table 'TeamSeason'
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Buffalo Bills', 1985, 'NFL', 'AFC', 'AFC East')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Indianapolis Colts', 1985, 'NFL', 'AFC', 'AFC East')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Miami Dolphins', 1985, 'NFL', 'AFC', 'AFC East')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('New England Patriots', 1985, 'NFL', 'AFC', 'AFC East')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('New York Jets', 1985, 'NFL', 'AFC', 'AFC East')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Cincinnati Bengals', 1985, 'NFL', 'AFC', 'AFC Central')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Cleveland Browns', 1985, 'NFL', 'AFC', 'AFC Central')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Houston Oilers', 1985, 'NFL', 'AFC', 'AFC Central')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Pittsburgh Steelers', 1985, 'NFL', 'AFC', 'AFC Central')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Denver Broncos', 1985, 'NFL', 'AFC', 'AFC West')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Kansas City Chiefs', 1985, 'NFL', 'AFC', 'AFC West')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Los Angeles Raiders', 1985, 'NFL', 'AFC', 'AFC West')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('San Diego Chargers', 1985, 'NFL', 'AFC', 'AFC West')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Seattle Seahawks', 1985, 'NFL', 'NFC', 'AFC West')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Dallas Cowboys', 1985, 'NFL', 'NFC', 'NFC East')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('New York Giants', 1985, 'NFL', 'NFC', 'NFC East')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Philadelphia Eagles', 1985, 'NFL', 'NFC', 'NFC East')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('St. Louis Cardinals', 1985, 'NFL', 'NFC', 'NFC East')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Washington Redskins', 1985, 'NFL', 'NFC', 'NFC East')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Chicago Bears', 1985, 'NFL', 'NFC', 'NFC Central')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Detroit Lions', 1985, 'NFL', 'NFC', 'NFC Central')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Green Bay Packers', 1985, 'NFL', 'NFC', 'NFC Central')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Minnesota Vikings', 1985, 'NFL', 'NFC', 'NFC Central')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Tampa Bay Buccaneers', 1985, 'NFL', 'NFC', 'NFC Central')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Atlanta Falcons', 1985, 'NFL', 'NFC', 'NFC West')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('Los Angeles Rams', 1985, 'NFL', 'NFC', 'NFC West')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('New Orleans Saints', 1985, 'NFL', 'NFC', 'NFC West')
INSERT INTO dbo.TeamSeason (team_name, season_year, league_name, conference_name, division_name)
	VALUES ('San Francisco 49ers', 1985, 'NFL', 'NFC', 'NFC West')

INSERT INTO dbo.WeekCount VALUES (1985, 1)

-- --------------------------------------------------
-- Verifying all tables
-- --------------------------------------------------

SELECT * FROM dbo.Season ORDER BY year DESC
SELECT * FROM dbo.League ORDER BY short_name ASC
SELECT * FROM dbo.Conference ORDER BY short_name ASC
SELECT * FROM dbo.Division ORDER BY name ASC
SELECT * FROM dbo.Team ORDER BY name ASC
SELECT * FROM dbo.LeagueSeason ORDER BY league_name ASC, season_year DESC
SELECT * FROM dbo.TeamSeason ORDER BY team_name ASC, season_year DESC
SELECT * FROM dbo.Game ORDER BY season_year DESC
SELECT * FROM dbo.WeekCount

-- --------------------------------------------------
-- Script has ended
-- --------------------------------------------------
