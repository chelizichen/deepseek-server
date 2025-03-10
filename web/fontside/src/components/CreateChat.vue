<template>
  <div>
    <h1>创建聊天</h1>
    <input v-model="chatMsg" placeholder="聊天消息" />
    <input v-model="sessionId" placeholder="会话 ID" />
    <button @click="handleCreateChat">创建聊天</button>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { createChat } from '../api';

const chatMsg = ref('');
const sessionId = ref(1); // 根据实际情况修改
const userId = ref(1); // 根据实际情况修改

const handleCreateChat = async () => {
  try {
    const response = await createChat(chatMsg.value, sessionId.value, userId.value);
    console.log('创建聊天成功:', response);
  } catch (error) {
    console.error('创建聊天失败:', error);
  }
};
</script>