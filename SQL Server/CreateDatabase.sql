-- --------------------------------------------------
-- Entity Designer DDL Script for SQL Server 2005, 2008, 2012 and Azure
-- --------------------------------------------------
-- Date Created: 02/06/2018 17:18:59
-- Generated from EDMX file: D:\Documents\BitBucket\CST 4X2 - SeniorProject\FootballApplication\FootballApplicationWeb\Models\FootballDataModel.edmx
-- --------------------------------------------------

SET QUOTED_IDENTIFIER OFF;
GO
USE ProFootballDb;
GO
IF SCHEMA_ID(N'dbo') IS NULL EXECUTE(N'CREATE SCHEMA dbo');
GO

-- --------------------------------------------------
-- Dropping existing FOREIGN KEY constraints
-- --------------------------------------------------

IF OBJECT_ID(N'dbo.FK_TeamSeason_Division_DivisionId', 'F') IS NOT NULL
    ALTER TABLE dbo.TeamSeason DROP CONSTRAINT FK_TeamSeason_Division_DivisionId;
GO
IF OBJECT_ID(N'dbo.FK_TeamSeason_Conference_ConferenceId', 'F') IS NOT NULL
    ALTER TABLE dbo.TeamSeason DROP CONSTRAINT FK_TeamSeason_Conference_ConferenceId;
GO
IF OBJECT_ID(N'dbo.FK_TeamSeason_League_LeagueId', 'F') IS NOT NULL
    ALTER TABLE dbo.TeamSeason DROP CONSTRAINT FK_TeamSeason_League_LeagueId;
GO
IF OBJECT_ID(N'dbo.FK_TeamSeason_Season_SeasonId', 'F') IS NOT NULL
    ALTER TABLE dbo.TeamSeason DROP CONSTRAINT FK_TeamSeason_Season_SeasonId;
GO
IF OBJECT_ID(N'dbo.FK_TeamSeason_Team_TeamId', 'F') IS NOT NULL
    ALTER TABLE dbo.TeamSeason DROP CONSTRAINT FK_TeamSeason_Team_TeamId;
GO
IF OBJECT_ID(N'dbo.FK_LeagueSeason_Season_SeasonId', 'F') IS NOT NULL
    ALTER TABLE dbo.LeagueSeason DROP CONSTRAINT FK_LeagueSeason_Season_SeasonId;
GO
IF OBJECT_ID(N'dbo.FK_LeagueSeason_League_LeagueId', 'F') IS NOT NULL
    ALTER TABLE dbo.LeagueSeason DROP CONSTRAINT FK_LeagueSeason_League_LeagueId;
GO
IF OBJECT_ID(N'dbo.FK_Game_Team_LoserId', 'F') IS NOT NULL
    ALTER TABLE dbo.Game DROP CONSTRAINT FK_Game_Team_LoserId;
GO
IF OBJECT_ID(N'dbo.FK_Game_Team_WinnerId', 'F') IS NOT NULL
    ALTER TABLE dbo.Game DROP CONSTRAINT FK_Game_Team_WinnerId;
GO
IF OBJECT_ID(N'dbo.FK_Game_Team_HostId', 'F') IS NOT NULL
    ALTER TABLE dbo.Game DROP CONSTRAINT FK_Game_Team_HostId;
GO
IF OBJECT_ID(N'dbo.FK_Game_Team_GuestId', 'F') IS NOT NULL
    ALTER TABLE dbo.Game DROP CONSTRAINT FK_Game_Team_GuestId;
GO
IF OBJECT_ID(N'dbo.FK_Game_Season_SeasonId', 'F') IS NOT NULL
    ALTER TABLE dbo.Game DROP CONSTRAINT FK_Game_Season_SeasonId;
GO
IF OBJECT_ID(N'dbo.FK_Division_Season_LastSeasonId', 'F') IS NOT NULL
    ALTER TABLE dbo.Division DROP CONSTRAINT FK_Division_Season_LastSeasonId;
GO
IF OBJECT_ID(N'dbo.FK_Division_Season_FirstSeasonId', 'F') IS NOT NULL
    ALTER TABLE dbo.Division DROP CONSTRAINT FK_Division_Season_FirstSeasonId;
