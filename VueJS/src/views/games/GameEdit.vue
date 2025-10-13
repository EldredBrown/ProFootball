<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">Game</h2>
      <div class="card">
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
              >{{ game.id }}</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="seasonYear"
              >Season</label>
              <input
                class="input"
                id="seasonYear"
                v-model="game.seasonYear"
                :class="{ invalid: !game.seasonYear }"
              />
            </div>
            <div class="field">
              <label
                class="label"
                for="week"
              >Week</label>
              <input
                class="input"
                id="week"
                v-model="game.week"
                :class="{ invalid: !game.week }"
              />
            </div>
            <div class="field">
              <label
                class="label"
                for="guestName"
              >Guest</label>
              <input
                class="input"
                id="guestName"
                v-model="game.guestName"
                :class="{ invalid: !game.guestName }"
              />
            </div>
            <div class="field">
              <label
                class="label"
                for="guestScore"
              >Guest Score</label>
              <input
                class="input"
                id="guestScore"
                v-model="game.guestScore"
                :class="{ invalid: !game.guestScore }"
              />
            </div>
            <div class="field">
              <label
                class="label"
                for="hostName"
              >Host</label>
              <input
                class="input"
                id="hostName"
                v-model="game.hostName"
                :class="{ invalid: !game.hostName }"
              />
            </div>
            <div class="field">
              <label
                class="label"
                for="hostScore"
              >Host Score</label>
              <input
                class="input"
                id="hostScore"
                v-model="game.hostScore"
                :class="{ invalid: !game.hostScore }"
              />
            </div>
            <div class="field">
              <input
                type="checkbox"
                id="isPlayoff"
                v-model="game.isPlayoff"
              />
              <label for="isPlayoff"> Is Playoff</label>
            </div>
            <div class="field">
              <label
                class="label"
                for="notes"
              >Notes</label>
              <input
                class="input"
                id="notes"
                v-model="game.notes"
              />
            </div>
          </div>
        </div>
      </div>
      <footer class="card-footer">
        <button
          class="link card-footer-item"
          @click="saveGame()"
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
          @click="cancelGame()"
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
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import { cloneDeep } from 'lodash';

export default {
  name: 'GameEdit',
  props: {
    id: {
      type: Number,
      default: 0,
    },
  },
  data() {
    return {
      game: {},
      oldGame: {},
    };
  },
  created() {
    if (this.isAddMode) {
      this.game = {
        id: undefined,
        name: '',
      };
    } else {
      this.game = cloneDeep(this.getGameById(this.id));
      this.oldGame = cloneDeep(this.game);
    }
  },
  computed: {
    ...mapGetters(['getGameById']),
    isAddMode() {
      return !this.id;
    },
    title() {
      return `${this.isAddMode ? 'Add' : 'Edit'}`;
    },
  },
  methods: {
    ...mapActions(['addGameAction', 'updateGameAction']),
    cancelGame() {
      this.$router.push({ name: 'GameIndex' });
    },
    async saveGame() {
      this.validateInput();
      this.game.id
        ? await this.updateGameAction({
            oldGame: this.oldGame,
            newGame: this.game,
          })
        : await this.addGameAction(this.game);
      this.$router.push({ name: 'GameIndex' });
    },
    validateInput() {
      this.game.seasonYear = parseInt(this.game.seasonYear);
      this.game.week = parseInt(this.game.week);
      this.game.guestScore = parseInt(this.game.guestScore);
      this.game.hostScore = parseInt(this.game.hostScore);
    },
  },
};
</script>
