import { useEffect, useState } from "react";
import axios from "axios";

function Dashboard() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get("http://localhost:8000/api/posts/")
      .then(res => setPosts(res.data))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading dashboard...</p>;

  return (
    <div style={{ padding: "20px", background: "#fafafa" }}>
      <h1 style={{ marginBottom: "20px" }}>Dashboard</h1>

      <Stats posts={posts} />
      <RecentPosts posts={posts} />
      <PlatformStats posts={posts} />
    </div>
  );
}

function Stats({ posts }) {
  const platforms = new Set(posts.map(p => p.platform));
  const latest = posts[posts.length - 1];

  return (
    <div style={{ display: "flex", gap: "16px", marginBottom: "20px" }}>
      <Card title="Total Posts" value={posts.length} />
      <Card title="Platforms" value={platforms.size} />
      <Card title="Latest Post" value={latest?.title || "—"} />
    </div>
  );
}

function Card({ title, value }) {
  return (
    <div style={{
      padding: "16px",
      border: "1px solid #ddd",
      borderRadius: "8px",
      width: "200px",
      background: "#fff",
      boxShadow: "0 2px 8px rgba(0,0,0,0.05)"
    }}>
      <h4 style={{ margin: "0 0 10px 0" }}>{title}</h4>
      <strong style={{ fontSize: "24px" }}>{value}</strong>
    </div>
  );
}

function RecentPosts({ posts }) {
  return (
    <div style={{ marginBottom: "20px", background: "#fff", padding: "16px", borderRadius: "8px", boxShadow: "0 2px 8px rgba(0,0,0,0.05)" }}>
      <h3>Recent Posts</h3>
      <ul>
        {posts.slice(-5).reverse().map(post => (
          <li key={post.id} style={{ padding: "8px 0", borderBottom: "1px solid #eee" }}>
            <strong>{post.title}</strong> — {post.platform}
          </li>
        ))}
      </ul>
    </div>
  );
}

function PlatformStats({ posts }) {
  const counts = posts.reduce((acc, post) => {
    acc[post.platform] = (acc[post.platform] || 0) + 1;
    return acc;
  }, {});

  return (
    <div style={{ background: "#fff", padding: "16px", borderRadius: "8px", boxShadow: "0 2px 8px rgba(0,0,0,0.05)" }}>
      <h3>Posts by Platform</h3>
      {Object.entries(counts).map(([platform, count]) => (
        <p key={platform}>
          {platform}: <strong>{count}</strong>
        </p>
      ))}
    </div>
  );
}

export default Dashboard;
