<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">Season</h2>
      <div class="card">
        <header class="card-header">
          <p class="card-header-title">Details</p>
        </header>
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="year"
              >Year</label>
              <label
                class="input"
                name="year"
                readonly
              >{{ season.year }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="numOfWeeksScheduled"
              >Weeks Scheduled</label>
              <label
                class="input"
                name="numOfWeeksScheduled"
                readonly
              >{{ season.numOfWeeksScheduled }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="numOfWeeksCompleted"
              >Weeks Completed</label>
              <label
                class="input"
                name="numOfWeeksCompleted"
                readonly
              >{{ season.numOfWeeksCompleted }}</label>
            </div>
          </div>
        </div>
        <footer class="card-footer">
          <button
            class="link card-footer-item"
            @click="editSeason()"
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
        :to="{ name: 'SeasonIndex' }"
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
  name: 'SeasonDetails',
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
    this.season = this.getSeasonById(this.id);
  },
  computed: {
    ...mapGetters(['getSeasonById'])
  },
  methods: {
    editSeason() {
      this.$router.push({ name: 'SeasonEdit' });
    }
  }
};
</script>
