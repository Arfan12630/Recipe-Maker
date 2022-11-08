<template>
  <main id>
    <section class="products">
      <ProductPlacer
        v-for="product in products"
        :key="product.color"
        :product="product"
      />
    </section>
  </main>
</template>

<script>
import ProductPlacer from './ProductPlacer.vue'
export default {
  name: 'app',
  components: {
    ProductPlacer
  },
  data () {
    return {
      products: [
        {
          title: 'Nike Air Max',
          color: 'green',
          bgtext: 'NIKE',
          
        },
        {
          title: 'Nike flex',
          color: 'blue',
          bgtext: 'AIR',
          
        }
       
      ]
    }
  }
}
</script>

<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  body {
    font-family: 'montseratt', sans-serif;
  }
  main {
    width: 100vw;
    min-height: 100vh; 
    overflow: hidden;
    background-color: #EEE;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .products {
    display: flex;
    max-width: 850px;
    padding: 25px;
   
  }
</style>