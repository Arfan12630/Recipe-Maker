<template>
    <div class="sidebar" :style="{width:sidebarWidth}"> 
        <span
        class="collapse-icon"
        @click="toggleSidebar"
        > 

     <v-icon :path="path"> mdi-chevron-double-left</v-icon>
        </span>

    </div>
</template>


<script>
import {collapsed, toggleSidebar, sidebarWidth} from './state'
import { mdiChevronDoubleLeft } from '@mdi/js';
export default ({
data(){
return{
    path:mdiChevronDoubleLeft
}
},
    props: {},
    setup() {
        return {collapsed, toggleSidebar, sidebarWidth}
    },
})
</script>

<style>
:root{
    --sidebar-bg-color:#2f855a;
    --sidebar-item-hover:#38a169;
    --sidebar-item-active:#276749;
}
</style>
<style scoped>
.sidebar{
    color:white;
    background-color: var(--sidebar-bg-color);
    float:left; 
    position:fixed; 
    z-index:1;
    top:0;
    bottom:0;
    left:0;
    padding:0.5em;
    transition:0.3 ease;
    display:flex; 
    flex-direction:column;

}

.collapse-icon{
    position:absolute;
    bottom:0;
    padding:0.75em;
    color:rgba(255,255,255,0.7);
    transition:0.2s linear;
}

</style>
