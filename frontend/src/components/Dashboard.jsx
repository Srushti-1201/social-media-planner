import { useEffect, useState } from 'react';
import { Pie, Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
} from 'chart.js';
import api from '../api'; // Assumes api.js is in the parent src/ folder

ChartJS.register(
  ArcElement, Tooltip, Legend, CategoryScale, LinearScale, BarElement, Title
);

export default function Dashboard() {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const res = await api.get("/dashboard/stats/");
        setStats(res.data);
      } catch (err) {
        setError('Failed to fetch dashboard statistics.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchStats();
  }, []);

  if (loading) {
    return <p>Loading dashboard...</p>;
  }

  if (error) {
    return <p>{error}</p>;
  }

  if (!stats) return <p>No stats available.</p>;

  const pieData = {
    labels: ['Published', 'Drafts'],
    datasets: [
      {
        label: '# of Posts',
        data: [stats.published, stats.drafts],
        backgroundColor: [
          'rgba(75, 192, 192, 0.6)',
          'rgba(255, 159, 64, 0.6)',
        ],
        borderColor: [
          'rgba(75, 192, 192, 1)',
          'rgba(255, 159, 64, 1)',
        ],
        borderWidth: 1,
      },
    ],
  };

  const barData = {
    labels: stats.platform_stats.map(p => p.platform.charAt(0).toUpperCase() + p.platform.slice(1)),
    datasets: [
      {
        label: 'Posts',
        data: stats.platform_stats.map(p => p.count),
        backgroundColor: 'rgba(54, 162, 235, 0.6)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1,
      },
    ],
  };

  const barOptions = {
    responsive: true,
    plugins: {
      legend: { display: false },
      title: {
        display: true,
        text: 'Posts per Platform',
      },
    },
  };

  return (
    <div style={{ maxWidth: "1200px", margin: "auto", padding: "20px" }}>
      <h1 style={{ textAlign: "center", marginBottom: "40px" }}>Dashboard</h1>
      <div style={{ display: "flex", flexWrap: "wrap", justifyContent: "center", alignItems: "center", gap: "40px" }}>
        <div style={{ width: "100%", maxWidth: "400px" }}>
          <Pie data={pieData} options={{ plugins: { title: { display: true, text: 'Post Status' } } }} />
        </div>
        <div style={{ width: "100%", maxWidth: "600px" }}>
          <Bar options={barOptions} data={barData} />
        </div>
      </div>
    </div>
  );
}