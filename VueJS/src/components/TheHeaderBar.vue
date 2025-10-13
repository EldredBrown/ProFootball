<template>
  <header>
    <nav
      class="navbar has-background-dark is-dark"
      role="navigation"
      aria-label="main navigation"
    >
      <div class="navbar-brand">
        <a
          class="navbar-item"
          :href="vuejs"
          target="_blank"
          rel="noopener noreferrer"
        >
          <!-- For development mode -->
          <font-awesome-icon
            :icon="['fab', 'vuejs']"
            class="fab js-logo fa-2x"
          />
          <!-- For production or test mode -->
          <!-- <i class="fab js-logo fa-vuejs fa-2x" aria-hidden="true" /> -->
        </a>
        <div class="navbar-item nav-home">Pro Football VueJS</div>
        <button
          class="link navbar-burger burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbarBasicExample"
        >
          <span aria-hidden="true" />
          <span aria-hidden="true" />
          <span aria-hidden="true" />
        </button>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'TheHeaderBar',
  data() {
    return {
      vuejs: 'https://vuejs.org/'
    };
  }
};
</script>
