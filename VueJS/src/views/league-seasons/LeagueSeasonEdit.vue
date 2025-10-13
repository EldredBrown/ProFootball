<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">League Season</h2>
      <div class="card">
        <header class="card-header">
          <p class="card-header-title">{{title}}</p>
        </header>
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="id"
              >ID</label>
              <label
                class="input"
                name="id"
                readonly
              >{{ leagueSeason.id }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="leagueName"
              >League</label>
              <input
                class="input"
                id="leagueName"
                v-model="leagueSeason.leagueName"
                :class="{ invalid: !leagueSeason.leagueName }"
              />
            </div>
            <div class="field">
              <label
                class="label"
                for="seasonYear"
              >Season</label>
              <input
                class="input"
                id="seasonYear"
                v-model="leagueSeason.seasonYear"
                :class="{ invalid: !leagueSeason.seasonYear }"
              />
            </div>
            <div class="field">
              <label
                class="label"
                for="totalGames"
              >Total Games</label>
              <input
                class="input"
                id="totalGames"
                v-model="leagueSeason.totalGames"
              />
            </div>
            <div class="field">
              <label
                class="label"
                for="totalPoints"
              >Total Points</label>
              <input
                class="input"
                id="totalPoints"
                v-model="leagueSeason.totalPoints"
              />
            </div>
            <div class="field">
              <label
                class="label"
                for="averagePoints"
              >Average Points</label>
              <input
                class="input"
                id="averagePoints"
                v-model="leagueSeason.averagePoints"
              />
            </div>
          </div>
        </div>
        <footer class="card-footer">
          <button
            class="link card-footer-item"
            @click="saveLeagueSeason()"
          >
            <!-- For development mode -->
            <font-awesome-icon
              :icon="['fas', 'save']"
              class="fas"
            />
            <!-- For production or test mode -->
            <!-- <i class="fas fa-save"></i> -->
            <span>Save</span>
          </button>
          <button
            class="link card-footer-item cancel-button"
            @click="cancelLeagueSeason()"
          >
            <!-- For development mode -->
            <font-awesome-icon
              :icon="['fas', 'undo']"
              class="fas"
            />
            <!-- For production or test mode -->
            <!-- <i class="fas fa-undo"></i> -->
            <span>Cancel</span>
          </button>
        </footer>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import { cloneDeep } from 'lodash';

export default {
  name: 'LeagueSeasonEdit',
  props: {
    id: {
      type: Number,
      default: 0,
    },
  },
  data() {
    return {
      leagueSeason: {},
    };
  },
  created() {
    if (this.isAddMode) {
      this.leagueSeason = {
        id: undefined,
        leagueName: '',
        seasonYear: 0,
        totalGames: 0,
        totalPoints: 0,
        averagePoints: 0,
      };
    } else {
      this.leagueSeason = cloneDeep(this.getLeagueSeasonById(this.id));
    }
  },
  computed: {
    ...mapGetters(['getLeagueSeasonById']),
    isAddMode() {
      return !this.id;
    },
    title() {
      return `${this.isAddMode ? 'Add' : 'Edit'}`;
    },
  },
  methods: {
    ...mapActions(['addLeagueSeasonAction', 'updateLeagueSeasonAction']),
    cancelLeagueSeason() {
      this.$router.push({ name: 'LeagueSeasonIndex' });
    },
    async saveLeagueSeason() {
      this.validateInput();
      this.leagueSeason.id
        ? await this.updateLeagueSeasonAction(this.leagueSeason)
        : await this.addLeagueSeasonAction(this.leagueSeason);
      this.$router.push({ name: 'LeagueSeasonIndex' });
    },
    validateInput() {
      this.leagueSeason.seasonYear = parseInt(this.leagueSeason.seasonYear);
      this.leagueSeason.totalGames = parseInt(this.leagueSeason.totalGames);
      this.leagueSeason.totalPoints = parseInt(this.leagueSeason.totalPoints);
      this.leagueSeason.averagePoints = parseFloat(
        this.leagueSeason.averagePoints,
      );
    },
  },
};
</script>
