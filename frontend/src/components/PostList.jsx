import { useEffect, useState } from "react";
import api from "../api";
import { Link } from "react-router-dom";

function PostList() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    api.get("posts/")
      .then(res => setPosts(res.data.results || res.data))
      .catch(err => console.error(err));
  }, []);

  const handleDelete = async (id) => {
    if (!window.confirm("Delete this post?")) return;
    await api.delete(`posts/${id}/`);
    setPosts(posts.filter(p => p.id !== id));
  };

  return (
    <div>
      <h2>Posts</h2>
      <Link to="/create">➕ Create Post</Link>

      <ul>
        {posts.map(post => (
          <li key={post.id}>
            <b>{post.title}</b> ({post.platform})
            <br />
            <Link to={`/edit/${post.id}`}>✏️ Edit</Link>
            {" | "}
            <button onClick={() => handleDelete(post.id)}>🗑 Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PostList;