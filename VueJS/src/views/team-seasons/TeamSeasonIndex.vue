<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">Team Seasons</h2>
      <form>
        <div>
          <label>Season </label>
          <select
            id="year"
            v-model="selectedYear"
            @change="selectYear()"
          >
            <option
              v-for="season in seasons"
              :key="season.id"
            >{{season.year}}</option>
          </select>
        </div>
        <p>
          <button
            class="btn btn-primary btn-lg"
            id="run-weekly-update"
            @click="runWeeklyUpdate()"
          >Run Weekly Update</button>
        </p>
      </form>
      <table class="table is-striped is-hoverable">
        <thead>
          <tr>
            <th>Name</th>
            <th>W</th>
            <th>L</th>
            <th>T</th>
            <th>Pct</th>
            <th>PF</th>
            <th>PA</th>
            <th>PythW</th>
            <th>PythL</th>
            <th>OA</th>
            <th>OF</th>
            <th>OI</th>
            <th>DA</th>
            <th>DF</th>
            <th>DI</th>
            <th>FinPythPct</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="teamSeason in teamSeasonsByYear"
            :key="teamSeason.id"
          >
            <td>{{teamSeason.teamName}}</td>
            <td>{{teamSeason.wins}}</td>
            <td>{{teamSeason.losses}}</td>
            <td>{{teamSeason.ties}}</td>
            <td>{{teamSeason.winningPercentage}}</td>
            <td>{{teamSeason.pointsFor}}</td>
            <td>{{teamSeason.pointsAgainst}}</td>
            <td>{{teamSeason.pythagoreanWins}}</td>
            <td>{{teamSeason.pythagoreanLosses}}</td>
            <td>{{teamSeason.offensiveAverage}}</td>
            <td>{{teamSeason.offensiveFactor}}</td>
            <td>{{teamSeason.offensiveIndex}}</td>
            <td>{{teamSeason.defensiveAverage}}</td>
            <td>{{teamSeason.defensiveFactor}}</td>
            <td>{{teamSeason.defensiveIndex}}</td>
            <td>{{teamSeason.finalPythagoreanWinningPercentage}}</td>
            <td>
              <router-link
                tag="button"
                class="link"
                :to="{ name: 'TeamSeasonDetails', params: { id: teamSeason.id } }"
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
            </td>
          </tr>
        </tbody>
      </table>
      <div
        class="notification is-info"
        v-show="message"
      >{{ message }}</div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapState } from 'vuex';

export default {
  name: 'TeamSeasonIndex',
  data() {
    return {
      message: '',
      selectedYear: 1920,
      teamSeasonsByYear: [],
    };
  },
  async created() {
    await this.loadSeasons();
    await this.loadTeamSeasons();
  },
  computed: {
    ...mapState(['seasons', 'teamSeasons']),
    ...mapGetters(['getTeamSeasonsByYear']),
  },
  methods: {
    ...mapActions(['getSeasonsAction', 'getTeamSeasonsAction']),
    async loadSeasons() {
      await this.getSeasonsAction();
    },
    async loadTeamSeasons() {
      this.message = `Getting the team seasons for ${this.selectedYear}, please be patient.`;

      await this.getTeamSeasonsAction();

      this.teamSeasonsByYear = [
        ...this.getTeamSeasonsByYear(this.selectedYear),
      ];

      this.message = '';
    },
    runWeeklyUpdate() {
      console.log('Running weekly update');

      // TODO: Implement the logic for running a weekly update.
    },
    async selectYear() {
      this.selectedYear = parseInt(this.selectedYear);
      await this.loadTeamSeasons();
    },
  },
};
</script>
