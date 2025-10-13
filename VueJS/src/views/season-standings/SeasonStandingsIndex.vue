<template>
  <div class="content-container">
    <div class="section content-title-group">
      <h2 class="title">Season Standings</h2>
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
      <table class="table is-striped is-hoverable">
        <thead>
          <tr>
            <th>Team</th>
            <th>W</th>
            <th>L</th>
            <th>T</th>
            <th>Pct.</th>
            <th>PF</th>
            <th>PA</th>
            <th>AvgPF</th>
            <th>AvgPA</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="record in seasonStandings"
            :key="record.id"
          >
            <td>{{record.team}}</td>
            <td>{{record.wins}}</td>
            <td>{{record.losses}}</td>
            <td>{{record.ties}}</td>
            <td>{{record.winningPercentage}}</td>
            <td>{{record.pointsFor}}</td>
            <td>{{record.pointsAgainst}}</td>
            <td>{{record.avgPointsFor}}</td>
            <td>{{record.avgPointsAgainst}}</td>
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
import { mapActions, mapState } from 'vuex';

export default {
  name: 'SeasonStandingsIndex',
  data() {
    return {
      message: '',
      selectedYear: 1920,
    };
  },
  async created() {
    await this.loadSeasons();
    await this.loadSeasonStandings();
  },
  computed: {
    ...mapState(['seasons', 'seasonStandings']),
  },
  methods: {
    ...mapActions(['getSeasonsAction', 'getSeasonStandingsAction']),
    async loadSeasons() {
      await this.getSeasonsAction();
    },
    async loadSeasonStandings() {
      this.message = `Getting the team seasons for ${this.selectedYear}, please be patient.`;
      await this.getSeasonStandingsAction(this.selectedYear);
      this.message = '';
    },
    async selectYear() {
      this.selectedYear = parseInt(this.selectedYear);
      await this.loadSeasonStandings();
    },
  },
};
</script>
