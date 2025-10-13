<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">Teams</h2>
      <button
        class="button refresh-button"
        @click="loadTeams()"
      >
        <!-- For development mode -->
        <font-awesome-icon
          :icon="['fas', 'sync']"
          class="fas"
        />
        <!-- For production or test mode -->
        <!-- <i class="fas fa-sync"></i> -->
      </button>
      <router-link
        tag="button"
        class="button add-button"
        :to="{ name: 'TeamEdit', params: { id: 0 } }"
      >
        <!-- For development mode -->
        <font-awesome-icon
          :icon="['fas', 'plus']"
          class="fas"
        />
        <!-- For production or test mode -->
        <!-- <i class="fas fa-plus"></i> -->
        <span>Create New</span>
      </router-link>
      <table class="table is-striped is-hoverable">
        <thead>
          <tr>
            <th>Name</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="team in teams"
            :key="team.id"
          >
            <td>{{team.name}}</td>
            <td>
              <router-link
                tag="button"
                class="link"
                :to="{ name: 'TeamDetails', params: { id: team.id } }"
              >
                <!-- For development mode -->
                <font-awesome-icon
                  :icon="['fas', 'check']"
                  class="fas"
                />
                <!-- For production or test mode -->
                <!-- <i class="fas fa-check"></i> -->
                <span>Details</span>
              </router-link>
              <router-link
                tag="button"
                class="link"
                :to="{ name: 'TeamEdit', params: { id: team.id } }"
              >
                <!-- For development mode -->
                <font-awesome-icon
                  :icon="['fas', 'edit']"
                  class="fas"
                />
                <!-- For production or test mode -->
                <!-- <i class="fas fa-edit"></i> -->
                <span>Edit</span>
              </router-link>
              <button
                class="link"
                @click="confirmDelete(team)"
              >
                <!-- For development mode -->
                <font-awesome-icon
                  :icon="['fas', 'trash']"
                  class="fas"
                />
                <!-- For production or test mode -->
                <i class="fas fa-trash"></i>
                <span>Delete</span>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <div
        class="notification is-info"
        v-show="message"
      >{{ message }}</div>
      <Modal
        :message="modalMessage"
        :isOpen="showModal"
        @handleNo="closeModal"
        @handleYes="deleteTeam"
      >
      </Modal>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';
import Modal from '@/components/Modal';

export default {
  name: 'TeamIndex',
  components: {
    Modal,
  },
  data() {
    return {
      teamToDelete: null,
      message: '',
      showModal: false,
    };
  },
  async created() {
    await this.loadTeams();
  },
  computed: {
    ...mapState(['teams']),
    modalMessage() {
      const name =
        this.teamToDelete && this.teamToDelete.name
          ? this.teamToDelete.name
          : '';
      return `Would you like to delete ${name}?`;
    },
  },
  methods: {
    ...mapActions(['getTeamsAction', 'deleteTeamAction']),
    closeModal() {
      this.showModal = false;
    },
    confirmDelete(team) {
      this.teamToDelete = team;
      this.showModal = true;
    },
    async deleteTeam() {
      this.closeModal();
      if (this.teamToDelete) {
        await this.deleteTeamAction(this.teamToDelete);
      }
    },
    async loadTeams() {
      this.message = 'Getting the teams, please be patient.';
      await this.getTeamsAction();
      this.message = '';
    },
  },
};
</script>
