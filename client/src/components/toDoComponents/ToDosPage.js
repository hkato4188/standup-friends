import ToDosContainer from "./ToDosContainer";
import React from "react";

import "../css/styles.css";

function ToDosPage() {
  return (
    <div>
      <h1 style={{ textAlign: "center" }}>
        📐📚📋🖌️🗂️📌📘 Things ToDo! 🖍️🗒️📒📏📕📓✏️
      </h1>
      <ToDosContainer />
    </div>
  );
}

export default ToDosPage;
