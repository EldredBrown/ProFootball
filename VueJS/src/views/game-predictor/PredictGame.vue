<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">Predict Game</h2>
      <div class="card">
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="guestSeason"
              >Guest Season</label>
              <select
                id="guestSeason"
                v-model="guestSeason"
                @change="selectGuestSeason()"
              >
                <option
                  v-for="season in seasons"
                  :key="season.id"
                >{{season.year}}</option>
              </select>
            </div>
            <div class="field">
              <label
                class="label"
                for="guestName"
              >Guest</label>
              <select
                id="guestName"
                v-model="guestName"
              >
                <option>Select Guest</option>
                <option
                  v-for="teamSeason in teamSeasons"
                  :key="teamSeason.id"
                >
                  {{teamSeason.teamName}}
                </option>
              </select>
            </div>
            <div class="field">
              <label
                class="label"
                for="guestScore"
              >Guest Score</label>
              <b id="guestScore">{{guestScore}}</b>
            </div>

            <div class="field">
              <label
                class="label"
                for="hostSeason"
              >Host Season</label>
              <select
                id="hostSeason"
                v-model="hostSeason"
                @change="selectHostSeason()"
              >
                <option
                  v-for="season in seasons"
                  :key="season.id"
                >{{season.year}}</option>
              </select>
            </div>
            <div class="field">
              <label
                class="label"
                for="hostName"
              >Host</label>
              <select
                id="hostName"
                v-model="hostName"
              >
                <option>Select Host</option>
                <option
                  v-for="teamSeason in teamSeasons"
                  :key="teamSeason.id"
                >
                  {{teamSeason.teamName}}
                </option>
              </select>
            </div>
            <div class="field">
              <label
                class="label"
                for="hostScore"
              >Host Score</label>
              <b id="hostScore">{{hostScore}}</b>
            </div>

          </div>
        </div>
      </div>
      <footer class="card-footer">
        <button
          class="link card-footer-item"
          @click="calculatePrediction()"
        >Calculate Prediction</button>
      </footer>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

const firstYear = 1920;
const guestOrHost = {
  guest: 1,
  host: 2,
};

let teamSeasonsCache = null;

export default {
  name: 'PredictGame',
  components: {},
  data() {
    return {
      guestSeason: firstYear,
      guestName: 'Select Guest',
      guestScore: null,
      hostSeason: firstYear,
      hostName: 'Select Host',
      hostScore: null,
    };
  },
  async created() {
    await this.loadSeasons();
    await this.loadTeamNames(guestOrHost.guest);
    await this.loadTeamNames(guestOrHost.host);
  },
  computed: {
    ...mapState(['seasons', 'teamSeasons']),
  },
  methods: {
    ...mapActions(['getSeasonsAction', 'getTeamSeasonsAction']),
    calculatePrediction() {
      this.guestScore = 0;
      this.hostScore = 0;
    },
    async loadSeasons() {
      await this.getSeasonsAction();
    },
    async loadTeamNames(guestOrHost, year = firstYear) {
      if (!teamSeasonsCache) {
        teamSeasonsCache = await this.getTeamSeasonsAction();
      }

      this.teamSeasons = teamSeasonsCache.filter(ts => ts.seasonYear === year);
    },
    async selectGuestSeason() {
      this.guestSeason = parseInt(this.guestSeason);
    },
    async selectHostSeason() {
      this.hostSeason = parseInt(this.hostSeason);
    },
  },
};
</script>
