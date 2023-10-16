import ToDosContainer from "./ToDosContainer";
import React, { useState, useEffect } from "react";

function ToDosPage() {
  const [inputText, setInputText] = useState("");

  return (
    <div>
      <h1>Let's get ToDo'in Stuff...</h1>

      <ToDosContainer />
    </div>
  );
}

export default ToDosPage;
