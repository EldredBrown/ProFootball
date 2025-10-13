<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">League Seasons</h2>
      <button
        class="button refresh-button"
        @click="loadLeagueSeasons()"
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
        :to="{ name: 'LeagueSeasonEdit', params: { id: 0 } }"
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
            <th>League</th>
            <th>Season</th>
            <th>G</th>
            <th>PF</th>
            <th>AvgPF</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="leagueSeason in leagueSeasons"
            :key="leagueSeason.id"
          >
            <td>{{leagueSeason.leagueName}}</td>
            <td>{{leagueSeason.seasonYear}}</td>
            <td>{{leagueSeason.totalGames}}</td>
            <td>{{leagueSeason.totalPoints}}</td>
            <td>{{leagueSeason.averagePoints}}</td>
            <td>
              <router-link
                tag="button"
                class="link"
                :to="{ name: 'LeagueSeasonDetails', params: { id: leagueSeason.id } }"
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
                :to="{ name: 'LeagueSeasonEdit', params: { id: leagueSeason.id } }"
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
                @click="confirmDelete(leagueSeason)"
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
        @handleYes="deleteLeagueSeason"
      >
      </Modal>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';
import Modal from '@/components/Modal';

export default {
  name: 'LeagueSeasonIndex',
  components: {
    Modal,
  },
  data() {
    return {
      leagueSeasonToDelete: null,
      message: '',
      showModal: false,
    };
  },
  async created() {
    await this.loadLeagueSeasons();
  },
  computed: {
    ...mapState(['leagueSeasons']),
    modalMessage() {
      const league =
        this.leagueSeasonToDelete && this.leagueSeasonToDelete.leagueName
          ? this.leagueSeasonToDelete.leagueName
          : '';
      const year =
        this.leagueSeasonToDelete && this.leagueSeasonToDelete.seasonYear
          ? this.leagueSeasonToDelete.seasonYear
          : '';
      return `Would you like to delete ${league} ${year}?`;
    },
  },
  methods: {
    ...mapActions(['getLeagueSeasonsAction', 'deleteLeagueSeasonAction']),
    closeModal() {
      this.showModal = false;
    },
    confirmDelete(leagueSeason) {
      this.leagueSeasonToDelete = leagueSeason;
      this.showModal = true;
    },
    async deleteLeagueSeason() {
      this.closeModal();
      if (this.leagueSeasonToDelete) {
        await this.deleteLeagueSeasonAction(this.leagueSeasonToDelete);
      }
    },
    async loadLeagueSeasons() {
      this.message = 'Getting the league seasons, please be patient.';
      await this.getLeagueSeasonsAction();
      this.message = '';
    },
  },
};
</script>