GO
IF OBJECT_ID(N'dbo.FK_Division_Conference_ConferenceId', 'F') IS NOT NULL
    ALTER TABLE dbo.Division DROP CONSTRAINT FK_Division_Conference_ConferenceId;
GO
IF OBJECT_ID(N'dbo.FK_Division_League_LeagueId', 'F') IS NOT NULL
    ALTER TABLE dbo.Division DROP CONSTRAINT FK_Division_League_LeagueId;
GO
IF OBJECT_ID(N'dbo.FK_Conference_Season_LastSeasonId', 'F') IS NOT NULL
    ALTER TABLE dbo.Conference DROP CONSTRAINT FK_Conference_Season_LastSeasonId;
GO
IF OBJECT_ID(N'dbo.FK_Conference_Season_FirstSeasonId', 'F') IS NOT NULL
    ALTER TABLE dbo.Conference DROP CONSTRAINT FK_Conference_Season_FirstSeasonId;
GO
IF OBJECT_ID(N'dbo.FK_Conference_League_LeagueId', 'F') IS NOT NULL
    ALTER TABLE dbo.Conference DROP CONSTRAINT FK_Conference_League_LeagueId;
GO
IF OBJECT_ID(N'dbo.FK_League_Season_LastSeasonId', 'F') IS NOT NULL
    ALTER TABLE dbo.League DROP CONSTRAINT FK_League_Season_LastSeasonId;
GO
IF OBJECT_ID(N'dbo.FK_League_Season_FirstSeasonId', 'F') IS NOT NULL
    ALTER TABLE dbo.League DROP CONSTRAINT FK_League_Season_FirstSeasonId;
GO

-- --------------------------------------------------
-- Dropping existing tables
-- --------------------------------------------------

IF OBJECT_ID(N'dbo.TeamSeason', 'U') IS NOT NULL
    DROP TABLE dbo.TeamSeason;
GO
IF OBJECT_ID(N'dbo.LeagueSeason', 'U') IS NOT NULL
    DROP TABLE dbo.LeagueSeason;
GO
IF OBJECT_ID(N'dbo.Game', 'U') IS NOT NULL
    DROP TABLE dbo.Game;
GO
IF OBJECT_ID(N'dbo.Team', 'U') IS NOT NULL
    DROP TABLE dbo.Team;
GO
IF OBJECT_ID(N'dbo.Division', 'U') IS NOT NULL
    DROP TABLE dbo.Division;
GO
IF OBJECT_ID(N'dbo.Conference', 'U') IS NOT NULL
    DROP TABLE dbo.Conference;
GO
IF OBJECT_ID(N'dbo.League', 'U') IS NOT NULL
    DROP TABLE dbo.League;
GO
IF OBJECT_ID(N'dbo.Season', 'U') IS NOT NULL
    DROP TABLE dbo.Season;
GO

-- --------------------------------------------------
-- Creating all tables
-- --------------------------------------------------

-- Creating table 'Season'
CREATE TABLE dbo.Season (
    id int IDENTITY(1,1) NOT NULL,
    year smallint NOT NULL,
    num_of_weeks_scheduled tinyint NOT NULL DEFAULT 0,
    num_of_weeks_completed tinyint NOT NULL DEFAULT 0,
);
GO

-- Creating table 'League'
CREATE TABLE dbo.League (
    id int IDENTITY(1,1) NOT NULL,
	short_name varchar(5) NOT NULL,
	long_name varchar(50) NOT NULL,
	first_season_id int NOT NULL,
	last_season_id int NULL,
);
GO

-- Creating table 'Conference'
CREATE TABLE dbo.Conference (
    id int IDENTITY(1,1) NOT NULL,
    short_name varchar(5) NOT NULL,
    long_name varchar(50) NOT NULL,
    league_id int NOT NULL,
	first_season_id int NOT NULL,
	last_season_id int NULL,
);
GO

-- Creating table 'Division'
CREATE TABLE dbo.Division (
    id int IDENTITY(1,1) NOT NULL,
    name varchar(50) NOT NULL,
    league_id int NOT NULL,
    conference_id int NOT NULL,
	first_season_id int NOT NULL,
	last_season_id int NULL,
);
GO

