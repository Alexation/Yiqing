import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'

import { Button, Form, Message, FormItem, Input } from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(Button);
Vue.use(Form);
Vue.use(FormItem);
Vue.use(Input);

Vue.prototype.$message = Message

Vue.config.productionTip = false

Vue.prototype.$axios = axios

new Vue({
  // axios,
  render: h => h(App),
}).$mount('#app')



