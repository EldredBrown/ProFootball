<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">Team Season</h2>
      <div class="card">
        <header class="card-header">
          <p class="card-header-title">Details</p>
        </header>
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="teamName"
              >Team</label>
              <label
                class="input"
                name="teamName"
                readonly
              >{{ teamSeason.teamName }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="seasonYear"
              >Season</label>
              <label
                class="input"
                name="seasonYear"
                readonly
              >{{ teamSeason.seasonYear }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="wins"
              >Wins</label>
              <label
                class="input"
                name="wins"
                readonly
              >{{ teamSeason.wins }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="losses"
              >Losses</label>
              <label
                class="input"
                name="losses"
                readonly
              >{{ teamSeason.losses }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="ties"
              >Ties</label>
              <label
                class="input"
                name="ties"
                readonly
              >{{ teamSeason.ties }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="winningPercentage"
              >Winning Percentage</label>
              <label
                class="input"
                name="winningPercentage"
                readonly
              >{{ teamSeason.winningPercentage }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="pointsFor"
              >Points For</label>
              <label
                class="input"
                name="pointsFor"
                readonly
              >{{ teamSeason.pointsFor }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="pointsAgainst"
              >Points Against</label>
              <label
                class="input"
                name="pointsAgainst"
                readonly
              >{{ teamSeason.pointsAgainst }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="pythagoreanWins"
              >Expected Wins</label>
              <label
                class="input"
                name="pythagoreanWins"
                readonly
              >{{ teamSeason.pythagoreanWins }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="pythagoreanLosses"
              >Expected Losses</label>
              <label
                class="input"
                name="pythagoreanLosses"
                readonly
              >{{ teamSeason.pythagoreanLosses }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="offensiveAverage"
              >Offensive Average</label>
              <label
                class="input"
                name="offensiveAverage"
                readonly
              >{{ teamSeason.offensiveAverage }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="offensiveFactor"
              >Offensive Factor</label>
              <label
                class="input"
                name="offensiveFactor"
                readonly
              >{{ teamSeason.offensiveFactor }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="offensiveIndex"
              >Offensive Index</label>
              <label
                class="input"
                name="offensiveIndex"
                readonly
              >{{ teamSeason.offensiveIndex }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="defensiveAverage"
              >Defensive Average</label>
              <label
                class="input"
                name="defensiveAverage"
                readonly
              >{{ teamSeason.defensiveAverage }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="defensiveFactor"
              >Defensive Factor</label>
              <label
                class="input"
                name="defensiveFactor"
                readonly
              >{{ teamSeason.defensiveFactor }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="defensiveIndex"
              >Defensive Index</label>
              <label
                class="input"
                name="defensiveIndex"
                readonly
              >{{ teamSeason.defensiveIndex }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="finalPythagoreanWinningPercentage"
              >Final Expected W-L%</label>
              <label
                class="input"
                name="finalPythagoreanWinningPercentage"
                readonly
              >{{ teamSeason.finalPythagoreanWinningPercentage }}</label>
            </div>
          </div>
        </div>
      </div>
      <router-link
        tag="button"
        class="button"
        :to="{ name: 'TeamSeasonIndex' }"
      >
        <!-- For development mode -->
        <font-awesome-icon
          :icon="['fas', 'backward']"
          class="fas"
        />
        <!-- For production or test mode -->
        <!-- <i class="fas fa-backward"></i> -->
        <span>Back to List</span>
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'TeamSeasonDetails',
  props: {
    id: {
      type: Number,
      default: 0,
    },
  },
  data() {
    return {
      teamSeason: {},
    };
  },
  created() {
    this.teamSeason = this.getTeamSeasonById(this.id);
  },
  computed: {
    ...mapGetters(['getTeamSeasonById']),
  },
};
</script>
