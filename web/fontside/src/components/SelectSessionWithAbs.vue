<template>
  <div class="w-full h-full">
    <div class="h-5/6 relative overflow-scroll pb-12">
      <div v-for="item in chatList" :key="item.question">
        <div class="flex justify-end">
          <div class="p-4 rounded my-4 bg-blue-50 text-gray-950 w-fit">
            <p class="text-right">{{ item.question }}</p>
          </div>
        </div>
        <div class="flex justify-start">
          <div class="answer bg-gray-100 p-4 rounded my-4 text-gray-950">
            <p v-html="item.answer"></p>
          </div>
        </div>
      </div>
    </div>
    <div class="absolute bottom-4 w-5/6">
      <div class="flex justify-center items-center">
        <div class="w-10/12">
          <el-input
            v-model="message"
            :autosize="{ minRows: 4, maxRows: 20 }"
            type="textarea"
            placeholder="Input your question here"
            class="bg-gray-400"
          >
          </el-input>
        </div>
        <div>
          <el-button
            @click="sendMessage"
            class="ml-2 bg-blue-500 px-2 py-2 text-white w-14 h-14"
            circle
          >
            Send
          </el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from "vue";
import { useRoute } from "vue-router";
import {chat, getChatHistory, getChatHistoryInferenceBySessionId} from "../api";
import { ElMessage } from "element-plus";
import MarkdownIt from "markdown-it";
let md = new MarkdownIt();


let chatList = ref<Array<{ question: string; answer: string }>>([]);
let route = useRoute();

watch(
  route,
  (newVal) => {
    const sessionId = Number(newVal.query.id);
    getChatListBySessionId(sessionId);
  },
  {
    immediate: true,
  },
);

function getChatListBySessionId(id: number) {
  getChatHistoryInferenceBySessionId(id).then((res) => {
    chatList.value = res.data.map((v:any) => {
      v.answer = md.render(v.answer); //传入
      console.log("v.answer", v.answer);
      return v;
    });
    console.log("chatList", chatList);
  });
}

const message = ref("");

function sendMessage() {
  if (message.value.trim() !== "") {
    // 这里可以添加发送消息的逻辑，例如调用 API 发送消息
    console.log("发送消息:", message.value);
    chatList.value.push({
      question: message.value,
      answer: "loading...",
    });
    let body = {
      session_id: Number(route.query.id),
      chat_msg: message.value,
      user_id: 1, // todo
    };
    chat(body.session_id, body.chat_msg, body.user_id)
      .then((res) => {
        if(res.code){
          ElMessage.error(res.message);
          return
        }
        chatList.value[chatList.value.length - 1].answer = md.render(
          res.data.answer,
        );
      })
      .catch((err) => {
        ElMessage.error(err);
        chatList.value.splice(chatList.value.length - 1, 1);
      });
    message.value = ""; // 清空输入框
  }
}
</script>

<style scoped></style>