-- Creating table 'Team'
CREATE TABLE dbo.Team (
    id int IDENTITY(1,1) NOT NULL,
    name varchar(50) NOT NULL
);
GO

-- Creating table 'Game'
CREATE TABLE dbo.Game (
    id int IDENTITY(1,1) NOT NULL,
    season_id int NOT NULL,
    week tinyint NOT NULL,
    guest_name varchar(50) NOT NULL,
    guest_score tinyint NOT NULL DEFAULT 0,
    host_name varchar(50) NOT NULL,
    host_score tinyint NOT NULL DEFAULT 0,
    winner_name varchar(50),
    winner_score tinyint,
    loser_name varchar(50),
    loser_score tinyint,
    is_playoff bit NOT NULL DEFAULT 0,
    notes varchar(256),
);
GO

-- Creating table 'LeagueSeason'
CREATE TABLE dbo.LeagueSeason (
    id int IDENTITY(1,1) NOT NULL,
    league_id int NOT NULL,
    season_id int NOT NULL,
    total_games smallint NOT NULL DEFAULT 0,
    total_points smallint NOT NULL DEFAULT 0,
    average_points float,
);
GO

-- Creating table 'TeamSeason'
CREATE TABLE dbo.TeamSeason (
    id int IDENTITY(1,1) NOT NULL,
    team_id int NOT NULL,
    season_id int NOT NULL,
    league_id int NOT NULL,
    conference_id int,
    division_id int,
    games tinyint NOT NULL DEFAULT 0,
    wins tinyint NOT NULL DEFAULT 0,
    losses tinyint NOT NULL DEFAULT 0,
    ties tinyint NOT NULL DEFAULT 0,
    winning_percentage float,
    points_for smallint NOT NULL DEFAULT 0,
    points_against smallint NOT NULL DEFAULT 0,
    expected_wins float NOT NULL DEFAULT 0,
    expected_losses float NOT NULL DEFAULT 0,
    offensive_average float,
    offensive_factor float,
    offensive_index float,
    defensive_average float,
    defensive_factor float,
    defensive_index float,
    final_expected_winning_percentage float,
);
GO

-- --------------------------------------------------
-- Creating all PRIMARY KEY constraints
-- --------------------------------------------------

-- Creating primary key on id in table 'Season'
ALTER TABLE dbo.Season
ADD CONSTRAINT PK_Season
    PRIMARY KEY CLUSTERED (id ASC);
GO

-- Creating primary key on id in table 'League'
ALTER TABLE dbo.League
ADD CONSTRAINT PK_League
    PRIMARY KEY CLUSTERED (id ASC);
GO

-- Creating primary key on id in table 'Conference'
ALTER TABLE dbo.Conference
ADD CONSTRAINT PK_Conference
    PRIMARY KEY CLUSTERED (id ASC);
GO

-- Creating primary key on id in table 'Division'
ALTER TABLE dbo.Division
ADD CONSTRAINT PK_Division
    PRIMARY KEY CLUSTERED (id ASC);
GO

-- Creating primary key on id in table 'Team'
ALTER TABLE dbo.Team
ADD CONSTRAINT PK_Team
    PRIMARY KEY CLUSTERED (id ASC);
GO

-- Creating primary key on id in table 'Game'
ALTER TABLE dbo.Game
ADD CONSTRAINT PK_Game
    PRIMARY KEY CLUSTERED (id ASC);
GO

-- Creating primary key on id in table 'LeagueSeason'
ALTER TABLE dbo.LeagueSeason
ADD CONSTRAINT PK_LeagueSeason
    PRIMARY KEY CLUSTERED (id ASC);
GO

-- Creating primary key on id in table 'TeamSeason'
ALTER TABLE dbo.TeamSeason
ADD CONSTRAINT PK_TeamSeason
    PRIMARY KEY CLUSTERED (id ASC);
GO

-- --------------------------------------------------
-- Creating all UNIQUE constraints
-- --------------------------------------------------

-- Creating unique key on year in table 'Season'
ALTER TABLE dbo.Season
ADD CONSTRAINT UK_Season_Year
    UNIQUE (year);
