<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">Seasons</h2>
      <button
        class="button refresh-button"
        @click="loadSeasons()"
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
        :to="{ name: 'SeasonEdit', params: { id: 0 } }"
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
            <th>Year</th>
            <th>Weeks Scheduled</th>
            <th>Weeks Completed</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="season in seasons"
            :key="season.id"
          >
            <td>{{season.year}}</td>
            <td>{{season.numOfWeeksScheduled}}</td>
            <td>{{season.numOfWeeksCompleted}}</td>
            <td>
              <router-link
                tag="button"
                class="link"
                :to="{ name: 'SeasonDetails', params: { id: season.id } }"
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
                :to="{ name: 'SeasonEdit', params: { id: season.id } }"
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
                @click="confirmDelete(season)"
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
        @handleYes="deleteSeason"
      >
      </Modal>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';
import Modal from '@/components/Modal';

export default {
  name: 'SeasonIndex',
  components: {
    Modal,
  },
  data() {
    return {
      seasonToDelete: null,
      message: '',
      showModal: false,
    };
  },
  async created() {
    await this.loadSeasons();
  },
  computed: {
    ...mapState(['seasons']),
    modalMessage() {
      const year =
        this.seasonToDelete && this.seasonToDelete.year
          ? this.seasonToDelete.year
          : '';
      return `Would you like to delete ${year}?`;
    },
  },
  methods: {
    ...mapActions(['getSeasonsAction', 'deleteSeasonAction']),
    closeModal() {
      this.showModal = false;
    },
    confirmDelete(season) {
      this.seasonToDelete = season;
      this.showModal = true;
    },
    async deleteSeason() {
      this.closeModal();
      if (this.seasonToDelete) {
        await this.deleteSeasonAction(this.seasonToDelete);
      }
    },
    async loadSeasons() {
      this.message = 'Getting the seasons, please be patient.';
      await this.getSeasonsAction();
      this.message = '';
    },
  },
};
</script>
