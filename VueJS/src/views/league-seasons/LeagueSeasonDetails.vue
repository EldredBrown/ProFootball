<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">League Season</h2>
      <div class="card">
        <header class="card-header">
          <p class="card-header-title">Details</p>
        </header>
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="leagueName"
              >League</label>
              <label
                class="input"
                name="leagueName"
                readonly
              >{{ leagueSeason.leagueName }}</label>
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
              >{{ leagueSeason.seasonYear }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="totalGames"
              >Total Games</label>
              <label
                class="input"
                name="totalGames"
                readonly
              >{{ leagueSeason.totalGames }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="totalPoints"
              >Total Points</label>
              <label
                class="input"
                name="totalPoints"
                readonly
              >{{ leagueSeason.totalPoints }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="averagePoints"
              >Average Points</label>
              <label
                class="input"
                name="averagePoints"
                readonly
              >{{ leagueSeason.averagePoints }}</label>
            </div>
          </div>
        </div>
        <footer class="card-footer">
          <button
            class="link card-footer-item"
            @click="editLeagueSeason()"
          >
            <!-- For development mode -->
            <font-awesome-icon
              :icon="['fas', 'edit']"
              class="fas"
            />
            <!-- For production or test mode -->
            <!-- <i class="fas fa-edit"></i> -->
            <span>Edit</span>
          </button>
        </footer>
      </div>
      <router-link
        tag="button"
        class="button"
        :to="{ name: 'LeagueSeasonIndex' }"
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
  name: 'LeagueSeasonDetails',
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
    this.leagueSeason = this.getLeagueSeasonById(this.id);
  },
  computed: {
    ...mapGetters(['getLeagueSeasonById']),
  },
  methods: {
    editLeagueSeason() {
      this.$router.push({ name: 'LeagueSeasonEdit' });
    },
  },
};
</script>
