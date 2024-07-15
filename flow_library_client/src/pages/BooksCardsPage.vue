<template>
  <search-field v-model="searchQuery" :placeholder="'Поиск' + (currentTag ? ` в ${currentTag}...` : '...')" />
  <book-tags-list />
  <book-cards :books="filteredBooksBySearchQuery" v-if="filteredBooksBySearchQuery.length" />
  <the-loading v-else />
  <div ref="observer" class="observer"></div>
</template>

<script>
import BookCards from "@/components/BookCards.vue";
import axios from "axios";
import TheLoading from "@/components/TheLoading.vue";
import BookTagsList from "@/components/BookTagsList.vue";
import SearchField from "@/components/SearchField.vue";

export default {
  name: "BooksCardsPage",
  components: {
    BookCards,
    TheLoading,
    BookTagsList,
    SearchField,
  },

  data() {
    return {
      books: [],
      searchQuery: "",
      currentPage: 1,
      isNextPage: null,
      currentTag: this.$route.query.tag || "",
    };
  },

  mounted() {
    this.setupIntersectionObserver();
  },

  created() {
    this.loadBooks();
  },

  watch: {
    "$route.query.tag": "handleTagChange",
    searchQuery: "handleSearchQueryChange",
  },

  methods: {
    setupIntersectionObserver() {
      const options = {
        rootMargin: "0px",
        threshold: 1.0,
      };
      const callback = (entries) => {
        if (entries[0].isIntersecting && this.isNextPage) {
          this.currentPage += 1;
          this.loadBooks();
        }
      };
      const observer = new IntersectionObserver(callback, options);
      observer.observe(this.$refs.observer);
    },

    handleTagChange(tagName) {
      this.books = [];
      this.currentTag = tagName;
      this.currentPage = 1;
      this.loadBooks();
    },

    handleSearchQueryChange() {
      this.currentPage = 1;
      this.loadBooks();
    },

    loadBooks() {
      let url = `http://192.168.0.104:8000/api/books/?page=${this.currentPage}`;

      if (this.currentTag) {
        url += `&tag=${this.currentTag}`;
      }

      axios
        .get(url)
        .then((response) => {
          this.books = this.currentPage === 1 ? response.data.results : [...this.books, ...response.data.results];
          this.isNextPage = response.data.next;
        })
        .catch((error) => console.log(error));
    },
  },

  computed: {
    filteredBooksBySearchQuery() {
      return this.books.filter((book) =>
        book.title.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
  },
};
</script>

<style scoped>
.observer {
  height: 1px;
}
</style>