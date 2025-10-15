SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
USE ProFootballDb
GO
-- =============================================
-- Author:		Eldred Brown
-- Create date: 2019-02-10
-- Description:	A procedure to return a league's season standings
-- Revision history:
--	2025-10-02	Eldred Brown
--	*	Changed variable names to snake_case to make more Pythonic
--	2025-10-14	Eldred Brown
--	*	Referenced season data by id, not by year
-- =============================================
CREATE PROCEDURE dbo.sp_GetSeasonStandingsForLeague
	-- Add the parameters for the stored procedure here
	@season_id int,
	@league_id int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	-- Validate arguments.
	IF EXISTS (
		SELECT year FROM dbo.Season WHERE id = @season_id
	)
	AND EXISTS (
		SELECT short_name FROM dbo.League WHERE id = @league_id
	)
	BEGIN
		-- Insert statements for procedure here
		SELECT
			team.name as team,
			wins,
			losses,
			ties,
			winning_percentage =
				CASE
					WHEN games = 0 THEN NULL
					ELSE winning_percentage
				END,
			points_for,
			points_against,
			avg_points_for =
				CASE
					WHEN games = 0 THEN NULL
					ELSE (CAST(points_for as float) / games)
				END,
			avg_points_against =
				CASE
					WHEN games = 0 THEN NULL
					ELSE (CAST(points_against as float) / games)
				END
		FROM
			dbo.TeamSeason as ts
				INNER JOIN dbo.Team AS team
					ON ts.team_id = team.id
		WHERE
			season_id = @season_id
			AND
			league_id = @league_id
		ORDER BY
			winning_percentage DESC,
			wins DESC,
			losses ASC,
			team.name ASC

	END
END
GO
