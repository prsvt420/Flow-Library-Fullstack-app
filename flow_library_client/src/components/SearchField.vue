<template>
    <input class="search-field" :value="modelValue" @input="$emit('update:modelValue', $event.target.value)" type="text" />
</template>

<script>
export default {
    name: "SearchField",
    props: {
        modelValue: String,
    }
}
</script>

<style scoped>
.search-field {
    width: 90%;
    margin-top: 20px;
    height: 50px;
    border-radius: 10px;
    border: 2px solid black;
    padding: 20px 10px;
    font-size: 20px;
}
</style>