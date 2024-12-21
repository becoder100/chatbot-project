import React, { useState, useEffect } from "react";

const base_url = "http://localhost:5000"; // Replace with your backend domain

const LoginForm = ({ onLogin }) => {
  const [isSignUp, setIsSignUp] = useState(false); // State to toggle between login and sign-up
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState(""); // For sign-up
  const [name, setName] = useState(""); // For sign-up
  const [loading, setLoading] = useState(false); // Loading state for API calls
  const [message, setMessage] = useState(""); // Message state for feedback

  // Check if the user is logged in on component mount
  useEffect(() => {
    const token = localStorage.getItem("authToken");
    if (token) {
      // If token exists in localStorage, user is logged in, so skip login page
      onLogin(token); // Pass the token to parent component
    }
  }, [onLogin]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMessage("");

    if (isSignUp) {
      if (password !== confirmPassword) {
        setLoading(false);
        setMessage("Passwords do not match. Please try again.");
        return;
      }

      try {
        const response = await fetch(`${base_url}/signup`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ name, email, password, confirm_password: confirmPassword }),
        });
        const data = await response.json();
        setLoading(false);

        if (response.ok) {
          setMessage("Sign-up successful! Please log in.");
          setIsSignUp(false); // Switch to login mode
        } else {
          setMessage(data.message || "Sign-up failed.");
        }
      } catch (error) {
        setLoading(false);
        setMessage("An error occurred during sign-up.");
      }
    } else {
      try {
        const response = await fetch(`${base_url}/login`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email, password }),
        });
        const data = await response.json();
        setLoading(false);

        if (response.ok) {
          setMessage("Login successful!");
          localStorage.setItem("authToken", data.token); // Save the token to localStorage
          onLogin(data.token); // Pass the token to the parent component
        } else {
          setMessage(data.message || "Login failed.");
        }
      } catch (error) {
        setLoading(false);
        setMessage("An error occurred during login.");
      }
    }
  };

  return (
    <div className="max-w-sm mx-auto p-6 bg-white rounded-lg shadow-lg">
      <h2 className="text-3xl font-bold text-center mb-4">
        {isSignUp ? "Create an Account" : "Login"}
      </h2>

      {message && (
        <p className={`text-center mb-4 ${message.includes("successful") ? "text-green-500" : "text-red-500"}`}>
          {message}
        </p>
      )}

      <form onSubmit={handleSubmit} className="space-y-4">
        {isSignUp && (
          <div className="mb-4">
            <label className="block text-sm font-medium mb-1">Name</label>
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full border rounded-md p-2"
              required
            />
          </div>
        )}
        <div className="mb-4">
          <label className="block text-sm font-medium mb-1">Email</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full border rounded-md p-2"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium mb-1">Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full border rounded-md p-2"
            required
          />
        </div>

        {isSignUp && (
          <div className="mb-4">
            <label className="block text-sm font-medium mb-1">Confirm Password</label>
            <input
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              className="w-full border rounded-md p-2"
              required
            />
          </div>
        )}

        <button
          type="submit"
          className={`w-full py-2 rounded-md ${loading ? "bg-gray-400" : "bg-blue-500"} text-white`}
          disabled={loading}
        >
          {loading ? "Please wait..." : isSignUp ? "Sign Up" : "Login"}
        </button>
      </form>

      <div className="mt-4 text-center">
        <p className="text-sm text-gray-500">
          {isSignUp ? "Already have an account?" : "Don't have an account?"}
          <button
            onClick={() => setIsSignUp(!isSignUp)}
            className="text-blue-500 font-medium hover:underline ml-1"
          >
            {isSignUp ? "Login here" : "Sign up here"}
          </button>
        </p>
      </div>
    </div>
  );
};

export default LoginForm;
