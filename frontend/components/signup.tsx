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

export default SignupCard;