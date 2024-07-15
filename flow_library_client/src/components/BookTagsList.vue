<template>
  <div class="book-tags-list">
    <book-tag :tag="{ name: 'Все' }" @click="callLoadAllBooks"/>
    <book-tag
      v-for="tag in tags"
      :key="tag.id"
      :tag="tag"
    />
  </div>
</template>

<script>
import axios from 'axios';
import BookTag from "./BookTag.vue";

export default {
    name: "BookTagsList",
    components: {
        BookTag
    },
    data() {
        return {
            tags: []
        }
    },
    mounted() {
        this.loadTags()
    },
    methods: {
        loadTags() {
            axios.get('http://192.168.0.104:8000/api/tags/')
            .then(response => {
                this.tags = response.data
            })
            .catch(error => console.log(error))
        },
        callLoadAllBooks() {
            this.$router.push({ name: "Книги" })
        }
    },
}
</script>

<style scoped>
.book-tags-list {
  margin-top: 30px;
  justify-content: flex-start;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  width: 90%;
}

@media screen and (max-width: 600px) {
  .book-tags-list {
    justify-content: center;
  }
}
</style>