<template>
  <div id="app">
    <TheHeaderBar />
    <div class="main-section columns">
      <TheNavBar />
      <main class="column">
        <router-view />
      </main>
    </div>
  </div>
</template>

<script>
import TheHeaderBar from '@/components/TheHeaderBar';
import TheNavBar from '@/components/TheNavBar';

export default {
  name: 'App',
  components: { TheHeaderBar, TheNavBar }
};
</script>

<style lang="scss">
@import '@/styles/index.scss';
</style>
