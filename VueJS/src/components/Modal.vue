<template>
  <div
    id="modal"
    class="modal"
    :class="{ 'is-active': isOpen }"
  >
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Confirm</p>
      </header>
      <section class="modal-card-body">{{ message }}</section>
      <footer class="modal-card-foot">
        <button
          class="button modal-yes"
          @click="onYes"
        >Yes</button>
        <button
          class="button is-primary modal-no"
          @click="onNo"
        >No</button>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Modal',
  props: {
    message: {
      type: String,
      default: () => ''
    },
    isOpen: {
      type: Boolean,
      default: () => false
    }
  },
  methods: {
    onYes() {
      this.$emit('handleYes');
    },
    onNo() {
      this.$emit('handleNo');
    }
  }
};
</script>
