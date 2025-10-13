SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
USE ProFootballDb
GO
-- =============================================
-- Author:		Eldred Brown
-- Create date: 2016-11-23
-- Description:	A procedure to return the averages of a team's schedule data
-- Revision History:
--	2017-01-05	Eldred Brown
--	*	Added parameter to restrict results to a single season
--	2025-10-02	Eldred Brown	Changed variable names to snake_case to make more Pythonic
-- =============================================
CREATE PROCEDURE dbo.sp_GetTeamSeasonScheduleAverages
	-- Add the parameters for the stored procedure here
	@team_name varchar(50),
	@season_year smallint
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	-- Validate arguments.
	IF EXISTS (
		-- Verify that @team_name is the name of a valid team.
		SELECT name FROM dbo.Team WHERE name = @team_name
	)
	AND EXISTS (
		-- Verify that @season_year is the year of a valid season.
		SELECT year FROM dbo.Season WHERE year = @season_year
	)
	BEGIN
		-- Insert statements for procedure here
		SELECT
			avg_points_for = 
				CASE
					WHEN games = 0 THEN NULL
					ELSE ROUND(CAST(points_for as float) / games, 2)
				END,
			avg_points_against = 
				CASE
					WHEN games = 0 THEN NULL
					ELSE ROUND(CAST(points_against as float) / games, 2)
				END,
			avg_schedule_points_for = 
				CASE
					WHEN schedule_games = 0 THEN NULL
					ELSE ROUND(CAST(schedule_points_for as float) / schedule_games, 2)
				END,
			avg_schedule_points_against = 
				CASE
					WHEN schedule_games = 0 THEN NULL
					ELSE ROUND(CAST(schedule_points_against as float) / schedule_games, 2)
				END
		FROM
			dbo.fn_GetTeamSeasonScheduleTotals(@team_name, @season_year)

	END
END
GO
