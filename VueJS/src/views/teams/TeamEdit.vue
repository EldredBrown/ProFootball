<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">Team</h2>
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
              >{{ team.id }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="name"
              >Name</label>
              <input
                class="input"
                id="name"
                v-model="team.name"
                :class="{ invalid: !team.name }"
              />
            </div>
          </div>
        </div>
        <footer class="card-footer">
          <button
            class="link card-footer-item"
            @click="saveTeam()"
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
            @click="cancelTeam()"
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
  name: 'TeamEdit',
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
    if (this.isAddMode) {
      this.team = {
        id: undefined,
        name: '',
      };
    } else {
      this.team = cloneDeep(this.getTeamById(this.id));
    }
  },
  computed: {
    ...mapGetters(['getTeamById']),
    isAddMode() {
      return !this.id;
    },
    title() {
      return `${this.isAddMode ? 'Add' : 'Edit'}`;
    },
  },
  methods: {
    ...mapActions(['addTeamAction', 'updateTeamAction']),
    cancelTeam() {
      this.$router.push({ name: 'TeamIndex' });
    },
    async saveTeam() {
      this.validateInput();
      this.team.id
        ? await this.updateTeamAction(this.team)
        : await this.addTeamAction(this.team);
      this.$router.push({ name: 'TeamIndex' });
    },
    validateInput() {},
  },
};
</script>
