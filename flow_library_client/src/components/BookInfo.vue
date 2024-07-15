<template>
  <div class="book">
    <div class="book-info">
      <h1 class="book-title">{{ book.title }}</h1>
      <h2>О товаре</h2>
      <div class="book-author field" v-if="book.author">
        <span>Автор{{ book.author.length > 1 ? "ы" : "" }}:</span>
        <div class="book-author-box">
          <template v-for="author in book.author" :key="author.id">
            <p v-if="author.name">{{ author.name }}</p>
          </template>
        </div>
      </div>
      <hr />
      <div class="book-genre field">
        <span>Жанр:</span>
        <p v-if="book.genre">{{ book.genre.name }}</p>
      </div>
      <hr />
      <div class="book-year field">
        <span>Год:</span>
        <p>{{ book.year }}</p>
      </div>
      <hr />
      <div class="book-publisher field">
        <span>Издание:</span>
        <p v-if="book.publisher">{{ book.publisher.name }}</p>
      </div>
      <hr />
      <div class="book-isbn field">
        <span>ISBN:</span>
        <p>{{ book.isbn }}</p>
      </div>
      <hr />
      <div class="book-quantity_pages field">
        <span>Количество страниц:</span>
        <p>{{ book.quantity_pages }}</p>
      </div>
      <hr />
      <div class="book-description">
        <h2>О книге</h2>
        <p>{{ book.description }}</p>
      </div>
    </div>
    <div class="book-block">
      <div class="book-img">
        <img :src="book.image" />
        <a
          v-if="book.file"
          class="book-download-link"
          :href="book.file"
          target="_blank"
          >Скачать книгу</a
        >
      </div>
      <div class="book-tags">
        <book-tag v-for="tag in book.tags" :key="tag.id" :tag="tag" />
      </div>
    </div>
  </div>
</template>

<script>
import BookTag from "./BookTag.vue";

export default {
  name: "BookInfo",
  components: { BookTag },
  props: {
    book: Object,
  },
  watch: {
    book: {
      handler: function () {
        document.title = this.book.title;
      },
      deep: true,
    },
  },
};
</script>

<style scoped>
.book {
  padding: 30px;
  margin: 15px;
  text-align: left;
  display: flex;
  align-items: flex-start;
}

.book-info {
  margin-right: 45px;
  width: 75%;
}

.field {
  display: flex;
  width: 80%;
  justify-content: space-between;
  flex-flow: column, wrap;
}

hr {
  margin: 7px 0;
  width: 80%;
}

h2 {
  font-size: 20px;
  margin: 10px 0;
}

.book-info p,
span {
  font-size: 18px;
}

.book-info span {
  color: DarkSlateGrey;
}

.book-title {
  font-weight: bold;
  font-size: 23px;
  text-align: center;
  margin-bottom: 40px;
}

.book-author-box {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.book-block {
  display: flex;
  flex-direction: column;
  align-items: baseline;
  gap: 30px;
}

.book-tags {
  display: flex;
  justify-content: flex-start;
  flex-wrap: wrap;
  gap: 15px;
  max-width: 300px;
  margin-top: 15px;
}

.book-img {
  width: 300px;
  height: 450px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.book-img img {
  width: 100%;
  height: 100%;
  border: 1px solid black;
  border-radius: 20px;
}

.book-download-link {
  text-decoration: none;
  color: black;
  font-size: 17px;
  font-weight: bold;
}

.book-download-link:hover {
  color: red;
  font-size: 19px;
  transition: 0.8s;
}

@media screen and (max-width: 600px) {
  .book {
    flex-direction: column-reverse;
    align-items: center;
    gap: 25px;
  }

  .book-tags {
    justify-content: center;
  }

  .book-info {
    width: 100%;
    margin: 0;
  }

  .field {
    width: 100%;
  }

  hr {
    width: 100%;
  }

  .book-img {
    margin-bottom: 25px;
  }
}

@media screen and (max-width: 400px) {
  .book-img {
    width: 250px;
    height: 350px;
  }

  .book-title {
    font-size: 20px;
  }

  .book-info p,
  span {
    font-size: 16px;
  }
}

@media screen and (max-width: 300px) {
  .book-img {
    width: 200px;
    height: 300px;
  }

  .book-title {
    font-size: 18px;
  }

  .book-info p,
  span {
    font-size: 14px;
  }
}
</style>