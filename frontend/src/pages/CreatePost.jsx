import { useState } from "react";
import { api } from "../api";
import { useNavigate } from "react-router-dom";

export default function CreatePost() {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const navigate = useNavigate();

  const submit = async (e) => {
    e.preventDefault();
    await api.post("posts/", {
      title,
      content,
      platform: "facebook",
      status: "draft",
    });
    navigate("/");
  };

  return (
    <form onSubmit={submit}>
      <h1>Create Post</h1>
      <input placeholder="Title" onChange={e => setTitle(e.target.value)} />
      <textarea placeholder="Content" onChange={e => setContent(e.target.value)} />
      <button type="submit">Save</button>
    </form>
  );
}
