<template>
  <nav class="column is-2 menu">
    <p class="menu-label">Menu</p>
    <ul class="menu-list">
      <router-link to="/">Home</router-link>
      <router-link to="/seasons/index">Seasons</router-link>
      <router-link to="/leagues/index">Leagues</router-link>
      <router-link to="/teams/index">Teams</router-link>
      <router-link to="/league-seasons/index">League Seasons</router-link>
      <router-link to="/team-seasons-admin/index">Team Seasons (Admin)
      </router-link>
      <router-link to="/team-seasons/index">Team Seasons</router-link>
      <router-link to="/games/index">Games</router-link>
      <router-link to="/season-standings/index">Season Standings</router-link>
      <router-link to="/game-predictor/predict-game">Predict Game</router-link>
      <router-link to="/about">About</router-link>
    </ul>
  </nav>
</template>
