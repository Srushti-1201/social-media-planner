import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";

// Assuming your page components are moved to a `src/pages` directory
import PostsList from "./pages/PostList";
import CreatePost from "./pages/CreatePost";
import EditPost from "./pages/EditPost";
import Dashboard from "./pages/Dashboard";
import ThirdParty from "./pages/ThirdParty";

function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<PostsList />} />
        <Route path="/create" element={<CreatePost />} />
        <Route path="/edit/:id" element={<EditPost />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/external" element={<ThirdParty />} />
      </Routes>
    </>
  );
}

export default App;