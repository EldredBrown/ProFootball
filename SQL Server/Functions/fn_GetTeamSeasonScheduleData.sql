SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
USE ProFootballDb
GO
-- =============================================
-- Author:		Eldred Brown
-- Create date: 2016-11-21
-- Description:	A function to return a table showing how all 
--				of a team's opponents performed against their other opponents
-- Revision History:
--	2017-08-08	Eldred Brown
--	*	Added logic to prevent DivisionByZero exceptions.
--	2017-01-05	Eldred Brown
--	*	Added parameter to restrict results to a single season
--	2025-10-02	Eldred Brown
--	*	Changed variable names to snake_case to make more Pythonic
--	2025-10-14	Eldred Brown
--	*	Referenced team and season data by id, not by name or year
-- =============================================
CREATE FUNCTION dbo.fn_GetTeamSeasonScheduleData 
(	
	-- Add the parameters for the function here
	@team_id int,
	@season_id int
)
RETURNS @tbl TABLE
(
	id						int,
	opponent				varchar(50),
	wins					int,
	losses					int,
	ties					int,
	winning_percentage		float,
	weighted_games			int,
	weighted_points_for		int,
	weighted_points_against	int
)
AS
BEGIN
	-- Add the SELECT statement with parameter references here
	BEGIN
		INSERT @tbl

		SELECT
			tsg.id,
			tsg.opponent AS opponent,
			ts.wins AS wins,
			ts.losses AS losses,
			ts.ties AS ties,
			winning_percentage = 
				CASE
					WHEN ts.games = 0 THEN NULL		-- Prevent division by zero.
					ELSE CAST((2 * ts.wins + ts.ties) as float) / (2 * ts.games)
				END,
			(ts.games - 1) AS weighted_games,
			(ts.points_for - tsg.points_against) AS weighted_points_for,
			(ts.points_against - tsg.points_for) AS weighted_points_against
		FROM dbo.TeamSeason AS ts
			INNER JOIN dbo.Team AS team
				ON team.id = ts.team_id
			INNER JOIN dbo.fn_GetTeamSeasonGames(@team_id, @season_id) AS tsg
				ON team.name = tsg.opponent
		WHERE
			ts.season_id = @season_id
	END

	RETURN
END
GO