GO

-- Creating unique key on short_name in table 'League'
ALTER TABLE dbo.League
ADD CONSTRAINT UK_League_ShortName
    UNIQUE (short_name);
GO

-- Creating unique key on long_name in table 'League'
ALTER TABLE dbo.League
ADD CONSTRAINT UK_League_LongName
    UNIQUE (long_name);
GO

-- Creating unique key on short_name in table 'Conference'
ALTER TABLE dbo.Conference
ADD CONSTRAINT UK_Conference_ShortName
    UNIQUE (short_name);
GO

-- Creating unique key on long_name in table 'Conference'
ALTER TABLE dbo.Conference
ADD CONSTRAINT UK_Conference_LongName
    UNIQUE (long_name);
GO

-- Creating unique key on name in table 'Division'
ALTER TABLE dbo.Division
ADD CONSTRAINT UK_Division_Name
    UNIQUE (name);
GO

-- Creating unique key on name in table 'Team'
ALTER TABLE dbo.Team
ADD CONSTRAINT UK_Team_Name
    UNIQUE (name);
GO

-- Creating unique key on league_id, season_id in table 'LeagueSeason'
ALTER TABLE dbo.LeagueSeason
ADD CONSTRAINT UK_LeagueSeason_LeagueId_SeasonId
    UNIQUE (league_id, season_id);
GO

-- Creating unique key on team_id, season_id in table 'TeamSeason'
ALTER TABLE dbo.TeamSeason
ADD CONSTRAINT UK_TeamSeason_LeagueId_SeasonId
    UNIQUE (team_id, season_id);
GO

---- --------------------------------------------------
---- Creating all FOREIGN KEY constraints
---- --------------------------------------------------

-- Creating foreign key on first_season_id in table 'League'
ALTER TABLE dbo.League
ADD CONSTRAINT FK_League_Season_FirstSeasonId
    FOREIGN KEY (first_season_id)
    REFERENCES dbo.Season
        (id)
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_League_Season_FirstSeasonId'
CREATE INDEX IX_FK_League_Season_FirstSeasonId
ON dbo.League
    (first_season_id);
GO

-- Creating foreign key on last_season_id in table 'League'
ALTER TABLE dbo.League
ADD CONSTRAINT FK_League_Season_LastSeasonId
    FOREIGN KEY (last_season_id)
    REFERENCES dbo.Season
        (id)
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_League_Season_LastSeasonId'
CREATE INDEX IX_FK_League_Season_LastSeasonId
ON dbo.League
    (last_season_id);
GO

-- Creating foreign key on league_id in table 'Conference'
ALTER TABLE dbo.Conference
ADD CONSTRAINT FK_Conference_League_LeagueId
    FOREIGN KEY (league_id)
    REFERENCES dbo.League
        (id)
    ON DELETE CASCADE ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_Conference_League_LeagueId'
CREATE INDEX IX_FK_Conference_League_LeagueId
ON dbo.Conference
    (league_id);
GO

-- Creating foreign key on first_season_id in table 'Conference'
ALTER TABLE dbo.Conference
ADD CONSTRAINT FK_Conference_Season_FirstSeasonId
    FOREIGN KEY (first_season_id)
    REFERENCES dbo.Season
        (id)
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_Conference_Season_FirstSeasonId'
CREATE INDEX IX_FK_Conference_Season_FirstSeasonId
ON dbo.Conference
    (first_season_id);
GO

-- Creating foreign key on last_season_id in table 'Conference'
ALTER TABLE dbo.Conference
ADD CONSTRAINT FK_Conference_Season_LastSeasonId
    FOREIGN KEY (last_season_id)
    REFERENCES dbo.Season
        (id)
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_Conference_Season_LastSeasonId'
CREATE INDEX IX_FK_Conference_Season_LastSeasonId
ON dbo.Conference
    (last_season_id);
GO

-- Creating foreign key on league_id in table 'Division'
ALTER TABLE dbo.Division
ADD CONSTRAINT FK_Division_League_LeagueId
    FOREIGN KEY (league_id)
    REFERENCES dbo.League
        (id)
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_Division_League_LeagueId'
CREATE INDEX IX_FK_Division_League_LeagueId
ON dbo.Division
    (league_id);
