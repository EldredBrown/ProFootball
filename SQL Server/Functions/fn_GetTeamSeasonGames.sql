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
--	2025-10-02	Eldred Brown	Changed variable names to snake_case to make more Pythonic
-- =============================================
CREATE FUNCTION dbo.fn_GetTeamSeasonGames
(	
	-- Add the parameters for the function here
	@team_name varchar(50),
	@season_year smallint
)
RETURNS TABLE 
AS
RETURN 
(
	-- Add the SELECT statement with parameter references here
	SELECT
		id,
		season_year AS season,
		host_name AS opponent,
		guest_score AS points_for,
		host_score AS points_against
	FROM
		dbo.Game
	WHERE guest_name = @team_name AND season_year = @season_year
	UNION
	SELECT
		id,
		season_year AS season,
		guest_name AS opponent,
		host_score AS points_for,
		guest_score AS points_against
	FROM
		dbo.Game
	WHERE host_name = @team_name AND season_year = @season_year
)
