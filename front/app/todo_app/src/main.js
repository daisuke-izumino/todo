import { createApp } from 'vue'
import App from './App.vue'
import AxiosPlugin from '../plugins/axios.js'
import axios from 'axios'
import VueAxios from 'vue-axios'


createApp(App).use(VueAxios, axios).use(AxiosPlugin).mount('#app')