import axios from "axios";

const BASE_URL = "http://localhost:8000";

export const getConversations = () =>
    axios.get(`${BASE_URL}/conversation`);

export const createConversation = (data: any) =>
    axios.post(`${BASE_URL}/conversation`, data);

export const sendMessage = (data: any) =>
    axios.post(`${BASE_URL}/chat`, data);