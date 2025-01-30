import React from 'react';
import { useNavigate } from 'react-router-dom';
import LoginCard from '../components/LoginCard'; 

const LoginPage = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100">
      {/* Navigation */}
      <nav className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center">
              <button 
                onClick={() => navigate('/')}
                className="text-2xl font-bold text-blue-600 hover:text-blue-700"
              >
                Your App
              </button>
            </div>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900">Welcome Back!</h1>
          <p className="mt-2 text-gray-600">
            Don't have an account?{' '}
            <button
              onClick={() => navigate('/signup')}
              className="text-blue-600 hover:text-blue-500 font-medium"
            >
              Sign up
            </button>
          </p>
        </div>
        <LoginCard />
      </div>
    </div>
  );
};

export default LoginPage;