import { useEffect, useState } from "react";
import { getPost, updatePost } from "../api/posts";
import { useNavigate, useParams, Link } from "react-router-dom";

export default function EditPost() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    title: '',
    platform: 'instagram',
    content: '',
    status: 'draft'
  });

  useEffect(() => {
    getPost(id).then((res) => {
      setFormData(res.data);
    }).catch(err => console.error("Error loading post", err));
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await updatePost(id, formData);
      navigate("/");
    } catch (err) {
      console.error("Error updating post", err);
      alert("Failed to update post");
    }
  };

  return (
    <div className="p-6 max-w-2xl mx-auto">
      <h2 className="text-2xl font-bold mb-4">Edit Post</h2>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <input
          placeholder="Title"
          value={formData.title}
          onChange={(e) => setFormData({...formData, title: e.target.value})}
          className="border p-2 w-full rounded"
          required
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
          required
        />
        <div className="flex gap-2">
          <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
            Update
          </button>
          <Link to="/" className="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600">
            Cancel
          </Link>
        </div>
      </form>
    </div>
  );
}