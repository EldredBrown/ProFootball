SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
USE ProFootballDb
GO
-- =============================================
-- Author:		Eldred Brown
-- Create date: 2016-11-25
-- Description:	A procedure to compute and return final defensive ratings for all teams
-- Revision History:
--	2017-01-17	Eldred Brown	Added logic to restrict results to one season
--	2025-10-02	Eldred Brown	Changed variable names to snake_case to make more Pythonic
-- =============================================
CREATE PROCEDURE dbo.sp_GetRankingsDefensive
	-- Add the parameters for the stored procedure here
	@season_year smallint
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	-- Insert statements for procedure here
	SELECT
		team_name AS team,
		wins,
		losses,
		ties,
		defensive_average,
		defensive_factor,
		defensive_index
	FROM
		dbo.TeamSeason
	WHERE
		season_year = @season_year
	ORDER BY
		defensive_index ASC
END
GO
