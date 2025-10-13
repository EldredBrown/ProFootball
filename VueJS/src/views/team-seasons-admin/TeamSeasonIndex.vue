<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">Team Seasons</h2>
      <button
        class="button refresh-button"
        @click="loadTeamSeasons()"
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
        :to="{ name: 'TeamSeasonAdminEdit', params: { id: 0 } }"
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
            <th>Team</th>
            <th>Season</th>
            <th>League</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="teamSeason in teamSeasons"
            :key="teamSeason.id"
          >
            <td>{{teamSeason.teamName}}</td>
            <td>{{teamSeason.seasonYear}}</td>
            <td>{{teamSeason.leagueName}}</td>
            <td>
              <router-link
                tag="button"
                class="link"
                :to="{ name: 'TeamSeasonAdminDetails', params: { id: teamSeason.id } }"
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
                :to="{ name: 'TeamSeasonAdminEdit', params: { id: teamSeason.id } }"
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
                @click="confirmDelete(teamSeason)"
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
        @handleYes="deleteTeamSeason"
      >
      </Modal>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';
import Modal from '@/components/Modal';

export default {
  name: 'TeamSeasonIndex',
  components: {
    Modal,
  },
  data() {
    return {
      teamSeasonToDelete: null,
      message: '',
      showModal: false,
    };
  },
  async created() {
    await this.loadTeamSeasons();
  },
  computed: {
    ...mapState(['teamSeasons']),
    modalMessage() {
      const team =
        this.teamSeasonToDelete && this.teamSeasonToDelete.teamName
          ? this.teamSeasonToDelete.teamName
          : '';
      const year =
        this.teamSeasonToDelete && this.teamSeasonToDelete.seasonYear
          ? this.teamSeasonToDelete.seasonYear
          : '';
      return `Would you like to delete ${team} ${year}?`;
    },
  },
  methods: {
    ...mapActions(['getTeamSeasonsAction', 'deleteTeamSeasonAction']),
    closeModal() {
      this.showModal = false;
    },
    confirmDelete(teamSeason) {
      this.teamSeasonToDelete = teamSeason;
      this.showModal = true;
    },
    async deleteTeamSeason() {
      this.closeModal();
      if (this.teamSeasonToDelete) {
        await this.deleteTeamSeasonAction(this.teamSeasonToDelete);
      }
    },
    async loadTeamSeasons() {
      this.message = 'Getting the team seasons, please be patient.';
      await this.getTeamSeasonsAction();
      this.message = '';
    },
  },
};
</script>
