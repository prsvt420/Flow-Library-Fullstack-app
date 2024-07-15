<template>
    <footer class="footer">
    <div class="footer-links">

        <a href="https://vk.com/prsvt420">
            <img class="icon" :src="require('../assets/vk_icon.svg')" alt="">
        </a>
        <a href="https://t.me/prsvt420">
            <img class="icon" :src="require('../assets/telegram_icon.svg')" alt="">
        </a>
        <a href="https://github.com/prsvt420">
            <img class="icon" :src="require('../assets/github_icon.svg')" alt="">
        </a>
    </div>
    </footer>
</template>

<script>
export default {
    name: "TheFooter",
}
</script>

<style scoped>
.footer {
    width: 100%;
    height: 80px;
    border-radius: 0 0 20px 20px;
    background: #333;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
}

.footer-links {
    display: flex;
    align-items: center;
}

.icon {
    width: 40px;
    height: 40px;
    margin: 0 10px;
}

</style>