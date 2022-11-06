<template>
 <div>
       
  

</div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'TheHome',
  components: {

  }
}
</script>

<style>
body{
  background-image: url('https://png.pngtree.com/thumb_back/fh260/back_our/20190621/ourmid/pngtree-black-meat-western-food-banner-background-image_194600.jpg');
  background-repeat:no-repeat;
  background-size: 110%;
}

body:before,
body:after{
   background-color: rgba(0, 0, 0, 0.5);
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  content: '';
  transition: all 0.3s ease;
  z-index:1;    
  opacity: 0;
  
}

body:hover:before,
body:hover:after{
  transform: scale(1);
  opacity: 1;
}
</style>