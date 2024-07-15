<template>
  <p
    @click="callLoadBooks"
    @mouseover="hoverTag"
    class="book-tag"
    :class="{
      'current-tag':
        (Boolean(!$route.query.tag) && tag.name === 'Все') ||
        tag.name === $route.query.tag,
    }"
  >
    {{ tag.name }}
  </p>
</template>

<script>
import router from "@/router/router";
export default {
  name: "BookTag",
  props: {
    tag: Object,
  },
  methods: {
    callLoadBooks() {
      router.push({ name: "Книги", query: { tag: this.tag.name } });
    },
  },
};
</script>

<style scoped>
.book-tag {
  border: 2px solid black;
  border-radius: 10px;
  padding: 5px 10px;
  font-size: 15px;
}

.book-tag:hover {
  cursor: pointer;
  background: #dedede;
  transition: 0.3s;
}

.current-tag {
  background: #c6c5c5;
}
</style>