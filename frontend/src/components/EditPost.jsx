import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import api from "../api";

function EditPost() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [form, setForm] = useState({
    title: "",
    content: "",
    platform: ""
  });

  useEffect(() => {
    api.get(`posts/${id}/`).then(res => setForm(res.data));
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await api.put(`posts/${id}/`, form);
    navigate("/");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Edit Post</h2>

      <label>Title</label>
      <input
        value={form.title}
        onChange={e => setForm({ ...form, title: e.target.value })}
      />

      <label>Content</label>
      <textarea
        value={form.content}
        onChange={e => setForm({ ...form, content: e.target.value })}
      />

      <label>Platform</label>
      <input
        value={form.platform}
        onChange={e => setForm({ ...form, platform: e.target.value })}
      />

      <button type="submit">Update</button>
    </form>
  );
}

export default EditPost;