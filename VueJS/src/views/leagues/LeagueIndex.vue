<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">Leagues</h2>
      <button
        class="button refresh-button"
        @click="loadLeagues()"
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
        :to="{ name: 'LeagueEdit', params: { id: 0 } }"
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
            <th>Long Name</th>
            <th>Short Name</th>
            <th>First Season</th>
            <th>Last Season</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="league in leagues"
            :key="league.id"
          >
            <td>{{league.longName}}</td>
            <td>{{league.shortName}}</td>
            <td>{{league.firstSeasonYear}}</td>
            <td>{{league.lastSeasonYear}}</td>
            <td>
              <router-link
                tag="button"
                class="link"
                :to="{ name: 'LeagueDetails', params: { id: league.id } }"
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
                :to="{ name: 'LeagueEdit', params: { id: league.id } }"
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
                @click="confirmDelete(league)"
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
        @handleYes="deleteLeague"
      >
      </Modal>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';
import Modal from '@/components/Modal';

export default {
  name: 'LeagueIndex',
  components: {
    Modal
  },
  data() {
    return {
      leagueToDelete: null,
      message: '',
      showModal: false
    };
  },
  async created() {
    await this.loadLeagues();
  },
  computed: {
    ...mapState(['leagues']),
    modalMessage() {
      const shortName =
        this.leagueToDelete && this.leagueToDelete.shortName
          ? this.leagueToDelete.shortName
          : '';
      return `Would you like to delete ${shortName}?`;
    }
  },
  methods: {
    ...mapActions(['getLeaguesAction', 'deleteLeagueAction']),
    closeModal() {
      this.showModal = false;
    },
    confirmDelete(league) {
      this.leagueToDelete = league;
      this.showModal = true;
    },
    async deleteLeague() {
      this.closeModal();
      if (this.leagueToDelete) {
        await this.deleteLeagueAction(this.leagueToDelete);
      }
    },
    async loadLeagues() {
      this.message = 'Getting the leagues, please be patient.';
      await this.getLeaguesAction();
      this.message = '';
    }
  }
};
</script>
