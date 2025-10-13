<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">Team Season</h2>
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
              >{{ teamSeason.id }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="teamName"
              >Team</label>
              <input
                class="input"
                id="teamName"
                v-model="teamSeason.teamName"
                :class="{ invalid: !teamSeason.teamName }"
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
                v-model="teamSeason.seasonYear"
                :class="{ invalid: !teamSeason.seasonYear }"
              />
            </div>
            <div class="field">
              <label
                class="label"
                for="leagueName"
              >League</label>
              <input
                class="input"
                id="leagueName"
                v-model="teamSeason.leagueName"
              />
            </div>
          </div>
        </div>
        <footer class="card-footer">
          <button
            class="link card-footer-item"
            @click="saveTeamSeason()"
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
            @click="cancelTeamSeason()"
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
  name: 'TeamSeasonEdit',
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
    if (this.isAddMode) {
      this.teamSeason = {
        id: undefined,
        teamName: '',
        seasonYear: 0,
        leagueName: '',
      };
    } else {
      this.teamSeason = cloneDeep(this.getTeamSeasonById(this.id));
    }
  },
  computed: {
    ...mapGetters(['getTeamSeasonById']),
    isAddMode() {
      return !this.id;
    },
    title() {
      return `${this.isAddMode ? 'Add' : 'Edit'}`;
    },
  },
  methods: {
    ...mapActions(['addTeamSeasonAction', 'updateTeamSeasonAction']),
    cancelTeamSeason() {
      this.$router.push({ name: 'TeamSeasonAdminIndex' });
    },
    async saveTeamSeason() {
      this.validateInput();
      this.teamSeason.id
        ? await this.updateTeamSeasonAction(this.teamSeason)
        : await this.addTeamSeasonAction(this.teamSeason);
      this.$router.push({ name: 'TeamSeasonAdminIndex' });
    },
    validateInput() {
      this.teamSeason.seasonYear = parseInt(this.teamSeason.seasonYear);
    },
  },
};
</script>
