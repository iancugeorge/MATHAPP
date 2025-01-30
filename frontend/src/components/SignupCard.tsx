<<<<<<< HEAD:frontend/components/signup.tsx
import React from 'react';
import { Link } from 'react-router-dom';
import '../src/index.css';
import "../css/signup.css"

const SignupCard = () => {

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // Handle form submission logic here
  };
  return (
    <div className="w-[1280px] h-[720px] bg-white">
      <div className="flex h-full">
        <div className="w-1/2 relative">
          <img
            src="../imagini/loginMic.png"
            alt="Signup illustration"

            className="w-full h-full" 
          />
          <div className="absolute top-1/2 left-8">
            <h2 className="text-2xl text-white">Welcome to <br />MATHAPP!</h2>
            <p className="text-white">
              Create an account to get started with our amazing features and exclusive content.
            </p>
          </div>
        </div>
        <div className="w-1/2 p-8">
          <form onSubmit={handleSubmit}>
            <input
              id="username"
              type="text"
              placeholder="Enter your username"
              required
              className="w-full px-3 py-2 border"
            />
            <input
              id="email"
              type="email"
              placeholder="Enter your email"
              required
              className="w-full px-3 py-2 border mt-6"
            />
            <input
              id="password"
              type="password"
              placeholder="Create a password"
              required
              className="w-full px-3 py-2 border mt-6"
            />
            <button
              type="submit"

              className="w-full bg-blue-600 text-white py-2 mt-6"
            >
              Sign Up
            </button>
            <p className="text-center mt-6">
              Ai deja un cont? 
              <Link to="/loginpage" className="text-blue-600">
                Logheaza-te!
              </Link>
            </p>
          </form>
        </div>
      </div>
    </div>
  );
};

=======
import React, { useState } from 'react';
import '../index.css';

const SignupCard = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: ''
  });
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.id]: e.target.value
    });
    // Clear any previous messages when user starts typing
    setError('');
    setSuccess('');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError('');
    setSuccess('');

    try {
      const response = await fetch('http://localhost:8000/auth/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || 'Registration failed');
      }

      setSuccess('Registration successful! You can now log in.');
      setFormData({ username: '', email: '', password: '' }); // Clear form
    } catch (err) {
      setError(err.message || 'An error occurred during registration');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="w-full max-w-4xl mx-auto bg-white rounded-lg shadow-lg overflow-hidden">
      <div className="flex min-h-[500px]">
        {/* Left side - Image and text */}
        <div className="w-1/2 bg-slate-100 p-8 flex flex-col justify-center">
          <img 
            src="../imagini/loginMic.jpg" 
            alt="Signup illustration" 
            className="mb-6 rounded-lg w-full object-cover"
          />
          <h2 className="text-2xl font-bold mb-2">Join Our Community</h2>
          <p className="text-slate-600">
            Create an account to get started with our amazing features and exclusive content.
          </p>
        </div>

        {/* Right side - Form */}
        <div className="w-1/2 p-8">
          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <label htmlFor="username" className="block text-sm font-medium mb-2">
                Username
              </label>
              <input
                id="username"
                type="text"
                placeholder="Enter your username"
                required
                value={formData.username}
                onChange={handleChange}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            <div>
              <label htmlFor="email" className="block text-sm font-medium mb-2">
                Email
              </label>
              <input
                id="email"
                type="email"
                placeholder="Enter your email"
                required
                value={formData.email}
                onChange={handleChange}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            <div>
              <label htmlFor="password" className="block text-sm font-medium mb-2">
                Password
              </label>
              <input
                id="password"
                type="password"
                placeholder="Create a password"
                required
                value={formData.password}
                onChange={handleChange}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            {error && (
              <div className="text-red-600 text-sm">{error}</div>
            )}
            {success && (
              <div className="text-green-600 text-sm">{success}</div>
            )}

            <button
              type="submit"
              disabled={isLoading}
              className={`w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 ${
                isLoading ? 'opacity-50 cursor-not-allowed' : ''
              }`}
            >
              {isLoading ? 'Signing Up...' : 'Sign Up'}
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

>>>>>>> 4f91665df22fee19ad2b27f165fe5515af8d1f3d:frontend/src/components/SignupCard.tsx
export default SignupCard;