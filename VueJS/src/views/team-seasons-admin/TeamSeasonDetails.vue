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
                for="leagueName"
              >League</label>
              <label
                class="input"
                name="leagueName"
                readonly
              >{{ teamSeason.leagueName }}</label>
            </div>
          </div>
        </div>
        <footer class="card-footer">
          <button
            class="link card-footer-item"
            @click="editTeamSeason()"
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
        :to="{ name: 'TeamSeasonAdminIndex' }"
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
  methods: {
    editTeamSeason() {
      this.$router.push({ name: 'TeamSeasonAdminEdit' });
    },
  },
};
</script>
