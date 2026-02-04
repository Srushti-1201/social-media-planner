import { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid
} from "recharts";

function StatCard({ title, value }) {
  return (
    <div style={{
      background: "#fff",
      padding: "20px",
      borderRadius: "10px",
      boxShadow: "0 4px 10px rgba(0,0,0,0.08)"
    }}>
      <p style={{ color: "#666", margin: "0 0 5px 0", fontSize: "14px" }}>{title}</p>
      <h2 style={{ margin: 0, fontSize: "28px", fontWeight: "bold" }}>{value}</h2>
    </div>
  );
}

export default function Dashboard() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        // Fetching from your Django API
        const response = await axios.get("http://127.0.0.1:8000/api/posts/");
        setPosts(response.data);
      } catch (err) {
        console.error("Error fetching posts:", err);
        setError("Failed to load dashboard data.");
      } finally {
        setLoading(false);
      }
    };

    fetchPosts();
  }, []);

  // 📊 Prepare data for the chart
  const platformData = Object.entries(
    posts.reduce((acc, post) => {
      // Normalize platform names (e.g., "instagram" -> "Instagram")
      const platformName = post.platform ? (post.platform.charAt(0).toUpperCase() + post.platform.slice(1)) : "Unknown";
      acc[platformName] = (acc[platformName] || 0) + 1;
      return acc;
    }, {})
  ).map(([name, value]) => ({ name, value }));

  // 🧮 Calculate stats
  const totalPosts = posts.length;
  const platformCount = platformData.length;
  // API returns ordered by -created_at, so the first one is the latest
  const latestPost = posts.length > 0 ? posts[0] : null;

  if (loading) return <div className="p-6">Loading dashboard...</div>;
  if (error) return <div className="p-6 text-red-500">{error}</div>;

  return (
    <div style={{ padding: "24px", maxWidth: "1200px", margin: "0 auto", backgroundColor: "#f5f7fb", minHeight: "100vh" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "24px" }}>
        <h1 style={{ margin: 0, color: "#1f2937" }}>Dashboard</h1>
        <Link 
          to="/create" 
          style={{
            background: "#2563eb",
            color: "white",
            padding: "10px 20px",
            borderRadius: "6px",
            textDecoration: "none",
            fontWeight: "bold",
            fontSize: "14px"
          }}
        >
          + Create Post
        </Link>
      </div>

      {/* 🧩 STEP 1 & 2: Stat Cards Grid */}
      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))",
        gap: "16px",
        marginBottom: "32px"
      }}>
        <StatCard title="Total Posts" value={totalPosts} />
        <StatCard title="Active Platforms" value={platformCount} />
        <StatCard 
          title="Latest Post" 
          value={latestPost ? (latestPost.title.length > 15 ? latestPost.title.substring(0, 15) + "..." : latestPost.title) : "—"} 
        />
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(500px, 1fr))", gap: "24px" }}>
        
        {/* 📊 STEP 3: Chart (Main Visualization) */}
        <div style={{
          background: "#fff",
          padding: "24px",
          borderRadius: "10px",
          boxShadow: "0 4px 10px rgba(0,0,0,0.08)"
        }}>
          <h3 style={{ marginTop: 0, marginBottom: "20px", color: "#4b5563" }}>Posts per Platform</h3>
          <div style={{ width: "100%", height: 300 }}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={platformData}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} />
                <XAxis dataKey="name" axisLine={false} tickLine={false} />
                <YAxis axisLine={false} tickLine={false} allowDecimals={false} />
                <Tooltip 
                  cursor={{ fill: 'transparent' }}
                  contentStyle={{ borderRadius: '8px', border: 'none', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }}
                />
                <Bar dataKey="value" fill="#3b82f6" radius={[4, 4, 0, 0]} barSize={50} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* 🧾 STEP 4: Recent Activity */}
        <div style={{
          background: "#fff",
          padding: "24px",
          borderRadius: "10px",
          boxShadow: "0 4px 10px rgba(0,0,0,0.08)"
        }}>
          <h3 style={{ marginTop: 0, marginBottom: "20px", color: "#4b5563" }}>Recent Activity</h3>
          <ul style={{ listStyle: "none", padding: 0, margin: 0 }}>
            {posts.slice(0, 5).map(post => (
              <li key={post.id} style={{ 
                padding: "12px 0", 
                borderBottom: "1px solid #f3f4f6",
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center"
              }}>
                <div>
                  <strong style={{ display: "block", marginBottom: "4px", color: "#1f2937" }}>{post.title}</strong>
                  <span style={{ 
                    fontSize: "12px", 
                    color: "#4b5563",
                    background: "#f3f4f6",
                    padding: "2px 8px",
                    borderRadius: "12px",
                    textTransform: "capitalize"
                  }}>
                    {post.platform}
                  </span>
                </div>
                <span style={{ fontSize: "12px", color: "#9ca3af" }}>
                  {new Date(post.created_at).toLocaleDateString()}
                </span>
              </li>
            ))}
            {posts.length === 0 && <li style={{ color: "#888", fontStyle: "italic" }}>No posts yet.</li>}
          </ul>
        </div>
      </div>
    </div>
  );
}