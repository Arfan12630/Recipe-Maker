<template>
<div>
   <input placeholder="Enter food " class="searchbar"/> 
  
  </div>
</template>

<script>
import { collapsed, toggleSidebar } from '../components/state'
export default {
  setup() {
    return { collapsed, toggleSidebar }
  }
}
</script>

<style scoped>
.searchbar{
    width:1200px;
    display: "flex";
    flex-direction: "column";
    justify-content: "center";
    align-items: "center";
    text-align:"center";
    margin-left: 10px;
    margin-top: -10px;
    border-radius:10px 0 15px 0;
    padding: 10px 20px;
    color:black;
}
</style>