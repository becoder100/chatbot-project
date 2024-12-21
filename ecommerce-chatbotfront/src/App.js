import React, { useState } from "react";
import Login from "./pages/Login";
import Home from "./pages/Home";

const App = () => {
  const [user, setUser] = useState(null);

  const handleLogin = (email) => {
    setUser(email);
  };

  return (
    <div>
      {user ? <Home /> : <Login onLogin={handleLogin} />}
    </div>
  );
};

export default App;