GO

-- Creating foreign key on conference_id in table 'Division'
ALTER TABLE dbo.Division
ADD CONSTRAINT FK_Division_Conference_ConferenceId
    FOREIGN KEY (conference_id)
    REFERENCES dbo.Conference
        (id)
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_Division_Conference_ConferenceId'
CREATE INDEX IX_FK_Division_Conference_ConferenceId
ON dbo.Division
    (conference_id);
GO

-- Creating foreign key on first_season_id in table 'Division'
ALTER TABLE dbo.Division
ADD CONSTRAINT FK_Division_Season_FirstSeasonId
    FOREIGN KEY (first_season_id)
    REFERENCES dbo.Season
        (id)
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_Division_Season_FirstSeasonId'
CREATE INDEX IX_FK_Division_Season_FirstSeasonId
ON dbo.Division
    (first_season_id);
GO

-- Creating foreign key on last_season_id in table 'Division'
ALTER TABLE dbo.Division
ADD CONSTRAINT FK_Division_Season_LastSeasonId
    FOREIGN KEY (last_season_id)
    REFERENCES dbo.Season
        (id)
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_Division_Season_LastSeasonId'
CREATE INDEX IX_FK_Division_Season_LastSeasonId
ON dbo.Division
    (last_season_id);
GO

-- Creating foreign key on season_id in table 'Game'
ALTER TABLE dbo.Game
ADD CONSTRAINT FK_Game_Season_SeasonId
    FOREIGN KEY (season_id)
    REFERENCES dbo.Season
        (id)
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_Game_Season_SeasonId'
CREATE INDEX IX_FK_Game_Season_SeasonId
ON dbo.Game
    (season_id);
GO

---- Creating foreign key on guest_name in table 'Game'
--ALTER TABLE dbo.Game
--ADD CONSTRAINT FK_Game_Team_GuestName
--    FOREIGN KEY (guest_name)
--    REFERENCES dbo.Team
--        (name)
--    ON DELETE NO ACTION ON UPDATE NO ACTION;
--GO

---- Creating non-clustered index for FOREIGN KEY 'FK_Game_Team_GuestName'
--CREATE INDEX IX_FK_Game_Team_GuestName
--ON dbo.Game
--    (guest_name);
--GO

---- Creating foreign key on host_name in table 'Game'
--ALTER TABLE dbo.Game
--ADD CONSTRAINT FK_Game_Team_HostName
--    FOREIGN KEY (host_name)
--    REFERENCES dbo.Team
--        (name)
--    ON DELETE NO ACTION ON UPDATE NO ACTION;
--GO

---- Creating non-clustered index for FOREIGN KEY 'FK_Game_Team_HostName'
--CREATE INDEX IX_FK_Game_Team_HostName
--ON dbo.Game
--    (host_name);
--GO

---- Creating foreign key on winner_name in table 'Game'
--ALTER TABLE dbo.Game
--ADD CONSTRAINT FK_Game_Team_WinnerName
--    FOREIGN KEY (winner_name)
--    REFERENCES dbo.Team
--        (name)
--    ON DELETE NO ACTION ON UPDATE NO ACTION;
--GO

---- Creating non-clustered index for FOREIGN KEY 'FK_Game_Team_WinnerName'
--CREATE INDEX IX_FK_Game_Team_WinnerName
--ON dbo.Game
--    (winner_name);
--GO

---- Creating foreign key on loser_name in table 'Game'
--ALTER TABLE dbo.Game
--ADD CONSTRAINT FK_Game_Team_LoserName
--    FOREIGN KEY (loser_name)
--    REFERENCES dbo.Team
--        (name)
--    ON DELETE NO ACTION ON UPDATE NO ACTION;
--GO

---- Creating non-clustered index for FOREIGN KEY 'FK_Game_Team_LoserName'
--CREATE INDEX IX_FK_Game_Team_LoserName
--ON dbo.Game
--    (loser_name);
--GO

