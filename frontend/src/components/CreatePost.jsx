import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";

function CreatePost() {
  const [form, setForm] = useState({
    title: "",
    content: "",
    platform: ""
  });

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    await api.post("posts/", form);
    navigate("/");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Create Post</h2>

      <label>Title</label>
      <input
        placeholder="Title"
        value={form.title}
        onChange={e => setForm({ ...form, title: e.target.value })}
      />

      <label>Content</label>
      <textarea
        placeholder="Content"
        value={form.content}
        onChange={e => setForm({ ...form, content: e.target.value })}
      />

      <label>Platform</label>
      <input
        placeholder="Platform"
        value={form.platform}
        onChange={e => setForm({ ...form, platform: e.target.value })}
      />

      <button type="submit">Save</button>
    </form>
  );
}

export default CreatePost;