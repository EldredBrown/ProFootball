<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">League</h2>
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
              >{{ league.id }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="longName"
              >Long Name</label>
              <input
                class="input"
                id="longName"
                v-model="league.longName"
                :class="{ invalid: !league.longName }"
              />
            </div>
            <div class="field">
              <label
                class="label"
                for="shortName"
              >Short Name</label>
              <input
                class="input"
                id="shortName"
                v-model="league.shortName"
                :class="{ invalid: !league.shortName }"
              />
            </div>
            <div class="field">
              <label
                class="label"
                for="firstSeasonYear"
              >First Season</label>
              <input
                class="input"
                id="firstSeasonYear"
                v-model="league.firstSeasonYear"
                :class="{ invalid: !league.firstSeasonYear }"
              />
            </div>
            <div class="field">
              <label
                class="label"
                for="lastSeasonYear"
              >Last Season</label>
              <input
                class="input"
                id="lastSeasonYear"
                v-model="league.lastSeasonYear"
              />
            </div>
          </div>
        </div>
        <footer class="card-footer">
          <button
            class="link card-footer-item"
            @click="saveLeague()"
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
            @click="cancelLeague()"
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
  name: 'LeagueEdit',
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
    if (this.isAddMode) {
      this.league = {
        id: undefined,
        longName: '',
        shortName: '',
        firstSeasonYear: 0,
        lastSeasonYear: 0
      };
    } else {
      this.league = cloneDeep(this.getLeagueById(this.id));
    }
  },
  computed: {
    ...mapGetters(['getLeagueById']),
    isAddMode() {
      return !this.id;
    },
    title() {
      return `${this.isAddMode ? 'Add' : 'Edit'}`;
    }
  },
  methods: {
    ...mapActions(['addLeagueAction', 'updateLeagueAction']),
    cancelLeague() {
      this.$router.push({ name: 'LeagueIndex' });
    },
    async saveLeague() {
      this.validateInput();
      this.league.id
        ? await this.updateLeagueAction(this.league)
        : await this.addLeagueAction(this.league);
      this.$router.push({ name: 'LeagueIndex' });
    },
    validateInput() {
      this.league.firstSeasonYear = parseInt(this.league.firstSeasonYear);
      this.league.lastSeasonYear = parseInt(this.league.lastSeasonYear);
    }
  }
};
</script>