-- Creating foreign key on league_id in table 'LeagueSeason'
ALTER TABLE dbo.LeagueSeason
ADD CONSTRAINT FK_LeagueSeason_League_LeagueId
    FOREIGN KEY (league_id)
    REFERENCES dbo.League
        (id)
    ON DELETE CASCADE ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_LeagueSeason_League_LeagueId'
CREATE INDEX IX_FK_LeagueSeason_League_LeagueId
ON dbo.LeagueSeason
    (league_id);
GO

-- Creating foreign key on season_id in table 'LeagueSeason'
ALTER TABLE dbo.LeagueSeason
ADD CONSTRAINT FK_LeagueSeason_Season_SeasonId
    FOREIGN KEY (season_id)
    REFERENCES dbo.Season
        (id)
    ON DELETE CASCADE ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_LeagueSeason_Season_SeasonId'
CREATE INDEX IX_FK_LeagueSeason_Season_SeasonId
ON dbo.LeagueSeason
    (season_id);
GO

-- Creating foreign key on team_id in table 'TeamSeason'
ALTER TABLE dbo.TeamSeason
ADD CONSTRAINT FK_TeamSeason_Team_TeamId
    FOREIGN KEY (team_id)
    REFERENCES dbo.Team
        (id)
    ON DELETE CASCADE ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_TeamSeason_Team_TeamId'
CREATE INDEX IX_FK_TeamSeason_Team_TeamId
ON dbo.TeamSeason
    (team_id);
GO

-- Creating foreign key on season_id in table 'TeamSeason'
ALTER TABLE dbo.TeamSeason
ADD CONSTRAINT FK_TeamSeason_Season_SeasonId
    FOREIGN KEY (season_id)
    REFERENCES dbo.Season
        (id)
    ON DELETE CASCADE ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_TeamSeason_Season_SeasonId'
CREATE INDEX IX_FK_TeamSeason_Season_SeasonId
ON dbo.TeamSeason
    (season_id);
GO

-- Creating foreign key on league_id in table 'TeamSeason'
ALTER TABLE dbo.TeamSeason
ADD CONSTRAINT FK_TeamSeason_League_LeagueId
    FOREIGN KEY (league_id)
    REFERENCES dbo.League
        (id)
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_TeamSeason_League_LeagueId'
CREATE INDEX IX_FK_TeamSeason_League_LeagueId
ON dbo.TeamSeason
    (league_id);
GO

-- Creating foreign key on conference_id in table 'TeamSeason'
ALTER TABLE dbo.TeamSeason
ADD CONSTRAINT FK_TeamSeason_Conference_ConferenceId
    FOREIGN KEY (conference_id)
    REFERENCES dbo.Conference
        (id)
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_TeamSeason_Conference_ConferenceId'
CREATE INDEX IX_FK_TeamSeason_Conference_ConferenceId
ON dbo.TeamSeason
    (conference_id);
GO

-- Creating foreign key on division_id in table 'TeamSeason'
ALTER TABLE dbo.TeamSeason
ADD CONSTRAINT FK_TeamSeason_Division_DivisionId
    FOREIGN KEY (division_id)
    REFERENCES dbo.Division
        (id)
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_TeamSeason_Division_DivisionId'
CREATE INDEX IX_FK_TeamSeason_Division_DivisionId
ON dbo.TeamSeason
    (division_id);
GO

-- --------------------------------------------------
-- Populating all tables
-- --------------------------------------------------

-- Populating table 'Seasons'
INSERT INTO dbo.Season (year) VALUES (1920);

-- Populating table 'Leagues'
INSERT INTO dbo.League VALUES ('APFA', 'American Professional Football Association', 1, NULL);

------ Populating table 'Conference'
----INSERT INTO dbo.Conference VALUES ('AFC', 'American Football Conference', 'NFL', 1970, NULL);
----INSERT INTO dbo.Conference VALUES ('NFC', 'National Football Conference', 'NFL', 1970, NULL);

