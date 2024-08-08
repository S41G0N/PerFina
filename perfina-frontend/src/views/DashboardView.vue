<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Dashboard page</h1>
    <div class="grid grid-cols-2 gap-4">
      <!-- Left half (empty) -->
      <div></div>
      <!-- Right half with buttons in a 2x2 grid -->
      <div class="grid grid-cols-2 gap-4">
        <DashboardButton
          v-for="button in buttons"
          :key="button.id"
          :button-text="button.text"
          :on-click="button.action"
        />
      </div>
    </div>
    <!-- Invoice Form Modal -->
    <InvoiceForm v-if="showInvoiceForm" @close="closeInvoiceForm" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import DashboardButton from '@/components/DashboardButton.vue'
import InvoiceForm from '@/components/InvoiceForm.vue'

const showInvoiceForm = ref(false)

const generateInvoice = () => {
  console.log('Generating a new invoice')
  showInvoiceForm.value = true
  // Generate receipt logic here
}

const addCompany = () => {
  console.log('Adding a company')
  // Add company logic here
}

const addClient = () => {
  console.log('Adding a client')
  // Add client logic here
}

const showStatistics = () => {
  console.log('Showing statistics')
  // Show statistics logic here
}

const closeInvoiceForm = () => {
  showInvoiceForm.value = false
}

const buttons = ref([
  { id: 1, text: 'Add a Company', action: addCompany },
  { id: 2, text: 'Add a Client', action: addClient },
  { id: 3, text: 'Generate receipt', action: generateInvoice },
  { id: 4, text: 'Statistics', action: showStatistics },
])
</script>

