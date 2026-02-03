import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const postsAPI = {
  getAll: () => api.get('/posts/'),
  getOne: (id) => api.get(`/posts/${id}/`),
  create: (data) => api.post('/posts/', data),
  update: (id, data) => api.put(`/posts/${id}/`, data),
  delete: (id) => api.delete(`/posts/${id}/`),
  getAnalytics: () => api.get('/posts/analytics/'),
  fetchImage: (query) => api.get('/posts/fetch_image/', { params: { query } }),
  getRandomQuote: () => api.get('/posts/random_quote/'),
};

export default api;