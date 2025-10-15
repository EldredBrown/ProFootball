SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
USE ProFootballDb
GO
-- =============================================
-- Author:		Eldred Brown
-- Create date: 2016-11-21
-- Description:	A function to get all games played by a team
-- Revision History:
--	2017-01-05	Eldred Brown
--	*	Added parameter to restrict results to a single season
--	2025-10-02	Eldred Brown
--	*	Changed variable names to snake_case to make more Pythonic
--	2025-10-14	Eldred Brown
--	*	Referenced team and season data by id, not by name or year
-- =============================================
CREATE FUNCTION dbo.fn_GetTeamSeasonGames
(	
	-- Add the parameters for the function here
	@team_id int,
	@season_id int
)
RETURNS TABLE 
AS
RETURN 
(
	-- Add the SELECT statement with parameter references here
	SELECT
		game.id,
		season.year AS season,
		host_name AS opponent,
		guest_score AS points_for,
		host_score AS points_against
	FROM
		dbo.Game as game
			INNER JOIN dbo.Team as team
				ON team.id = @team_id
			INNER JOIN dbo.Season AS season
				ON game.season_id = season.id
	WHERE guest_name = team.name AND season_id = @season_id
	UNION
	SELECT
		game.id,
		season.year AS season,
		guest_name AS opponent,
		host_score AS points_for,
		guest_score AS points_against
	FROM
		dbo.Game as game
			INNER JOIN dbo.Team as team
				ON team.id = @team_id
			INNER JOIN dbo.Season AS season
				ON game.season_id = season.id
	WHERE host_name = team.name AND season_id = @season_id
)
