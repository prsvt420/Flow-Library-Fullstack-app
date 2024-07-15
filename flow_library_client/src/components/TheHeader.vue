<template>
  <header class="header">
    <a class="header-title" @click="$router.push(`/`)">Flow-Library</a>
  </header>
</template>

<script>
export default {
  name: "TheHeader",
};
</script>

<style scoped>
.header {
  width: 100%;
  height: 80px;
  border-radius: 20px 20px 0 0;
  background: #333;
  display: flex;
  justify-content: center;
  align-items: center;
}

.header-title {
  font-size: 30px;
  color: white;
  text-decoration: none;
}

.header-title:hover {
  cursor: pointer;
  color: #ccc;
  transition: 0.8s;
  font-size: 32px;
}
</style>