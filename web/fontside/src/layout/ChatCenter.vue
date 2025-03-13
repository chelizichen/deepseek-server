<template>
  <div class="flex h-screen">
    <div class="w-1/6 bg-gray-100 overflow-y-auto">
      <h2 class="text-lg font-bold p-4 cursor-pointer" @click="createSession">DeepSeek</h2>

      <ul>
        <li class="flex items-center justify-center">
          <el-switch
              v-model="isInference"
              inactive-text="abstract"
              @change="handleSwitchChange"
          >
          </el-switch>
        </li>
        <li v-for="session in sessions" :key="session.id" class="p-4 hover:bg-gray-200 cursor-pointer"
            :class="{
              'bg-blue-100': session.id === Number($route.query.id),
              'text-black':session.id === Number($route.query.id)
            }"
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
const isInference = ref(false);
const handleSwitchChange = (value: boolean) => {
  isInference.value = value;
  let query = router.currentRoute.value.query;
  if (value) {
    router.push({
      path: "/chat-center/select-session-abs",
      query
    });
  } else {
    router.push({
      path: "/chat-center/select-session",
      query
    });
  }
}
onMounted(async () => {
  getSessions(1).then(rsp => {
    sessions.value = rsp.data;
  })
})

function handleSessionClick(sessionId: number) {
  if (isInference.value) {
    router.push({
      path: "/chat-center/select-session-abs",
      query: {
        id: sessionId
      }
    });
  } else {
    router.push({
      path: "/chat-center/select-session",
      query: {
        id: sessionId
      }
    });
  }

}

function createSession() {
  router.push("create-session");
}


</script>

<style scoped>
:deep(.el-switch__label.is-active) {
  color: gray;
}

:deep(.el-switch.is-checked .el-switch__core ) {
  background: gray;
  border-color: darkgray;
}
</style>
