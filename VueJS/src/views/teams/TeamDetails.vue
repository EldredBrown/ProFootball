<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">Team</h2>
      <div class="card">
        <header class="card-header">
          <p class="card-header-title">Details</p>
        </header>
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="name"
              >Name</label>
              <label
                class="input"
                name="name"
                readonly
              >{{ team.name }}</label>
            </div>
          </div>
        </div>
        <footer class="card-footer">
          <button
            class="link card-footer-item"
            @click="editTeam()"
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
        :to="{ name: 'TeamIndex' }"
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
  name: 'TeamDetails',
  props: {
    id: {
      type: Number,
      default: 0,
    },
  },
  data() {
    return {
      team: {},
    };
  },
  created() {
    this.team = this.getTeamById(this.id);
  },
  computed: {
    ...mapGetters(['getTeamById']),
  },
  methods: {
    editTeam() {
      this.$router.push({ name: 'TeamEdit' });
    },
  },
};
</script>
