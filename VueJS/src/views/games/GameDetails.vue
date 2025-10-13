<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">Game</h2>
      <div class="card">
        <header class="card-header">
          <p class="card-header-title">Details</p>
        </header>
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="seasonYear"
              >Season</label>
              <label
                class="input"
                name="seasonYear"
                readonly
              >{{ game.seasonYear }}</label>
            </div>
          </div>
        </div>
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="week"
              >Week</label>
              <label
                class="input"
                name="week"
                readonly
              >{{ game.week }}</label>
            </div>
          </div>
        </div>
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="guestName"
              >Guest</label>
              <label
                class="input"
                name="guestName"
                readonly
              >{{ game.guestName }}</label>
            </div>
          </div>
        </div>
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="guestScore"
              >Guest Score</label>
              <label
                class="input"
                name="guestScore"
                readonly
              >{{ game.guestScore }}</label>
            </div>
          </div>
        </div>
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="hostName"
              >Host</label>
              <label
                class="input"
                name="hostName"
                readonly
              >{{ game.hostName }}</label>
            </div>
          </div>
        </div>
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="hostScore"
              >Host Score</label>
              <label
                class="input"
                name="hostScore"
                readonly
              >{{ game.hostScore }}</label>
            </div>
          </div>
        </div>
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="winnerName"
              >Winner</label>
              <label
                class="input"
                name="winnerName"
                readonly
              >{{ game.winnerName }}</label>
            </div>
          </div>
        </div>
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="winnerScore"
              >Winner Score</label>
              <label
                class="input"
                name="winnerScore"
                readonly
              >{{ game.winnerScore }}</label>
            </div>
          </div>
        </div>
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="loserName"
              >Loser</label>
              <label
                class="input"
                name="loserName"
                readonly
              >{{ game.loserName }}</label>
            </div>
          </div>
        </div>
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="loserScore"
              >Loser Score</label>
              <label
                class="input"
                name="loserScore"
                readonly
              >{{ game.loserScore }}</label>
            </div>
          </div>
        </div>
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="isPlayoff"
              >Is Playoff?</label>
              <label
                class="input"
                name="isPlayoff"
                readonly
              >{{ game.isPlayoff }}</label>
            </div>
          </div>
        </div>
        <div class="card-content">
          <div class="content">
            <div class="field">
              <label
                class="label"
                for="notes"
              >Notes</label>
              <label
                class="input"
                name="notes"
                readonly
              >{{ game.notes }}</label>
            </div>
          </div>
        </div>
        <footer class="card-footer">
          <button
            class="link card-footer-item"
            @click="editGame()"
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
        :to="{ name: 'GameIndex' }"
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
  name: 'GameDetails',
  props: {
    id: {
      type: Number,
      default: 0,
    },
  },
  data() {
    return {
      game: {},
    };
  },
  created() {
    this.game = this.getGameById(this.id);
  },
  computed: {
    ...mapGetters(['getGameById']),
  },
  methods: {
    editGame() {
      this.$router.push({ name: 'GameEdit' });
    },
  },
};
</script>
