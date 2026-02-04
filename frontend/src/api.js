import axios from "axios";

export const api = axios.create({
  baseURL: "https://social-media-planner-1.onrender.com/api/",
});
