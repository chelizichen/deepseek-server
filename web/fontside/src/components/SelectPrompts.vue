<template>
  <div>
    <h1>选取提示词</h1>
    <input v-model="promptName" placeholder="提示词名称" />
    <button @click="handleSavePrompts">保存提示词</button>
    <!-- 可以添加更多提示词选择和操作 -->
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { savePrompts } from '../api';

const promptName = ref('');
const userId = ref(1); // 根据实际情况修改

const handleSavePrompts = async () => {
  try {
    const response = await savePrompts(userId.value, promptName.value);
    console.log('保存提示词成功:', response);
  } catch (error) {
    console.error('保存提示词失败:', error);
  }
};
</script>
