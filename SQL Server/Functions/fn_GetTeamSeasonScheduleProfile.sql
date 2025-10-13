SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
USE ProFootballDb
GO
-- =============================================
-- Author:		Eldred Brown
-- Create date: 2016-11-21
-- Description:	A function to return a team's profile
-- Revision History:
--	2017-01-05	Eldred Brown
--	*	Added parameter to restrict results to a single season
--	2025-10-02	Eldred Brown	Changed variable names to snake_case to make more Pythonic
-- =============================================
CREATE FUNCTION dbo.fn_GetTeamSeasonScheduleProfile 
(	
	-- Add the parameters for the function here
	@team_name varchar(50),
	@season_year smallint
)
RETURNS @tbl TABLE
(
	id									int,
	opponent							varchar(50),
	game_points_for						int,
	game_points_against					int,
	opponent_wins						int,
	opponent_losses						int,
	opponent_ties						int,
	opponent_winning_percentage			float,
	opponent_weighted_games				int,
	opponent_weighted_points_for		int,
	opponent_weighted_points_against	int
)
AS
BEGIN
	-- Add the SELECT statement with parameter references here
	INSERT @tbl

	SELECT
		tsg.id,
		tsg.opponent,
		tsg.points_for,
		tsg.points_against,
		tssd.wins,
		tssd.losses,
		tssd.ties,
		tssd.winning_percentage,
		tssd.weighted_games,
		tssd.weighted_points_for,
		tssd.weighted_points_against
	FROM dbo.fn_GetTeamSeasonGames(@team_name, @season_year) AS tsg
		INNER JOIN dbo.fn_GetTeamSeasonScheduleData(@team_name, @season_year) AS tssd
			ON tsg.id = tssd.id

	RETURN
END
