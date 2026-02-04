import { useEffect, useState } from "react";
import { getPosts, deletePost } from "../api/posts";
import { Link } from "react-router-dom";

export default function PostList() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  const loadPosts = async () => {
    try {
      setLoading(true);
      const res = await getPosts();
      setPosts(res.data);
    } catch (err) {
      console.error("Failed to load posts", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadPosts();
  }, []);

  const handleDelete = async (id) => {
    if (!confirm("Are you sure?")) return;
    await deletePost(id);
    loadPosts();
  };

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">Content Planner 🚀</h1>
        <Link to="/create" className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
          + New Post
        </Link>
      </div>

      <div className="grid gap-4">
        {loading && <p>Loading posts...</p>}
        {!loading && posts.length === 0 && (
          <p>No posts yet. Create your first post 🚀</p>
        )}
        {posts.map((post) => (
          <div key={post.id} className="border p-4 rounded shadow-sm bg-white">
            <div className="flex justify-between items-start">
              <h2 className="text-xl font-bold">{post.title}</h2>
              <span className="text-xs bg-gray-200 px-2 py-1 rounded">{post.status}</span>
            </div>
            <p className="text-sm text-gray-500 mb-2">Platform: {post.platform}</p>
            <p className="whitespace-pre-wrap mb-4">{post.content}</p>

            <div className="flex gap-3">
              <Link to={`/edit/${post.id}`} className="text-blue-600 hover:underline">
                Edit
              </Link>
              <button
                onClick={() => handleDelete(post.id)}
                className="text-red-600 hover:underline"
              >
                Delete
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}