import { useState } from "react";
import { createPost } from "../api/posts";
import { useNavigate, Link } from "react-router-dom";
import axios from "axios";

export default function CreatePost() {
  const [formData, setFormData] = useState({
    title: '',
    platform: 'instagram',
    content: '',
    status: 'draft'
  });
  const [loading, setLoading] = useState(false);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("SUBMIT CLICKED"); // 👈 add this
    if (!formData.title || !formData.content) {
      setError("Title and content are required");
      return;
    }
    setError("");
    setSaving(true);
    try {
      await createPost(formData);
      navigate("/");
    } catch (err) {
      console.error("STATUS:", err.response?.status);
      console.error("DATA:", err.response?.data);
      alert(JSON.stringify(err.response?.data));
    } finally {
      setSaving(false);
    }
  };

  const generateCaption = async () => {
    try {
      setError("");
      setLoading(true);
      const res = await axios.get("https://api.quotable.io/random");
      const quote = res.data.content;
      const author = res.data.author;
      setFormData(prevData => ({...prevData, content: `${quote} — ${author}`}));
    } catch (error) {
      setError("Could not fetch caption. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6 max-w-2xl mx-auto">
      <h2 className="text-2xl font-bold mb-4">Create New Post</h2>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <input
          placeholder="Title"
          value={formData.title}
          onChange={(e) => setFormData({...formData, title: e.target.value})}
          className="border p-2 w-full rounded"
        />
        <select
          value={formData.platform}
          onChange={(e) => setFormData({...formData, platform: e.target.value})}
          className="border p-2 w-full rounded"
        >
          <option value="instagram">Instagram</option>
          <option value="facebook">Facebook</option>
          <option value="linkedin">LinkedIn</option>
          <option value="twitter">Twitter</option>
        </select>
        <textarea
          placeholder="Content"
          value={formData.content}
          onChange={(e) => setFormData({...formData, content: e.target.value})}
          className="border p-2 w-full rounded h-32"
        />
        <div className="flex gap-2 items-center">
          <button
            type="button"
            onClick={generateCaption}
            disabled={loading || formData.content.length > 0}
            className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 disabled:bg-blue-300"
          >
            {loading ? "Generating..." : "Generate Caption"}
          </button>
          <small className="text-gray-500">Powered by Quotable API</small>
        </div>
        {error && <p className="text-red-500">{error}</p>}
        <div className="flex gap-2">
          <button 
            type="submit" 
            className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 disabled:bg-green-300"
            disabled={saving}
          >
            {saving ? "Saving..." : "Save"}
          </button>
          <Link to="/" className="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600">
            Cancel
          </Link>
        </div>
      </form>
    </div>
  );
}
