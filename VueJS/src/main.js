import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faVuejs } from '@fortawesome/free-brands-svg-icons'
import { faSync, faBackward, faCheck, faEdit, faPlus, faSave, faTrash, faUndo } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faVuejs, faSync, faBackward, faPlus, faCheck, faEdit, faSave, faTrash, faUndo)
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
