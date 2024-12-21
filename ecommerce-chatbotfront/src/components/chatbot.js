import React, { useState, useEffect } from "react";

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  // Fetch product data when the component mounts
  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch("http://localhost:5000/api/product"); // Replace with your backend endpoint for products
        const products = await response.json();

        // Add the products as initial context to the messages
        const initialMessage = [
          { role: "system", content: "These are product information for my store, user can ask questions about it." },
          { role: "system", content: JSON.stringify(products) }
        ];
        console.log(products);
        setMessages(initialMessage); // Set the initial messages with product data
      } catch (error) {
        console.error("Error fetching products:", error);
      }
    };

    fetchProducts();
  }, []);

  const handleSend = async (event) => {
    if (event) event.preventDefault();
    if (input.trim() === "") return;

    const userMessage = { role: "user", content: input };

    // Add the user's message to the chat
    setMessages((prev) => [...prev, userMessage]);

    setInput(""); // Clear the input field

    // Send the user's message to the backend API, including the initial product data in the message array
    try {
      console.log(messages);
      const response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + localStorage.getItem("authToken")
        },
        body: JSON.stringify({
          messages: [
            ...messages, // Include existing messages (products and previous messages)
            userMessage, // Add the user's message
          ],
        }),
      });

      const data = await response.json();

      // Add the bot's response to the chat
      const botResponse = { role: "assistant", content: data.response };
      setMessages((prev) => [...prev, botResponse]); // Append only the bot response
    } catch (error) {
      console.error("Error sending message:", error);
    }
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      handleSend(event);
    }
  };

  const handleReset = () => {
    setMessages([]); // Clear the conversation
  };

  const handleLogout = () => {
    localStorage.removeItem("authToken"); // Clear the auth token from local storage
    window.location.reload(); // Reload the page
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500">
      <div className="w-full max-w-lg p-8 bg-white rounded-xl shadow-2xl backdrop-blur-lg bg-opacity-40">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-6">
          How can I assist you today?
        </h2>

        <div className="h-80 overflow-y-auto mb-6 p-4 rounded-lg bg-white shadow-md">
          {messages
            .filter((msg) => msg.role !== "system") // Filter out system messages
            .map((msg, index) => (
              <div
                key={index}
                className={`mb-3 ${msg.role === "user" ? "text-right" : "text-left"}`}
              >
                <p
                  className={`inline-block p-4 rounded-lg ${
                    msg.role === "user"
                      ? "bg-blue-600 text-white"
                      : "bg-gray-200 text-gray-800"
                  }`}
                >
                  <strong>{msg.content}</strong>
                </p>
              </div>
            ))}
        </div>

        <div className="flex gap-4 items-center mb-4">
          <input
            type="text"
            className="flex-1 p-4 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Ask me about products, sales, or support..."
          />
          <button
            className="bg-blue-600 text-white px-6 py-3 rounded-lg shadow-lg hover:bg-blue-700 focus:outline-none"
            onClick={handleSend}
          >
            Send
          </button>
        </div>

        <div className="flex justify-center gap-4 mb-4">
          <button
            className="bg-blue-600 text-white px-6 py-3 rounded-lg shadow-lg hover:bg-blue-700 focus:outline-none"
            onClick={handleReset}
          >
            Reset Chat
          </button>
          <button
            className="bg-red-600 text-white px-6 py-3 rounded-lg shadow-lg hover:bg-red-700 focus:outline-none"
            onClick={handleLogout}
          >
            Log Out
          </button>
        </div>

        <div className="mt-4 text-center text-sm text-gray-600">
          <p>
            <strong>Looking for a great deal?</strong> Ask me about our latest discounts and offers!
          </p>
        </div>
      </div>
    </div>
  );
};

export default Chatbot;
