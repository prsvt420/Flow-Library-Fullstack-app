import BooksCardsPage from "@/pages/BooksCardsPage";
import BookInfoPage from "@/pages/BookInfoPage";
import MainPage from "@/pages/MainPage";
import ErrorNotFound from "@/components/ErrorNotFound";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
    { path: "/404", name:'ErrorNotFound', component: ErrorNotFound },
    { path: "/:pathMatch(.*)*", redirect: "/404" },
    {
        path: "/",
        component: MainPage,
        name: "Главная",
    },
    {
        path: "/books",
        component: BooksCardsPage,
        name: "Книги",
    },
    {
        path: "/book/:id",
        component: BookInfoPage,
    },
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL),
})

router.beforeEach((to, from, next) => {
    document.title = to.name;
    next();
  });

export default router;