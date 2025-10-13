<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">League</h2>
      <div class="card">
        <header class="card-header">
          <p class="card-header-title">Details</p>
        </header>
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="longName"
              >Long Name</label>
              <label
                class="input"
                name="longName"
                readonly
              >{{ league.longName }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="shortName"
              >Short Name</label>
              <label
                class="input"
                name="shortName"
                readonly
              >{{ league.shortName }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="firstSeasonYear"
              >First Season</label>
              <label
                class="input"
                name="firstSeasonYear"
                readonly
              >{{ league.firstSeasonYear }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="lastSeasonYear"
              >Last Season</label>
              <label
                class="input"
                name="lastSeasonYear"
                readonly
              >{{ league.lastSeasonYear }}</label>
            </div>
          </div>
        </div>
        <footer class="card-footer">
          <button
            class="link card-footer-item"
            @click="editLeague()"
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
        :to="{ name: 'LeagueIndex' }"
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
  name: 'LeagueDetails',
  props: {
    id: {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      league: {}
    };
  },
  created() {
    this.league = this.getLeagueById(this.id);
  },
  computed: {
    ...mapGetters(['getLeagueById'])
  },
  methods: {
    editLeague() {
      this.$router.push({ name: 'LeagueEdit' });
    }
  }
};
</script>
