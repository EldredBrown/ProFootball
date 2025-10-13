import Vue from 'vue';
import Vuex from 'vuex';

import { dataService } from '../shared';
import {
  GET_GAMES,
  ADD_GAME,
  UPDATE_GAME,
  DELETE_GAME,
  GET_LEAGUES,
  ADD_LEAGUE,
  UPDATE_LEAGUE,
  DELETE_LEAGUE,
  GET_LEAGUE_SEASONS,
  ADD_LEAGUE_SEASON,
  UPDATE_LEAGUE_SEASON,
  DELETE_LEAGUE_SEASON,
  GET_SEASONS,
  ADD_SEASON,
  UPDATE_SEASON,
  DELETE_SEASON,
  GET_SEASON_STANDINGS,
  GET_TEAMS,
  ADD_TEAM,
  UPDATE_TEAM,
  DELETE_TEAM,
  GET_TEAM_SEASONS,
  ADD_TEAM_SEASON,
  UPDATE_TEAM_SEASON,
  DELETE_TEAM_SEASON,
} from './mutation-types';

Vue.use(Vuex);

const state = {
  games: [],
  leagues: [],
  leagueSeasons: [],
  seasons: [],
  seasonStandings: [],
  teams: [],
  teamSeasons: [],
};

const getters = {
  getGameById: state => id => state.games.find(g => g.id === id),
  getLeagueById: state => id => state.leagues.find(l => l.id === id),
  getLeagueSeasonById: state => id => state.leagueSeasons.find(ls => ls.id === id),
  getSeasonById: state => id => state.seasons.find(s => s.id === id),
  getTeamById: state => id => state.teams.find(t => t.id === id),
  getTeamSeasonById: state => id => state.teamSeasons.find(ts => ts.id === id),
  getTeamSeasonsByYear: state => year => state.teamSeasons.filter(ts => ts.seasonYear === year),
};

const mutations = {
  [GET_GAMES](state, games) {
    state.games = games;
  },
  [ADD_GAME](state, game) {
    state.games.push(game);
  },
  [UPDATE_GAME](state, game) {
    // TODO: Explore other ways to edit the selected state.
    const index = state.games.findIndex(g => g.id === game.id);
    state.games.splice(index, 1, game);
    state.games = [...state.games];
  },
  [DELETE_GAME](state, gameId) {
    // TODO: Explore other ways to delete the selected state.
    state.games = [...state.games.filter(g => g.id !== gameId)];
  },
  [GET_LEAGUES](state, leagues) {
    state.leagues = leagues;
  },
  [ADD_LEAGUE](state, league) {
    state.leagues.push(league);
  },
  [UPDATE_LEAGUE](state, league) {
    // TODO: Explore other ways to edit the selected state.
    const index = state.leagues.findIndex(l => l.id === league.id);
    state.leagues.splice(index, 1, league);
    state.leagues = [...state.leagues];
  },
  [DELETE_LEAGUE](state, leagueId) {
    // TODO: Explore other ways to delete the selected state.
    state.leagues = [...state.leagues.filter(l => l.id !== leagueId)];
  },
  [GET_LEAGUE_SEASONS](state, leagueSeasons) {
    state.leagueSeasons = leagueSeasons;
  },
  [ADD_LEAGUE_SEASON](state, leagueSeason) {
    state.leagueSeasons.push(leagueSeason);
  },
  [UPDATE_LEAGUE_SEASON](state, leagueSeason) {
    // TODO: Explore other ways to edit the selected state.
    const index = state.leagueSeasons.findIndex(ls => ls.id === leagueSeason.id);
    state.leagueSeasons.splice(index, 1, leagueSeason);
    state.leagueSeasons = [...state.leagueSeasons];
  },
  [DELETE_LEAGUE_SEASON](state, leagueSeasonId) {
    // TODO: Explore other ways to delete the selected state.
    state.leagueSeasons = [...state.leagueSeasons.filter(ls => ls.id !== leagueSeasonId)];
  },
  [GET_SEASONS](state, seasons) {
    state.seasons = seasons;
  },
  [ADD_SEASON](state, season) {
    state.seasons.push(season);
  },
  [UPDATE_SEASON](state, season) {
    // TODO: Explore other ways to edit the selected state.
    const index = state.seasons.findIndex(s => s.id === season.id);
    state.seasons.splice(index, 1, season);
    state.seasons = [...state.seasons];
  },
  [DELETE_SEASON](state, seasonId) {
    // TODO: Explore other ways to delete the selected state.
    state.seasons = [...state.seasons.filter(s => s.id !== seasonId)];
  },
  [GET_SEASON_STANDINGS](state, seasonStandings) {
    state.seasonStandings = seasonStandings;
  },
  [GET_TEAMS](state, teams) {
    state.teams = teams;
  },
  [ADD_TEAM](state, team) {
    state.teams.push(team);
  },
  [UPDATE_TEAM](state, team) {
    // TODO: Explore other ways to edit the selected state.
    const index = state.teams.findIndex(s => s.id === team.id);
    state.teams.splice(index, 1, team);
    state.teams = [...state.teams];
  },
  [DELETE_TEAM](state, teamId) {
    // TODO: Explore other ways to delete the selected state.
    state.teams = [...state.teams.filter(s => s.id !== teamId)];
  },
  [GET_TEAM_SEASONS](state, teamSeasons) {
    state.teamSeasons = teamSeasons;
  },
  [ADD_TEAM_SEASON](state, teamSeason) {
    state.teamSeasons.push(teamSeason);
  },
  [UPDATE_TEAM_SEASON](state, teamSeason) {
    // TODO: Explore other ways to edit the selected state.
    const index = state.teamSeasons.findIndex(ts => ts.id === teamSeason.id);
    state.teamSeasons.splice(index, 1, teamSeason);
    state.teamSeasons = [...state.teamSeasons];
  },
  [DELETE_TEAM_SEASON](state, teamSeasonId) {
    // TODO: Explore other ways to delete the selected state.
    state.teamSeasons = [...state.teamSeasons.filter(ts => ts.id !== teamSeasonId)];
  },
};

