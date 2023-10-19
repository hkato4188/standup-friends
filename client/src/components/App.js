import React from "react";
import Authenticate from "./Authenticate";
import { UserProvider } from "../context/user";
import Header from "./Header";
function App() {
  return (
    <UserProvider>
      <Header />
      <Authenticate />
    </UserProvider>
  );
}

export default App;
