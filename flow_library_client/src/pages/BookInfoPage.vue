<template>
  <book-info :book="book" v-if="book"/>
  <error-not-found v-else/>
</template>

<script>
import axios from "axios";
import BookInfo from '@/components/BookInfo.vue';
import ErrorNotFound from '@/components/ErrorNotFound.vue';

export default {
  components: { BookInfo, ErrorNotFound },
  name: "BookInfoPage",
  data() {
    return {
      book: {},
    };
  },
  mounted() {
    axios
      .get(`http://192.168.0.104:8000/api/books/${this.$route.params.id}`)
      .then((response) => {
        this.book = response.data;
      })
      .catch(() => {
        this.book = false;
      });
  },
};
</script>

<style scoped>

</style>