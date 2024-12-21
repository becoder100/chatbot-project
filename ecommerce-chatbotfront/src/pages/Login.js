import React from "react";
import LoginForm from "../components/LoginForm";

const Login = ({ onLogin }) => {
  return (
    <div className="h-screen flex items-center justify-center bg-gradient-to-r from-blue-200 via-purple-200 to-pink-200">
      <div className="backdrop-blur-xl bg-white/90 rounded-2xl shadow-xl p-8 w-full max-w-sm transform transition-all hover:scale-105 duration-300">
        <h2 className="text-4xl font-bold text-gray-800 text-center mb-6">
          Welcome Back
        </h2>
        <p className="text-center text-gray-600 font-bold mb-8">
          Please login to access your account.
        </p>
        <LoginForm onLogin={onLogin} />
        <div className="mt-6 text-center">
          <p className="text-sm text-gray-500 font-bold">
            Don't have an account?{" "}
            <a
              href="#"
              className="text-gray-800 font-medium hover:underline"
            >
              Sign up here
            </a>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Login;
