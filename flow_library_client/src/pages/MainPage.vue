<template>
  <div class="main-page">
    <h1 class="main-page-title">Flow-Library — читай, учись, программируй.</h1>
    <p class="main-page-description">Это открытая библиотека для изучения программирования. Библиотека предоставляет множество бесплатных книг по программированию абсолютно бесплатно!</p>
    <div class="main-page-info-block">
      <div class="main-page-info-block-items">
        <img src="@/assets/book.svg" class="img" alt="" />
        <p>{{ countBooks.book_count }} книг</p>
      </div>
      <div class="main-page-info-block-items">
        <img src="@/assets/star.svg" class="img" alt="" />
        <p>Бесплатно</p>
      </div>
      <div class="main-page-info-block-items">
        <img src="@/assets/update.svg" class="img" alt="" />
        <p>Постоянные<br>обновления</p>
      </div>
    </div>
    <div class="button-block">
        <button @click="$router.push('/books')" class="main-page-button">Читать</button>
    </div>  
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "MainPage",

  data() {
    return {
      countBooks: 0,
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/api/books/count")
      .then((response) => {
        this.countBooks = response.data;
      })
      .catch((error) => console.log(error));
  },
};
</script>

<style scoped>
.main-page {
  padding: 100px 100px;
  display: flex;
  flex-direction: column;
  min-height: 500px;
  width: 100%;
  font-size: 13px;
  gap: 30px;
}

.main-page-description {
  font-size: 19px;
}

.img {
  width: 45px;
  height: 45px;
}

.main-page-info-block {
  display: flex;
  flex-flow: row wrap;
  justify-content: space-around;
  gap: 20px;
}

.main-page-info-block-items {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.main-page-info-block-items p {
  margin-top: 5px;
  font-size: 20px;
  text-align: center;
}

.button-block {
  display: flex;
  justify-content: center;
}

.main-page-button {
  width: 200px;
  height: 50px;
  border-radius: 10px;
  background: #333;
  color: white;
  font-size: 17px;
  font-weight: bold;
}

.main-page-button:hover {
  cursor: pointer;
  box-shadow:  0 8px 16px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  transition: 0.8s;
}

@media screen and (max-width: 600px) {
  .main-page {
    align-items: center;
    padding: 20px 150px;
  }

  .main-page-info {
    gap: 20px;
  }
}
</style>