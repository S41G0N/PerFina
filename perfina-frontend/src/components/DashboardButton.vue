<template>
  <button
    class="px-8 py-4 bg-white text-blue-400 font-bold text-lg uppercase tracking-wider rounded-xl shadow-md hover:bg-gray-100 hover:shadow-lg transition duration-300 ease-in-out transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-blue-300 focus:ring-opacity-50"
    @click="onClick"
  >
    {{ buttonText }}
  </button>
</template>

<script lang="js" setup>
const props = defineProps({
  buttonText: {
    type: String,
    default: 'Click Me',
  },
  onClick: {
    type: Function,
    default: () => {},
  },
})
</script>
