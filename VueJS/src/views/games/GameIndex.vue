<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">Games</h2>
      <button
        class="button refresh-button"
        @click="loadGames()"
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
        :to="{ name: 'GameEdit', params: { id: 0 } }"
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
            <th>Season</th>
            <th>Week</th>
            <th>Guest</th>
            <th>Guest Score</th>
            <th>Host</th>
            <th>Host Score</th>
            <th>Is Playoff?</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="game in games"
            :key="game.id"
          >
            <td>{{game.seasonYear}}</td>
            <td>{{game.week}}</td>
            <td>{{game.guestName}}</td>
            <td>{{game.guestScore}}</td>
            <td>{{game.hostName}}</td>
            <td>{{game.hostScore}}</td>
            <td>{{game.isPlayoff}}</td>
            <td>
              <router-link
                tag="button"
                class="link"
                :to="{ name: 'GameDetails', params: { id: game.id } }"
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
                :to="{ name: 'GameEdit', params: { id: game.id } }"
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
                @click="confirmDelete(game)"
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
        @handleYes="deleteGame"
      >
      </Modal>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';
import Modal from '@/components/Modal';

export default {
  name: 'GameIndex',
  components: {
    Modal,
  },
  data() {
    return {
      gameToDelete: null,
      message: '',
      showModal: false,
    };
  },
  async created() {
    await this.loadGames();
  },
  computed: {
    ...mapState(['games']),
    modalMessage() {
      const seasonYear =
        this.gameToDelete && this.gameToDelete.seasonYear
          ? this.gameToDelete.seasonYear
          : 0;
      const week =
        this.gameToDelete && this.gameToDelete.week
          ? this.gameToDelete.week
          : 0;
      const guestName =
        this.gameToDelete && this.gameToDelete.guestName
          ? this.gameToDelete.guestName
          : '';
      const hostName =
        this.gameToDelete && this.gameToDelete.hostName
          ? this.gameToDelete.hostName
          : '';
      return `
Would you like to delete this game:\n
\t* season = ${seasonYear}
\t* week = ${week}
\t * guest = ${guestName}
\t * host = ${hostName}?
`;
    },
  },
  methods: {
    ...mapActions(['getGamesAction', 'deleteGameAction']),
    closeModal() {
      this.showModal = false;
    },
    confirmDelete(game) {
      this.gameToDelete = game;
      this.showModal = true;
    },
    async deleteGame() {
      this.closeModal();
      if (this.gameToDelete) {
        await this.deleteGameAction(this.gameToDelete);
      }
    },
    async loadGames() {
      this.message = 'Getting the games, please be patient.';
      await this.getGamesAction();
      this.message = '';
    },
  },
};
</script>
