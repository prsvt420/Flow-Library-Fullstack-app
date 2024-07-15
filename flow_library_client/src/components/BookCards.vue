<template>
  <div class="book-cards">
    <book-card v-for="book in books" :key="book.id" :book="book"/>
  </div>
</template>

<script>
import BookCard from './BookCard.vue';

export default {
  name: "BookCards",
  components: { BookCard },
  props: {
    books: Array,
  },
};
</script>

<style scoped>
.book-cards {
  justify-items: center;
  justify-content: center;
  padding: 30px;
  width: 100%;
  display: grid;
  grid-template-columns: repeat(4, minmax(200px, 1fr));
}

@media screen and (max-width: 1200px) {
  .book-cards {
    grid-template-columns: repeat(3, minmax(200px, 1fr));
    width: 900px;
  }
}

@media screen and (max-width: 1024px) {
  .book-cards {
    grid-template-columns: repeat(3, minmax(200px, 1fr));
    width: 900px;
  }
}

@media screen and (max-width: 950px) {
  .book-cards {
    grid-template-columns: repeat(3, minmax(200px, 1fr));
    width: 800px;
  }
}

@media screen and (max-width: 830px) {
  .book-cards {
    grid-template-columns: repeat(2, minmax(200px, 1fr));
    width: 750px;
  }
}

@media screen and (max-width: 760px) {
  .book-cards {
    grid-template-columns: repeat(2, minmax(200px, 1fr));
    width: 720px;
  }
}

@media screen and (max-width: 730px) {
  .book-cards {
    grid-template-columns: repeat(2, minmax(200px, 1fr));
    width: 700px;
  }
}

@media screen and (max-width: 700px) {
  .book-cards {
    grid-template-columns: repeat(2, minmax(200px, 1fr));
    width: 600px;
  }
}

@media screen and (max-width: 600px) {
  .book-cards {
    grid-template-columns: repeat(1, minmax(200px, 1fr));
    width: 500px;
  }
}

@media screen and (max-width: 500px) {
  .book-cards {
    grid-template-columns: repeat(1, minmax(200px, 1fr));
    width: 350px;
  }
}

@media screen and (max-width: 450px) {
  .book-cards {
    grid-template-columns: repeat(1, minmax(200px, 1fr));
    width: 350px;
  }
}

@media screen and (max-width: 350px) {
  .book-cards {
    width: 280px;
  }
}

@media screen and (max-width: 300px) {
  .book-cards {
    width: 250px;
  }
}

</style>