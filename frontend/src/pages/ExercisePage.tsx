// src/pages/ExercisePage.tsx
import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import ExerciseComponent from "../components/ExerciseComponent";
import Navbar from "../components/Navbar";

const ExercisePage: React.FC = () => {
    const navigate = useNavigate();
    const { lessonCode } = useParams<{ lessonCode: string }>(); // Extract lesson code from URL
    const [username, setUsername] = useState('');
    const [isLoading, setIsLoading] = useState(true);
    
    useEffect(() => {
      const storedUsername = localStorage.getItem('username');
      if (storedUsername) {
        setUsername(storedUsername);
      }
      setIsLoading(false);
    }, []);
    
    const handleLogout = () => {
        localStorage.removeItem('token');
        localStorage.removeItem('username');
        navigate('/login');
    };
    
    // Optionally, if lessonCode is missing, you could redirect to /lessons.
    if (!lessonCode) {
      return <div>Error: Lesson code not specified.</div>;
    }
    
    return (
      <div>
          <Navbar username={username} handleLogout={handleLogout} />
          <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
              <h1 className="text-3xl font-bold mb-4">Math Exercise</h1>
              {/* Pass the lessonCode prop to the ExerciseComponent */}
              <ExerciseComponent lessonCode={lessonCode} />
          </div>
      </div>
    );
};

export default ExercisePage;
