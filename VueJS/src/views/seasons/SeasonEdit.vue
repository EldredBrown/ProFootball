<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">Season</h2>
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
              >{{ season.id }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="year"
              >Year</label>
              <input
                class="input"
                id="year"
                v-model="season.year"
                :class="{ invalid: !season.year }"
              />
            </div>
            <div class="field">
              <label
                class="label"
                for="numOfWeeksScheduled"
              >Weeks Scheduled</label>
              <input
                class="input"
                id="numOfWeeksScheduled"
                v-model="season.numOfWeeksScheduled"
              />
            </div>
            <div class="field">
              <label
                class="label"
                for="numOfWeeksCompleted"
              >Weeks Completed</label>
              <input
                class="input"
                id="numOfWeeksCompleted"
                v-model="season.numOfWeeksCompleted"
              />
            </div>
          </div>
        </div>
        <footer class="card-footer">
          <button
            class="link card-footer-item"
            @click="saveSeason()"
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
            @click="cancelSeason()"
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
  name: 'SeasonEdit',
  props: {
    id: {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      season: {}
    };
  },
  created() {
    if (this.isAddMode) {
      this.season = {
        id: undefined,
        year: 0,
        numOfWeeksScheduled: 0,
        numOfWeeksCompleted: 0
      };
    } else {
      this.season = cloneDeep(this.getSeasonById(this.id));
    }
  },
  computed: {
    ...mapGetters(['getSeasonById']),
    isAddMode() {
      return !this.id;
    },
    title() {
      return `${this.isAddMode ? 'Add' : 'Edit'}`;
    }
  },
  methods: {
    ...mapActions(['addSeasonAction', 'updateSeasonAction']),
    cancelSeason() {
      this.$router.push({ name: 'SeasonIndex' });
    },
    async saveSeason() {
      this.validateInput();
      this.season.id
        ? await this.updateSeasonAction(this.season)
        : await this.addSeasonAction(this.season);
      this.$router.push({ name: 'SeasonIndex' });
    },
    validateInput() {
      this.season.year = parseInt(this.season.year);
      this.season.numOfWeeksScheduled = parseInt(
        this.season.numOfWeeksScheduled
      );
      this.season.numOfWeeksCompleted = parseInt(
        this.season.numOfWeeksCompleted
      );
    }
  }
};
</script>
