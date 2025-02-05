// App.tsx
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import SignupPage from './pages/SignupPage';
import DashboardPage from './pages/DashboardPage';
import LessonSelectionPage from './pages/LessonSelectionPage';
import ExercisePage from './pages/ExercisePage';
import { useState } from 'react';
import './index.css';

const queryClient = new QueryClient();

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(() => {
    return localStorage.getItem('token') !== null;
  });

  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <div className="min-h-screen bg-gray-100">
          <Routes>
            {/* Public routes */}
            <Route path="/" element={<HomePage />} />
            <Route 
              path="/login" 
              element={isAuthenticated ? <Navigate to="/dashboard" /> : <LoginPage />} 
            />
            <Route 
              path="/signup" 
              element={isAuthenticated ? <Navigate to="/dashboard" /> : <SignupPage />} 
            />
            
            {/* Protected routes */}
            <Route
              path="/dashboard"
              element={isAuthenticated ? <DashboardPage /> : <Navigate to="/login" />}
            />

            {/* Route for Lesson Selection Page */}
            <Route 
              path="/lessons" 
              element={isAuthenticated ? <LessonSelectionPage /> : <Navigate to="/login" />} 
            />
  
            {/* Route for Dedicated Exercise Page */}
            <Route 
              path="/exercise/:lessonCode" 
              element={isAuthenticated ? <ExercisePage /> : <Navigate to="/login" />} 
            />            
          </Routes>
        </div>
      </Router>
    </QueryClientProvider>
  );
}

export default App;