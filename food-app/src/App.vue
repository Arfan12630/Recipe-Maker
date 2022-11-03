<template>
<div>

  <SideBar/>
  <div :style="{'margin-left':sidebarWidth}">
    <router-view/>
  </div>
  </div>
</template>

<script>
import SideBar from './components/SideBar.vue'
import {sidebarWidth} from './components/state'
export default {
  name: 'App',
  components: {
    SideBar
  },
  setup(){
    return {
      sidebarWidth
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
