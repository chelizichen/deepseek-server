// src/router/index.ts
import {createRouter, createWebHashHistory, RouteRecordRaw} from 'vue-router';
import Login from '../components/Login.vue';
import CreateSession from '../components/CreateSession.vue';
import SelectPrompts from '../components/SelectPrompts.vue';
import CreateChat from '../components/CreateChat.vue';
import ChatCenter from "../layout/ChatCenter.vue";
import SelectSession from "../components/SelectSession.vue";

const routes: RouteRecordRaw[] = [
    {path: '/login', component: Login},
    {
        path: "/chat-center",
        component: ChatCenter,
        children: [
            {path: 'create-session', component: CreateSession},
            {path: 'select-prompts', component: SelectPrompts},
            {path: 'create-chat', component: CreateChat},
            {path: 'select-session', component: SelectSession},
        ]
    }

];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

const TOKEN = "token"

function getToken() {
    return localStorage.getItem(TOKEN);
}

export function setToken(token: string) {
    localStorage.setItem(TOKEN, token);
}

router.beforeEach((to, from, next) => {
    const token = getToken(); // 获取 token
    console.log('token', token); // 打印 token（调试用）

    // 如果目标路径是登录页且没有 token，直接放行
    if (to.path === '/login') {
        if (!token) {
            next(); // 允许访问登录页
            return;
        } else {
            next('/chat-center'); // 如果有 token，重定向到聊天中心
            return;
        }
    }

    // 如果没有 token，重定向到登录页
    if (!token) {
        next('/login');
        return;
    }

    // 如果路径为空（通常是根路径），重定向到默认页面（如聊天中心）

    if (to.path != "/") {
        console.log(to.path);
        next();
        return;
    }
    next('/chat-center');
    // 其他情况，正常放行
});


export default router;
