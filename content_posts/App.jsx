import { Routes, Route } from "react-router-dom";
import PostList from "./PostList";
import CreatePost from "./CreatePost";
import EditPost from "./EditPost";
import Dashboard from "./Dashboard";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Dashboard />} />
      <Route path="/posts" element={<PostList />} />
      <Route path="/create" element={<CreatePost />} />
      <Route path="/edit/:id" element={<EditPost />} />
    </Routes>
  );
}