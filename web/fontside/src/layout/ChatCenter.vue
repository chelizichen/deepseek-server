<template>
  <div class="flex h-screen">
    <div class="w-1/6 bg-gray-100 overflow-y-auto">
      <h2 class="text-lg font-bold p-4 cursor-pointer" @click="createSession">SgridChat</h2>
      <ul>
        <li v-for="session in sessions" :key="session.id" class="p-4 hover:bg-gray-200 cursor-pointer"
            @click="handleSessionClick(session.id)">
          {{ session.name }}
        </li>
      </ul>
    </div>
    <div class="w-5/6 bg-white p-4">
      <router-view></router-view>
    </div>
  </div>
</template>

<script lang="ts" setup>
import {onMounted, ref} from 'vue';
import router from "../router";
import {getSessions} from "../api";
// 模拟会话列表数据
const sessions = ref<Array<{ name: string, id: number }>>([]);

onMounted(async () => {
  getSessions(1).then(rsp => {
    sessions.value = rsp.data;
  })
})

function handleSessionClick(sessionId: number) {
  router.push({
    path: "/chat-center/select-session",
    query: {
      id: sessionId
    }
  });
}

function createSession() {
  router.push("create-session");
}


</script>

<style scoped>
/* 可以根据需要添加更多样式 */
</style>
