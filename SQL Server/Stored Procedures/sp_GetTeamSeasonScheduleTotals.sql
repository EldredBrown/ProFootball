SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
USE ProFootballDb
GO
-- =============================================
-- Author:		Eldred Brown
-- Create date: 2016-11-21
-- Description:	A procedure to compute and return the totals of a team's 
--				schedule final data
-- Revision History:
--	2017-01-05	Eldred Brown
--	*	Added parameter to restrict results to a single season
--	2025-10-02	Eldred Brown
--	*	Changed variable names to snake_case to make more Pythonic
--	2025-10-14	Eldred Brown
--	*	Referenced team and season data by id, not by name or year
-- =============================================
CREATE PROCEDURE dbo.sp_GetTeamSeasonScheduleTotals 
	-- Add the parameters for the stored procedure here
	@team_id int,
	@season_id int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	-- Validate arguments.
	IF EXISTS (
		-- Verify that @team_id is the id of a valid team.
		SELECT name FROM dbo.Team WHERE id = @team_id
	)
	AND EXISTS (
		-- Verify that @season_id is the id of a valid season.
		SELECT year FROM dbo.Season WHERE id = @season_id
	)
	BEGIN
		-- Insert statements for procedure here
		SELECT
			games,
			points_for,
			points_against,
			schedule_wins,
			schedule_losses,
			schedule_ties,
			schedule_winning_percentage,
			schedule_games,
			schedule_points_for,
			schedule_points_against
		FROM dbo.fn_GetTeamSeasonScheduleTotals(@team_id, @season_id)

	END
END
GO