------ Populating table 'Divisions'
----INSERT INTO dbo.Divisions VALUES ('AFC East', 'NFL', 'AFC', 1970, NULL);
----INSERT INTO dbo.Divisions VALUES ('AFC North', 'NFL', 'AFC', 2002, NULL);
----INSERT INTO dbo.Divisions VALUES ('AFC South', 'NFL', 'AFC', 2002, NULL);
----INSERT INTO dbo.Divisions VALUES ('AFC West', 'NFL', 'AFC', 1970, NULL);
----INSERT INTO dbo.Divisions VALUES ('NFC East', 'NFL', 'NFC', 1970, NULL);
----INSERT INTO dbo.Divisions VALUES ('NFC North', 'NFL', 'NFC', 2002, NULL);
----INSERT INTO dbo.Divisions VALUES ('NFC South', 'NFL', 'NFC', 2002, NULL);
----INSERT INTO dbo.Divisions VALUES ('NFC West', 'NFL', 'NFC', 1970, NULL);

-- Populating table 'Teams'
INSERT INTO dbo.Team VALUES ('Akron Pros');
INSERT INTO dbo.Team VALUES ('Buffalo All-Americans');
INSERT INTO dbo.Team VALUES ('Canton Bulldogs');
INSERT INTO dbo.Team VALUES ('Chicago Cardinals');
INSERT INTO dbo.Team VALUES ('Chicago Tigers');
INSERT INTO dbo.Team VALUES ('Cleveland Tigers');
INSERT INTO dbo.Team VALUES ('Columbus Panhandles');
INSERT INTO dbo.Team VALUES ('Dayton Triangles');
INSERT INTO dbo.Team VALUES ('Decatur Staleys');
INSERT INTO dbo.Team VALUES ('Detroit Heralds');
INSERT INTO dbo.Team VALUES ('Hammond Pros');
INSERT INTO dbo.Team VALUES ('Muncie Flyers');
INSERT INTO dbo.Team VALUES ('Rochester Jeffersons');
INSERT INTO dbo.Team VALUES ('Rock Island Independents');

-- Populating table 'LeagueSeason'
INSERT INTO dbo.LeagueSeason (league_id, season_id) VALUES (1, 1);

-- Populating table 'TeamSeason'
INSERT INTO dbo.TeamSeason (team_id, season_id, league_id) VALUES (1, 1, 1);
INSERT INTO dbo.TeamSeason (team_id, season_id, league_id) VALUES (2, 1, 1);
INSERT INTO dbo.TeamSeason (team_id, season_id, league_id) VALUES (3, 1, 1);
INSERT INTO dbo.TeamSeason (team_id, season_id, league_id) VALUES (4, 1, 1);
INSERT INTO dbo.TeamSeason (team_id, season_id, league_id) VALUES (5, 1, 1);
INSERT INTO dbo.TeamSeason (team_id, season_id, league_id) VALUES (6, 1, 1);
INSERT INTO dbo.TeamSeason (team_id, season_id, league_id) VALUES (7, 1, 1);
INSERT INTO dbo.TeamSeason (team_id, season_id, league_id) VALUES (8, 1, 1);
INSERT INTO dbo.TeamSeason (team_id, season_id, league_id) VALUES (9, 1, 1);
INSERT INTO dbo.TeamSeason (team_id, season_id, league_id) VALUES (10, 1, 1);
INSERT INTO dbo.TeamSeason (team_id, season_id, league_id) VALUES (11, 1, 1);
INSERT INTO dbo.TeamSeason (team_id, season_id, league_id) VALUES (12, 1, 1);
INSERT INTO dbo.TeamSeason (team_id, season_id, league_id) VALUES (13, 1, 1);
INSERT INTO dbo.TeamSeason (team_id, season_id, league_id) VALUES (14, 1, 1);

-- --------------------------------------------------
-- Verifying all tables
-- --------------------------------------------------

SELECT * FROM dbo.Season ORDER BY id ASC
SELECT * FROM dbo.League ORDER BY id ASC
--SELECT * FROM dbo.Conference ORDER BY id ASC
--SELECT * FROM dbo.Division ORDER BY id ASC
SELECT * FROM dbo.Team ORDER BY id ASC
SELECT * FROM dbo.LeagueSeason ORDER BY id ASC
SELECT * FROM dbo.TeamSeason ORDER BY id ASC
SELECT * FROM dbo.Game ORDER BY id ASC

-- --------------------------------------------------
-- Script has ended
-- --------------------------------------------------
