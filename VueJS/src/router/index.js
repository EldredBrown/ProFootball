import Vue from 'vue';
import VueRouter from 'vue-router';
import PageNotFound from '@/views/PageNotFound';

Vue.use(VueRouter)

const parseProps = r => ({ id: parseInt(r.params.id) });

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: "bundle.home" */ '../views/Home'),
  },
  {
    path: '/games/index',
    name: 'GameIndex',
    component: () => import(/* webpackChunkName: "bundle.games" */ '../views/games/GameIndex'),
  },
  {
    path: '/games/details/:id',
    name: 'GameDetails',
    component: () => import(/* webpackChunkName: "bundle.games" */ '../views/games/GameDetails'),
    props: parseProps,
  },
  {
    path: '/games/edit/:id',
    name: 'GameEdit',
    component: () => import(/* webpackChunkName: "bundle.games" */ '../views/games/GameEdit'),
    props: parseProps,
  },
  {
    path: '/game-predictor/predict-game',
    name: 'PredictGame',
    component: () => import(
      /* webpackChunkName: "bundle.game-predictor" */ '../views/game-predictor/PredictGame'
    ),
    props: parseProps,
  },
  {
    path: '/leagues/index',
    name: 'LeagueIndex',
    component: () => import(/* webpackChunkName: "bundle.leagues" */ '../views/leagues/LeagueIndex'),
  },
  {
    path: '/leagues/details/:id',
    name: 'LeagueDetails',
    component: () => import(/* webpackChunkName: "bundle.leagues" */ '../views/leagues/LeagueDetails'),
    props: parseProps,
  },
  {
    path: '/leagues/edit/:id',
    name: 'LeagueEdit',
    component: () => import(/* webpackChunkName: "bundle.leagues" */ '../views/leagues/LeagueEdit'),
    props: parseProps,
  },
  {
    path: '/league-seasons/index',
    name: 'LeagueSeasonIndex',
    component: () => import(/* webpackChunkName: "bundle.league-seasons" */ '../views/league-seasons/LeagueSeasonIndex'),
  },
  {
    path: '/league-seasons/details/:id',
    name: 'LeagueSeasonDetails',
    component: () => import(/* webpackChunkName: "bundle.league-seasons" */ '../views/league-seasons/LeagueSeasonDetails'),
    props: parseProps,
  },
  {
    path: '/league-seasons/edit/:id',
    name: 'LeagueSeasonEdit',
    component: () => import(/* webpackChunkName: "bundle.league-seasons" */ '../views/league-seasons/LeagueSeasonEdit'),
    props: parseProps,
  },
  {
    path: '/seasons/index',
    name: 'SeasonIndex',
    component: () => import(/* webpackChunkName: "bundle.seasons" */ '../views/seasons/SeasonIndex'),
  },
  {
    path: '/seasons/details/:id',
    name: 'SeasonDetails',
    component: () => import(/* webpackChunkName: "bundle.seasons" */ '../views/seasons/SeasonDetails'),
    props: parseProps,
  },
  {
    path: '/seasons/edit/:id',
    name: 'SeasonEdit',
    component: () => import(/* webpackChunkName: "bundle.seasons" */ '../views/seasons/SeasonEdit'),
    props: parseProps,
  },
  {
    path: '/season-standings/index',
    name: 'SeasonStandingsIndex',
    component: () => import(/* webpackChunkName: "bundle.season-standings" */ '../views/season-standings/SeasonStandingsIndex'),
  },
  {
    path: '/teams/index',
    name: 'TeamIndex',
    component: () => import(/* webpackChunkName: "bundle.teams" */ '../views/teams/TeamIndex'),
  },
  {
    path: '/teams/details/:id',
    name: 'TeamDetails',
    component: () => import(/* webpackChunkName: "bundle.teams" */ '../views/teams/TeamDetails'),
    props: parseProps,
  },
  {
    path: '/teams/edit/:id',
    name: 'TeamEdit',
    component: () => import(/* webpackChunkName: "bundle.teams" */ '../views/teams/TeamEdit'),
    props: parseProps,
  },
  {
    path: '/team-seasons-admin/index',
    name: 'TeamSeasonAdminIndex',
    component: () => import(/* webpackChunkName: "bundle.team-seasons-admin" */ '../views/team-seasons-admin/TeamSeasonIndex'),
  },
  {
    path: '/team-seasons-admin/details/:id',
    name: 'TeamSeasonAdminDetails',
    component: () => import(/* webpackChunkName: "bundle.team-seasons-admin" */ '../views/team-seasons-admin/TeamSeasonDetails'),
    props: parseProps,
  },
  {
    path: '/team-seasons-admin/edit/:id',
    name: 'TeamSeasonAdminEdit',
    component: () => import(/* webpackChunkName: "bundle.team-seasons-admin" */ '../views/team-seasons-admin/TeamSeasonEdit'),
    props: parseProps,
  },
  {
    path: '/team-seasons/index',
    name: 'TeamSeasonIndex',
    component: () => import(/* webpackChunkName: "bundle.team-seasons" */ '../views/team-seasons/TeamSeasonIndex'),
  },
  {
    path: '/team-seasons/details/:id',
    name: 'TeamSeasonDetails',
    component: () => import(/* webpackChunkName: "bundle.team-seasons" */ '../views/team-seasons/TeamSeasonDetails'),
    props: parseProps,
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "bundle.about" */ '../views/About'),
  },
  {
    path: '*',
    component: PageNotFound,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

export default router
