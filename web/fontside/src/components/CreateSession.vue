<template>
  <div class="w-full h-full flex items-center justify-center">
    <div class="p-8 bg-white rounded-lg shadow-md">
      <!-- 会话标题 -->
      <h1 class="text-2xl font-bold text-center mb-6">创建会话</h1>

      <!-- 会话提示词输入框 -->
      <div class="mb-4">
        <label for="prompt" class="block text-gray-700 text-sm font-bold mb-2">会话名称</label>
        <input
            v-model="prompt"
            type="text"
            id="prompt"
            placeholder="输入会话名称"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        />
      </div>

      <!-- 可选的会话提示词列表 -->
      <div class="mb-6">
        <label class="block text-gray-700 text-sm font-bold mb-2">选择会话提示词</label>
        <div class="flex flex-wrap -mx-2">
          <div
              v-for="(option, index) in promptOptions"
              :key="index"
              class="w-1/2 px-2 mb-2"
          >
            <button
                @click="togglePromptSelection(option)"
                :class="{
              'border-gray-300':!selectedPrompts.includes(option),
              'border-blue-500': selectedPrompts.includes(option),
            }"
                class="w-full border py-2 px-3 rounded text-gray-700 text-center focus:outline-none"
            >
              {{ option.name }}
            </button>
          </div>
        </div>
      </div>
      <button
          @click="handleCreateSession"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full"
      >
        创建会话
      </button>

      <el-divider/>

      <div>
        <el-input
            v-model="promptText"
            placeholder="请输入预设词"
        >
          <template #append>
            <el-button @click="savePrompt">创建预设词</el-button>
          </template>
        </el-input>
      </div>
    </div>

  </div>
</template>

<script lang="ts" setup>
import {onMounted, ref} from 'vue';
import {getPromptsList, saveChatPrompts, savePrompts, saveSession} from '../api';

// 会话提示词
const prompt = ref('');
// 用户 ID
const userId = ref(1);
// 可选的提示词选项
const promptOptions = ref<Array<{ name: string, id: number }>>([]);

function getPromptOptions() {
  getPromptsList().then((promptsList) => {
    promptOptions.value = promptsList.data;
  })
}

onMounted(() => {
  getPromptOptions()
})

// 选中的提示词
const selectedPrompts = ref<any[]>([]);

const togglePromptSelection = (option: any) => {
  if (selectedPrompts.value.includes(option)) {
    selectedPrompts.value = selectedPrompts.value.filter((item) => item !== option);
  } else {
    selectedPrompts.value.push(option);
  }
};

const handleCreateSession = async () => {
  try {
    // 可以根据需要将 selectedPrompts 也传递给后端
    const session = await saveSession(userId.value, prompt.value);
    const response = await saveChatPrompts(session.data.id, userId.value, selectedPrompts.value.map((item) => item.id));
    console.log('创建会话成功 session :', session);
    console.log('创建会话成功 response:', response);
  } catch (error) {
    console.error('创建会话失败:', error);
  }
};


const promptText = ref("")

function savePrompt() {
  savePrompts(userId.value, promptText.value).then(()=>{
    getPromptOptions()
  })
}
</script>