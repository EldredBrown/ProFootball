SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
USE ProFootballDb
GO
-- =============================================
-- Author:		Eldred Brown
-- Create date: 2016-11-25
-- Description:	A procedure to compute and return final total ratings for all teams
-- Revision History:
--	2017-01-17	Eldred Brown
--	*	Added logic to restrict results to one season
--	2025-10-02	Eldred Brown
--	*	Changed variable names to snake_case to make more Pythonic
--	2025-10-14	Eldred Brown
--	*	Referenced team and season data by id, not by name or year
-- =============================================
CREATE PROCEDURE dbo.sp_GetRankingsTotal
	-- Add the parameters for the stored procedure here
	@season_id int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	-- Insert statements for procedure here
	SELECT
		team.name AS team,
		wins,
		losses,
		ties,
		offensive_average,
		offensive_factor,
		offensive_index,
		defensive_average,
		defensive_factor,
		defensive_index,
		final_expected_winning_percentage
	FROM
		dbo.TeamSeason AS ts
			INNER JOIN dbo.Team as team
				ON ts.team_id = team.id
	WHERE
		season_id = @season_id
	ORDER BY
		final_expected_winning_percentage DESC

END
GO
