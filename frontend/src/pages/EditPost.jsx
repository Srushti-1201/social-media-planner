import { useEffect, useState } from "react";
import { api } from "../api";
import { useParams, useNavigate } from "react-router-dom";

export default function EditPost() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  useEffect(() => {
    api.get(`posts/${id}/`).then(res => {
      setTitle(res.data.title);
      setContent(res.data.content);
    });
  }, [id]);

  const submit = async (e) => {
    e.preventDefault();
    await api.put(`posts/${id}/`, { title, content });
    navigate("/");
  };

  return (
    <form onSubmit={submit}>
      <h1>Edit Post</h1>
      <input value={title} onChange={e => setTitle(e.target.value)} />
      <textarea value={content} onChange={e => setContent(e.target.value)} />
      <button type="submit">Update</button>
    </form>
  );
}
