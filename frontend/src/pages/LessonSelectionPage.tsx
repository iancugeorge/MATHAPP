// src/pages/LessonSelectionPage.tsx
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";
import LessonItem from "../components/LessonItem.tsx"; // adjust the import path as needed
import { lessons } from "../types/SampleData"; // adjust the import path as needed

const LessonSelectionPage: React.FC = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");

  useEffect(() => {
    const storedUsername = localStorage.getItem("username");
    if (storedUsername) setUsername(storedUsername);
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("username");
    navigate("/login");
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 via-white to-blue-50 flex flex-col">
    {/* Navbar */}
    <Navbar username={username} handleLogout={handleLogout} />
  
    {/* Main content */}
    <main className="container mx-auto px-6 py-10 flex-grow">
      <h1 className="text-4xl font-extrabold text-center text-gray-900 mb-10 tracking-wide">
        Lecții
      </h1>
  
      {/* Render top-level lessons */}
      {lessons.map((lesson) => (
        <LessonItem key={lesson.id} lesson={lesson} />
      ))}
    </main>
  </div>
  
  );
};

export default LessonSelectionPage;
