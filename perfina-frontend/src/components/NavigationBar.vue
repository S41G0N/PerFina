<template>
  <nav class="bg-gradient-to-r from-purple-600 to-indigo-600 shadow-lg">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <div class="flex-shrink-0">
            <img
              class="h-8 w-8"
              src="https://tailwindui.com/img/logos/workflow-mark-indigo-500.svg"
              alt="Logo"
            />
          </div>
          <div class="hidden md:block">
            <div class="ml-10 flex items-baseline space-x-4">
              <router-link
                :to="{ name: 'Home' }"
                class="text-white hover:bg-indigo-500 hover:bg-opacity-75 px-3 py-2 rounded-md text-sm font-medium transition duration-150 ease-in-out"
                >Home</router-link
              >
              <router-link
                :to="{ name: 'Dashboard' }"
                class="text-white hover:bg-indigo-500 hover:bg-opacity-75 px-3 py-2 rounded-md text-sm font-medium transition duration-150 ease-in-out"
                >Dashboard</router-link
              >
            </div>
          </div>
        </div>
        <div class="hidden md:block">
          <div class="ml-4 flex items-center md:ml-6">
            <router-link
              :to="{ name: 'Home' }"
              class="bg-indigo-500 hover:bg-indigo-600 text-white px-4 py-2 rounded-md text-sm font-medium transition duration-150 ease-in-out"
              >Sign In</router-link
            >
          </div>
        </div>
        <div class="-mr-2 flex md:hidden">
          <button
            @click="isOpen = !isOpen"
            type="button"
            class="bg-indigo-600 inline-flex items-center justify-center p-2 rounded-md text-indigo-200 hover:text-white hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-indigo-600 focus:ring-white"
            aria-controls="mobile-menu"
            aria-expanded="false"
          >
            <span class="sr-only">Open main menu</span>
            <svg
              class="block h-6 w-6"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              aria-hidden="true"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              />
            </svg>
            <svg
              class="hidden h-6 w-6"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              aria-hidden="true"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <div class="md:hidden" id="mobile-menu" v-show="isOpen">
      <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
        <router-link
          :to="{ name: 'Home' }"
          class="text-white hover:bg-indigo-500 hover:bg-opacity-75 block px-3 py-2 rounded-md text-base font-medium"
          >Home</router-link
        >
        <router-link
          :to="{ name: 'Dashboard' }"
          class="text-white hover:bg-indigo-500 hover:bg-opacity-75 block px-3 py-2 rounded-md text-base font-medium"
          >Dashboard</router-link
        >
        <router-link
          :to="{ name: 'Home' }"
          class="bg-indigo-500 text-white block px-3 py-2 rounded-md text-base font-medium"
          >Sign In</router-link
        >
      </div>
    </div>
  </nav>
</template>

<script lang="js" setup>
import { ref } from 'vue'
const isOpen = ref(false)
</script>
