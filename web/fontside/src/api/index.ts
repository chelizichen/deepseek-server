// src/api/index.ts
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL; // 根据实际情况修改

const httpInstance = axios.create({
    baseURL: API_BASE_URL,
    timeout: 600000, // 请求超时时间
});

// 登录接口
export const login = async (email: string, password: string) => {
    try {
        const response = await httpInstance.post(`/user/login`, {email, password});
        return response.data;
    } catch (error) {
        console.error('登录失败:', error);
        throw error;
    }
};

// 创建会话接口
export const saveSession = async (userId: number, name: string) => {
    try {
        const response = await httpInstance.post(`/sessions/save`, {user_id: userId, name});
        return response.data;
    } catch (error) {
        console.error('创建会话失败:', error);
        throw error;
    }
};

// 保存提示词接口
export const savePrompts = async (userId: number, name: string) => {
    try {
        const response = await httpInstance.post(`/prompts/save`, {user_id: userId, name});
        return response.data;
    } catch (error) {
        console.error('保存提示词失败:', error);
        throw error;
    }
};

// 保存聊天提示词接口
export const saveChatPrompts = async (sessionId: number, userId: number, promptIds: number[]) => {
    try {
        const response = await httpInstance.post(`/chat_prompts/save`, {
            session_id: sessionId,
            user_id: userId,
            prompt_ids: promptIds
        });
        return response.data;
    } catch (error) {
        console.error('保存聊天提示词失败:', error);
        throw error;
    }
};

// 创建聊天接口
export const createChat = async (chatMsg: string, sessionId: number, userId: number, chatType?: string, prompts?: string[], history?: any[]) => {
    try {
        const data = {chat_msg: chatMsg, session_id: sessionId, user_id: userId, chat_type: chatType, prompts, history};
        const response = await httpInstance.post(`/chat`, data);
        return response.data;
    } catch (error) {
        console.error('创建聊天失败:', error);
        throw error;
    }
};

export const getSessions = async (userId: number) => {
    try {
        const response = await httpInstance.get(`/users/sessions/list`, {params: {user_id: userId}});
        console.log(response);
        return response.data;
    } catch (error) {
        console.error('获取会话失败:', error);
        throw error;
    }
};

export const getChatHistory = async (sessionId: number) => {
    try {
        const response = await httpInstance.get(`/get_chat_history`, {params: {session_id: sessionId}});
        console.log(response);
        return response.data;
    } catch (error) {
        console.error('获取会话失败:', error);
        throw error;
    }
}

export const getChatHistoryInferenceBySessionId = async (sessionId: number) => {
    try {
        const response = await httpInstance.get(`/get_chat_history_inference_by_session_id`, {params: {session_id: sessionId}});
        console.log(response);
        return response.data;
    }   catch (error) {
        console.error('获取会话失败:', error);
        throw error;
    }
}

export const chat = async (sessionId: number, chat_msg: string, user_id: number) => {
    try {
        const response = await httpInstance.post(`/chat`, {
            session_id: sessionId,
            user_id: user_id,
            chat_msg: chat_msg
        });
        console.log(response);
        return response.data;
    } catch (error) {
        console.error('获取会话失败:', error);
        throw error;
    }
}

export const getPromptsList = async () => {
    try {
        const response = await httpInstance.get(`/prompts/list`,);
        console.log(response);
        return response.data;
    } catch (error) {
        console.error('获取会话失败:', error);
        throw error;
    }
}