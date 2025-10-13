SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
USE ProFootballDb
GO
-- =============================================
-- Author:		Eldred Brown
-- Create date: 2017-01-14
-- Description:	A procedure to return a conference's season standings
-- Revision history:
--	2025-10-02	Eldred Brown	Changed variable names to snake_case to make more Pythonic
-- =============================================
CREATE PROCEDURE dbo.sp_GetSeasonStandingsForConference
	-- Add the parameters for the stored procedure here
	@season_year smallint,
	@conference_name varchar(5)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	-- Validate arguments.
	IF EXISTS (
		SELECT year FROM dbo.Season WHERE year = @season_year
	)
	AND EXISTS (
		SELECT short_name FROM dbo.Conference WHERE short_name = @conference_name
	)
	BEGIN
		-- Insert statements for procedure here
		SELECT
			team_name as team,
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
			dbo.TeamSeason
		WHERE
			season_year = @season_year
			AND
			conference_name = @conference_name
		ORDER BY winning_percentage DESC, wins DESC, losses ASC, team_name ASC

	END
END
GO
