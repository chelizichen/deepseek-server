<template>
  <div>
    <main class="w-full flex">
      <div
          class="relative flex-1 hidden items-center justify-center h-screen bg-gray-900 lg:flex"
      >
        <div class="relative z-10 w-full max-w-md">
          <img src="https://floatui.com/logo-dark.svg" width="150"/>
          <div class="mt-16 space-y-3">
            <h3 class="text-white text-3xl font-bold">
              Start growing your business quickly
            </h3>
            <p class="text-gray-300">
              Create an account and get access to all features for 30-days, No
              credit card required.
            </p>
            <div class="flex items-center -space-x-2 overflow-hidden">
              <img
                  src="https://randomuser.me/api/portraits/women/79.jpg"
                  class="w-10 h-10 rounded-full border-2 border-white"
              />
              <img
                  src="https://api.uifaces.co/our-content/donated/xZ4wg2Xj.jpg"
                  class="w-10 h-10 rounded-full border-2 border-white"
              />
              <img
                  src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&fit=crop&h=200&w=200&s=a72ca28288878f8404a795f39642a46f"
                  class="w-10 h-10 rounded-full border-2 border-white"
              />
              <img
                  src="https://randomuser.me/api/portraits/men/86.jpg"
                  class="w-10 h-10 rounded-full border-2 border-white"
              />
              <img
                  src="https://images.unsplash.com/photo-1510227272981-87123e259b17?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&fit=crop&h=200&w=200&s=3759e09a5b9fbe53088b23c615b6312e"
                  class="w-10 h-10 rounded-full border-2 border-white"
              />
              <p class="text-sm text-gray-400 font-medium translate-x-5">
                Join 5.000+ users
              </p>
            </div>
          </div>
        </div>
        <div
            class="absolute inset-0 my-auto h-[500px]"
            style="
          background: linear-gradient(
            152.92deg,
            rgba(192, 132, 252, 0.2) 4.54%,
            rgba(232, 121, 249, 0.26) 34.2%,
            rgba(192, 132, 252, 0.1) 77.55%
          );
          filter: blur(118px);
        "
        ></div>
      </div>
      <div class="flex-1 flex items-center justify-center h-screen">
        <div
            class="w-full max-w-md space-y-8 px-4 bg-white text-gray-600 sm:px-0"
        >
          <div class="">
            <img
                src="https://floatui.com/logo.svg"
                width="150"
                class="lg:hidden"
            />
            <div class="mt-5 space-y-2">
              <h3 class="text-gray-800 text-2xl font-bold sm:text-3xl">
                Sign In To Your Account
              </h3>
            </div>
          </div>
          <form @Submit="$event.preventDefault()" class="space-y-5">
            <div>
              <label class="font-medium">Email</label>
              <input
                  type="email"
                  required
                  v-model="email"
                  class="w-full mt-2 px-3 py-2 text-gray-500 bg-transparent outline-none border focus:border-indigo-600 shadow-sm rounded-lg"
              />
            </div>
            <div>
              <label class="font-medium">Password</label>
              <input
                  type="password"
                  required
                  v-model="password"
                  class="w-full mt-2 px-3 py-2 text-gray-500 bg-transparent outline-none border focus:border-indigo-600 shadow-sm rounded-lg"
              />
            </div>
            <button
                class="w-full px-4 py-2 text-white font-medium bg-indigo-600 hover:bg-indigo-500 active:bg-indigo-600 rounded-lg duration-150"
                @click="handleLogin"
            >
              Login
            </button>
          </form>
        </div>
      </div>
    </main>
  </div>
</template>

<script lang="ts" setup>
import {ref} from 'vue';
import {login} from '../api';
import router, {setToken} from "../router";
import {ElMessage} from "element-plus";

const email = ref('');
const password = ref('');

const handleLogin = async () => {
  let response;
  try {
    response = await login(email.value, password.value);
    console.log('登录成功:', response);
    setToken(response.data.password);
    router.push("/chat-center")
    // 登录成功后可以进行页面跳转等操作
  } catch (error) {
    console.error('登录失败:', error);
    ElMessage.error(response.message);
  }
};
</script>