const actions = {
  async getGamesAction({ commit }) {
    const games = await dataService.getGames();
    commit(GET_GAMES, games);
  },
  async addGameAction({ commit }, game) {
    const addedGame = await dataService.addGame(game);
    commit(ADD_GAME, addedGame);
  },
  async updateGameAction({ commit }, games) {
    const updatedGame = await dataService.updateGame(games.oldGame, games.newGame);
    commit(UPDATE_GAME, updatedGame);
  },
  async deleteGameAction({ commit }, game) {
    const deletedGameId = await dataService.deleteGame(game);
    commit(DELETE_GAME, deletedGameId);
  },
  async getLeaguesAction({ commit }) {
    const leagues = await dataService.getLeagues();
    commit(GET_LEAGUES, leagues);
  },
  async addLeagueAction({ commit }, league) {
    const addedLeague = await dataService.addLeague(league);
    commit(ADD_LEAGUE, addedLeague);
  },
  async updateLeagueAction({ commit }, league) {
    const updatedLeague = await dataService.updateLeague(league);
    commit(UPDATE_LEAGUE, updatedLeague);
  },
  async deleteLeagueAction({ commit }, league) {
    const deletedLeagueId = await dataService.deleteLeague(league);
    commit(DELETE_LEAGUE, deletedLeagueId);
  },
  async getLeagueSeasonsAction({ commit }) {
    const leagueSeasons = await dataService.getLeagueSeasons();
    commit(GET_LEAGUE_SEASONS, leagueSeasons);
  },
  async addLeagueSeasonAction({ commit }, leagueSeason) {
    const addedLeagueSeason = await dataService.addLeagueSeason(leagueSeason);
    commit(ADD_LEAGUE_SEASON, addedLeagueSeason);
  },
  async updateLeagueSeasonAction({ commit }, leagueSeason) {
    const updatedLeagueSeason = await dataService.updateLeagueSeason(leagueSeason);
    commit(UPDATE_LEAGUE_SEASON, updatedLeagueSeason);
  },
  async deleteLeagueSeasonAction({ commit }, leagueSeason) {
    const deletedLeagueSeasonId = await dataService.deleteLeagueSeason(leagueSeason);
    commit(DELETE_LEAGUE_SEASON, deletedLeagueSeasonId);
  },
  async getSeasonsAction({ commit }) {
    const seasons = await dataService.getSeasons();
    commit(GET_SEASONS, seasons);
  },
  async addSeasonAction({ commit }, season) {
    const addedSeason = await dataService.addSeason(season);
    commit(ADD_SEASON, addedSeason);
  },
  async updateSeasonAction({ commit }, season) {
    const updatedSeason = await dataService.updateSeason(season);
    commit(UPDATE_SEASON, updatedSeason);
  },
  async deleteSeasonAction({ commit }, season) {
    const deletedSeasonId = await dataService.deleteSeason(season);
    commit(DELETE_SEASON, deletedSeasonId);
  },
  async getSeasonStandingsAction({ commit }, seasonYear) {
    const seasonStandings = await dataService.getSeasonStandings(seasonYear);
    commit(GET_SEASON_STANDINGS, seasonStandings);
  },
  async getTeamsAction({ commit }) {
    const teams = await dataService.getTeams();
    commit(GET_TEAMS, teams);
  },
  async addTeamAction({ commit }, team) {
    const addedTeam = await dataService.addTeam(team);
    commit(ADD_TEAM, addedTeam);
  },
  async updateTeamAction({ commit }, team) {
    const updatedTeam = await dataService.updateTeam(team);
    commit(UPDATE_TEAM, updatedTeam);
  },
  async deleteTeamAction({ commit }, team) {
    const deletedTeamId = await dataService.deleteTeam(team);
    commit(DELETE_TEAM, deletedTeamId);
  },
  async getTeamSeasonsAction({ commit }) {
    const teamSeasons = await dataService.getTeamSeasons();
    commit(GET_TEAM_SEASONS, teamSeasons);
  },
  async addTeamSeasonAction({ commit }, teamSeason) {
    const addedTeamSeason = await dataService.addTeamSeason(teamSeason);
    commit(ADD_TEAM_SEASON, addedTeamSeason);
  },
  async updateTeamSeasonAction({ commit }, teamSeason) {
    const updatedTeamSeason = await dataService.updateTeamSeason(teamSeason);
    commit(UPDATE_TEAM_SEASON, updatedTeamSeason);
  },
  async deleteTeamSeasonAction({ commit }, teamSeason) {
    const deletedTeamSeasonId = await dataService.deleteTeamSeason(teamSeason);
    commit(DELETE_TEAM_SEASON, deletedTeamSeasonId);
  },
};

const store = new Vuex.Store({
  strict: process.env.NODE_ENV !== 'production',
  state,
  getters,
  mutations,
  actions,
});

export default store;
