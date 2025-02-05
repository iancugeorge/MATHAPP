import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from "../components/Navbar";

const DashboardPage = () => {
  const navigate = useNavigate();
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

  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-gray-600">Loading...</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Navigation */}
      <Navbar username={username} handleLogout={handleLogout} />

      {/* Main Content */}
      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="px-4 py-6 sm:px-0">
          <div className="bg-white shadow rounded-lg p-6">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">Dashboard</h2>
            
            {/* Dashboard Content */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {/* Example Card 1 */}
              <div className="bg-blue-50 p-6 rounded-lg">
                <h3 className="text-lg font-semibold text-blue-900 mb-2">Welcome!</h3>
                <p className="text-blue-700">
                  This is your personal dashboard. You can add your content here.
                </p>
              </div>

              {/* Example Card 2 */}
              <div className="bg-green-50 p-6 rounded-lg">
                <h3 className="text-lg font-semibold text-green-900 mb-2">Your Profile</h3>
                <p className="text-green-700">
                  Email: {username}
                </p>
              </div>

              {/* Example Card 3 */}
              <div className="bg-purple-50 p-6 rounded-lg">
                <h3 className="text-lg font-semibold text-purple-900 mb-2">Invata</h3>
                <button 
                  className="mt-2 bg-purple-600 text-black px-4 py-2 rounded-md hover:bg-purple-700 transition-colors"
                  onClick={() => {navigate('/lessons')}}
                >
                  Lectii
                </button>
                <div></div>
                <button 
                  className="mt-2 bg-purple-600 text-black px-4 py-2 rounded-md hover:bg-purple-700 transition-colors"
                  onClick={() => {navigate('/exercise/1')}}
                >
                  Exercitiu
                </button>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default DashboardPage;