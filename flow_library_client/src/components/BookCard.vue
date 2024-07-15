<template>
  <div class="book-card" @click="$router.push(`/book/${book.id}`)">
    <div class="book-img">
        <img :src="book.image"/>
    </div>
    <p class="book-title"> {{ book.title }}</p>
  </div>
</template>

<script>
export default {
  name: "BookCard",
  props: {
    book: Object,
  },
};
</script>

<style scoped>
.book-card {
  border-radius: 10px;
  margin: 15px;
  width: 220px;
  min-height: 400px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.book-card:hover {
  width: 250px;
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  transition: 0.8s;
  cursor: pointer;
}

@media screen and (max-width: 600px) {
  .book-card:hover {
    width: 290px;
  }
}

@media screen and (max-width: 500px) {
  .book-card:hover {
    width: 270px;
  }
}

@media screen and (max-width: 400px) {
  .book-card:hover {
    width: 250px;
  }
}

@media screen and (max-width: 300px) {
  .book-card:hover {
    width: 230px;
  }
}

.book-title {
  width: 90%;
  margin-bottom: 5px;
  color: black;
  font-size: 14px;
  text-align: left;
}

.book-img {
  width: 200px;
  height: 300px;

}

.book-img img {
  padding: 5px;
  width: 100%;
  height: auto;
  border-radius: 15px;
}
</style>