import { useEffect, useState } from "react";
import { api } from "../api";
import { Link } from "react-router-dom";

export default function PostList() {
  const [posts, setPosts] = useState([]);

  const loadPosts = async () => {
    const res = await api.get("posts/");
    setPosts(res.data);
  };

  const deletePost = async (id) => {
    await api.delete(`posts/${id}/`);
    loadPosts();
  };

  useEffect(() => {
    loadPosts();
  }, []);

  return (
    <div>
      <h1>Posts</h1>
      <Link to="/create">Create Post</Link>

      {posts.map((p) => (
        <div key={p.id}>
          <h3>{p.title}</h3>
          <p>{p.content}</p>
          <Link to={`/edit/${p.id}`}>Edit</Link>
          <button onClick={() => deletePost(p.id)}>Delete</button>
        </div>
      ))}
    </div>
  );
}
