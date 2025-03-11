<script setup lang="ts">
import {reloadState} from './store'

</script>

<template>
  <div>
    <router-view v-if="reloadState"></router-view>
  </div>
</template>

<style scoped>

</style>
