import * as axios from 'axios';

import { API } from './config';

async function getGames() {
  try {
    const response = await axios.get(`${API}/games`);

    let data = parseList(response);

    const games = data.map(g => {
      return g;
    });

    return games;
  } catch (error) {
    console.error(error);
    return [];
  }
}

async function getGame(id) {
  try {
    const response = await axios.get(`${API}/games/${id}`);
    let game = parseItem(response, 200);
    return game;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function addGame(game) {
  try {
    const response = await axios.post(`${API}/games`, game);
    const addedGame = parseItem(response, 201);
    return addedGame;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function updateGame(oldGame, newGame) {
  try {
    const response = await axios.put(`${API}/games/${newGame.id}`, {
      'oldGame': oldGame, 'newGame': newGame
    });
    const updatedGame = parseItem(response, 200);
    return updatedGame;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function deleteGame(game) {
  try {
    const response = await axios.delete(`${API}/games/${game.id}`);
    parseItem(response, 200);
    return game.id;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function getLeagues() {
  try {
    const response = await axios.get(`${API}/leagues`);

    let data = parseList(response);

    const leagues = data.map(l => {
      return l;
    });

    return leagues;
  } catch (error) {
    console.error(error);
    return [];
  }
}

async function getLeague(id) {
  try {
    const response = await axios.get(`${API}/leagues/${id}`);
    let league = parseItem(response, 200);
    return league;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function addLeague(league) {
  try {
    const response = await axios.post(`${API}/leagues`, league);
    const addedLeague = parseItem(response, 201);
    return addedLeague;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function updateLeague(league) {
  try {
    const response = await axios.put(`${API}/leagues/${league.id}`, league);
    const updatedLeague = parseItem(response, 200);
    return updatedLeague;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function deleteLeague(league) {
  try {
    const response = await axios.delete(`${API}/leagues/${league.id}`);
    parseItem(response, 200);
    return league.id;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function getLeagueSeasons() {
  try {
    const response = await axios.get(`${API}/leagueSeasons`);

    let data = parseList(response);

    const leagueSeasons = data.map(ls => {
      return ls;
    });

    return leagueSeasons;
  } catch (error) {
    console.error(error);
    return [];
  }
}

async function getLeagueSeason(id) {
  try {
    const response = await axios.get(`${API}/leagueSeasons/${id}`);
    let leagueSeason = parseItem(response, 200);
    return leagueSeason;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function addLeagueSeason(leagueSeason) {
  try {
    const response = await axios.post(`${API}/leagueSeasons`, leagueSeason);
    const addedLeagueSeason = parseItem(response, 201);
    return addedLeagueSeason;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function updateLeagueSeason(leagueSeason) {
  try {
    const response = await axios.put(`${API}/leagueSeasons/${leagueSeason.id}`, leagueSeason);
    const updatedLeagueSeason = parseItem(response, 200);
    return updatedLeagueSeason;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function deleteLeagueSeason(leagueSeason) {
  try {
    const response = await axios.delete(`${API}/leagueSeasons/${leagueSeason.id}`);
    parseItem(response, 200);
    return leagueSeason.id;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function getSeasons() {
  try {
    const response = await axios.get(`${API}/seasons`);

    let data = parseList(response);

    const seasons = data.map(s => {
      return s;
    });

    return seasons;
  } catch (error) {
    console.error(error);
    return [];
  }
}

async function getSeason(id) {
  try {
    const response = await axios.get(`${API}/seasons/${id}`);
    let season = parseItem(response, 200);
    return season;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function addSeason(season) {
  try {
    const response = await axios.post(`${API}/seasons`, season);
    const addedSeason = parseItem(response, 201);
    return addedSeason;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function updateSeason(season) {
  try {
    const response = await axios.put(`${API}/seasons/${season.id}`, season);
    const updatedSeason = parseItem(response, 200);
    return updatedSeason;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function deleteSeason(season) {
  try {
    const response = await axios.delete(`${API}/seasons/${season.id}`);
    parseItem(response, 200);
    return season.id;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function getSeasonStandings(seasonYear) {
  try {
    const response = await axios.get(`${API}/seasonStandings/${seasonYear}`);

    let data = parseList(response);

    const seasonStandings = data.map(ss => {
      return ss;
    });

    return seasonStandings;
  } catch (error) {
    console.error(error);
    return [];
  }
}

async function getTeams() {
  try {
    const response = await axios.get(`${API}/teams`);

    let data = parseList(response);

    const teams = data.map(t => {
      return t;
    });

    return teams;
  } catch (error) {
    console.error(error);
    return [];
  }
}

async function getTeam(id) {
  try {
    const response = await axios.get(`${API}/teams/${id}`);
    let team = parseItem(response, 200);
    return team;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function addTeam(team) {
  try {
    const response = await axios.post(`${API}/teams`, team);
    const addedTeam = parseItem(response, 201);
    return addedTeam;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function updateTeam(team) {
  try {
    const response = await axios.put(`${API}/teams/${team.id}`, team);
    const updatedTeam = parseItem(response, 200);
    return updatedTeam;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function deleteTeam(team) {
  try {
    const response = await axios.delete(`${API}/teams/${team.id}`);
    parseItem(response, 200);
    return team.id;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function getTeamSeasons() {
  try {
    const response = await axios.get(`${API}/teamSeasons`);

    let data = parseList(response);

    const teamSeasons = data.map(ts => {
      return ts;
    });

    return teamSeasons;
  } catch (error) {
    console.error(error);
    return [];
  }
}

async function getTeamSeason(id) {
  try {
    const response = await axios.get(`${API}/teamSeasons/${id}`);
    let teamSeason = parseItem(response, 200);
    return teamSeason;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function addTeamSeason(teamSeason) {
  try {
    const response = await axios.post(`${API}/teamSeasons`, teamSeason);
    const addedTeamSeason = parseItem(response, 201);
    return addedTeamSeason;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function updateTeamSeason(teamSeason) {
  try {
    const response = await axios.put(`${API}/teamSeasons/${teamSeason.id}`, teamSeason);
    const updatedTeamSeason = parseItem(response, 200);
    return updatedTeamSeason;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function deleteTeamSeason(teamSeason) {
  try {
    const response = await axios.delete(`${API}/teamSeasons/${teamSeason.id}`);
    parseItem(response, 200);
    return teamSeason.id;
  } catch (error) {
    console.error(error);
    return null;
  }
}

function parseList(response) {
  if (response.status !== 200) {
    throw Error(response.message);
  }

  if (!response.data) {
    return [];
  }

  let list = response.data;
  if (typeof list !== "object") {
    list = [];
  }

  return list;
}

function parseItem(response, code) {
  if (response.status !== code) {
    throw Error(response.message);
  }

  let item = response.data;
  if (typeof item !== 'object') {
    item = undefined;
  }

  return item;
}

export const dataService = {
  getGames,
  getGame,
  addGame,
  updateGame,
  deleteGame,
  getLeagues,
  getLeague,
  addLeague,
  updateLeague,
  deleteLeague,
  getLeagueSeasons,
  getLeagueSeason,
  addLeagueSeason,
  updateLeagueSeason,
  deleteLeagueSeason,
  getSeasons,
  getSeason,
  addSeason,
  updateSeason,
  deleteSeason,
  getSeasonStandings,
  getTeams,
  getTeam,
  addTeam,
  updateTeam,
  deleteTeam,
  getTeamSeasons,
  getTeamSeason,
  addTeamSeason,
  updateTeamSeason,
  deleteTeamSeason,
};
