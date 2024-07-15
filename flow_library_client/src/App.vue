<template>
  <the-header/>
    <router-view/>
    <the-footer/>
</template>

<script>
import TheHeader from '@/components/TheHeader.vue';
import TheFooter from '@/components/TheFooter.vue';

export default {
  components: {
    TheHeader,
    TheFooter,
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Roboto Slab';
  background: Ivory;
  display: flex;
  flex-direction: column;
  align-items: center;
}

#app {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: white;
  width: 1100px;
  margin: 20px;
  border-radius: 20px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

@media screen and (max-width: 1200px) {
  #app {
    width: 1000px;
  }
}

@media screen and (max-width: 1024px) {
  #app {
    width: 900px;
  }
}

@media screen and (max-width: 950px) {
  #app {
    width: 800px;
  }
}

@media screen and (max-width: 830px) {
  #app {
    width: 750px;
  }
}

@media screen and (max-width: 760px) {
  #app {
    width: 720px;
  }
}

@media screen and (max-width: 730px) {
  #app {
    width: 700px;
  }
}

@media screen and (max-width: 700px) {
  #app {
    width: 600px;
  }
}

@media screen and (max-width: 600px) {
  #app {
    width: 500px;
  }
}

@media screen and (max-width: 500px) {
  #app {
    width: 390px;
  }
}

@media screen and (max-width: 450px) {
  #app {
    width: 350px;
  }
}

@media screen and (max-width: 350px) {
  #app {
    width: 280px;
  }
}

@media screen and (max-width: 300px) {
  #app {
    width: 250px;
  }
}
</style>