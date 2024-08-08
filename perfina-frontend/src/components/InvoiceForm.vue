<!-- InvoiceForm.vue -->
<template>
  <div
    class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex items-center justify-center"
    id="my-modal"
  >
    <div class="relative p-8 border shadow-lg rounded-md bg-white w-full max-w-4xl">
      <button
        @click="$emit('close')"
        class="absolute top-4 right-4 text-gray-600 hover:text-gray-900"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </button>

      <h3 class="text-2xl font-bold text-gray-900 mb-6">Generate Invoice</h3>
      <form
        @submit.prevent="submitForm"
        class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4"
      >
        <div v-for="field in formFields" :key="field.key" class="mb-4">
          <label :for="field.key" class="block text-gray-700 text-sm font-bold mb-2">
            {{ formatLabel(field.key) }}
          </label>
          <input
            v-model="form[field.key]"
            :id="field.key"
            :type="field.type"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            required
          />
        </div>
        <div class="col-span-full mt-6">
          <button
            type="submit"
            class="px-6 py-3 bg-blue-500 text-white text-base font-medium rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-300 w-full md:w-auto"
          >
            Generate Invoice
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useUserStore } from '@/stores/user_store'

const emit = defineEmits(['close'])
const userStore = useUserStore()

const formFields = [
  { key: 'company_name', type: 'text' },
  { key: 'company_address', type: 'text' },
  { key: 'company_postal_code', type: 'text' },
  { key: 'company_phone', type: 'tel' },
  { key: 'company_email', type: 'email' },
  { key: 'company_ico', type: 'text' },
  { key: 'company_dic', type: 'text' },
  { key: 'company_bank_account', type: 'text' },
  { key: 'category', type: 'text' },
  { key: 'services', type: 'text' },
  { key: 'rate', type: 'number' },
  { key: 'hours', type: 'number' },
  { key: 'invoice_number', type: 'text' },
  { key: 'variable_symbol', type: 'text' },
  { key: 'invoice_date', type: 'date' },
  { key: 'invoice_due', type: 'date' },
  { key: 'client_name', type: 'text' },
  { key: 'client_address', type: 'text' },
  { key: 'client_postal_code', type: 'text' },
  { key: 'client_ico', type: 'text' },
  { key: 'client_dic', type: 'text' },
]

const form = ref(Object.fromEntries(formFields.map((field) => [field.key, ''])))

const formatLabel = (key) =>
  key
    .split('_')
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ')

const invoiceData = computed(() =>
  Object.fromEntries(
    Object.entries(form.value).map(([key, value]) => [
      key,
      ['rate', 'hours'].includes(key) ? parseFloat(value) || 0 : value,
    ])
  )
)

const submitForm = async () => {
  try {
    const response = await userStore.generateInvoice(invoiceData.value)
    downloadPdf(response.data)
    emit('close')
  } catch (error) {
    console.error('Error generating invoice:', error)
  }
}

const downloadPdf = (data) => {
  const blob = new Blob([data], { type: 'application/pdf' })
  const url = window.URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.style.display = 'none'
  a.href = url
  a.download = 'invoice.pdf'
  document.body.appendChild(a)
  a.click()
  window.URL.revokeObjectURL(url)
  document.body.removeChild(a)
}
</script>

