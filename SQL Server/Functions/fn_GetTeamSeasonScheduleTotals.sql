SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
USE ProFootballDb
GO
-- =============================================
-- Author:		Eldred Brown
-- Create date: 2016-11-21
-- Description:	A function to compute and return the totals of a team's 
--				schedule final data
-- Revision History:
--	2017-08-08	Eldred Brown
--	*	Added logic to prevent DivisionByZero exceptions
--	2017-01-05	Eldred Brown
--	*	Added parameter to restrict results to a single season
--	2025-10-02	Eldred Brown
--	*	Changed variable names to snake_case to make more Pythonic
--	2025-10-14	Eldred Brown
--	*	Referenced team and season data by id, not by name or year
-- =============================================
CREATE FUNCTION dbo.fn_GetTeamSeasonScheduleTotals
(	
	-- Add the parameters for the function here
	@team_id int,
	@season_id int
)
RETURNS @tbl TABLE
(
	games						int,
	points_for					int,
	points_against				int,
	schedule_wins				int,
	schedule_losses				int,
	schedule_ties				int,
	schedule_winning_percentage	float,
	schedule_games				int,
	schedule_points_for			int,
	schedule_points_against		int
)
AS
BEGIN
	-- Add the SELECT statement with parameter references here
	BEGIN
		INSERT @tbl

		SELECT
			COUNT(tssp.opponent) AS games,
			SUM(tssp.game_points_for) AS points_for,
			SUM(tssp.game_points_against) AS points_against,
			SUM(tssd.wins) AS schedule_wins,
			SUM(tssd.losses) AS schedule_losses,
			SUM(tssd.ties) AS schedule_ties,
			schedule_winning_percentage = 
				CASE		-- Prevent division by zero.
					WHEN (SUM(tssd.wins) + SUM(tssd.losses) + SUM(tssd.ties)) = 0
						THEN NULL
					ELSE (
						CAST(2 * SUM(tssd.wins) + SUM(tssd.ties) as decimal) / 
						(2 * (SUM(tssd.wins) + SUM(tssd.losses) + SUM(tssd.ties)))
					)
				END,
			SUM(tssd.weighted_games) AS schedule_games,
			SUM(tssd.weighted_points_for) AS schedule_points_for,
			SUM(tssd.weighted_points_against) AS schedule_points_against
		FROM dbo.fn_GetTeamSeasonScheduleProfile(@team_id, @season_id) AS tssp
			INNER JOIN dbo.fn_GetTeamSeasonScheduleData(@team_id, @season_id) AS tssd
				ON tssp.opponent = tssd.opponent
	END

	RETURN
END
GO
