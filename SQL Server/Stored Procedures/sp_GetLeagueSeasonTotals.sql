SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
USE ProFootballDb
GO
-- =============================================
-- Author:		Eldred Brown
-- Create date: 2016-12-06
-- Description:	A procedure to compute and return the NFL's total scoring
-- Revision History:
--	2017-03-08	Eldred Brown
--	*	Added parameter to limit results to one league and one season
--	2025-10-02	Eldred Brown
--	*	Changed variable names to snake_case to make more Pythonic
--	2025-10-14	Eldred Brown
--	*	Referenced team and season data by id, not by name or year
-- =============================================
CREATE PROCEDURE dbo.sp_GetLeagueSeasonTotals
	-- Add the parameters for the stored procedure here
	@league_id int,
	@season_id int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	SELECT
		SUM(games) AS total_games,
		SUM(points_for) AS total_points,
		average_points =
			CASE
				WHEN SUM(games) = 0 THEN NULL
				ELSE ROUND(CAST(SUM(points_for) as float) / SUM(games), 2)
			END,
		ROUND(AVG(games), 0) AS week_count
	FROM
		dbo.TeamSeason
	WHERE
		league_id = @league_id
		AND
		season_id = @season_id
END
GO
