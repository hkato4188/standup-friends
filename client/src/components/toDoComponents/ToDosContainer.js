import React, { useEffect, useState } from "react";
import ToDoList from "./ToDoList";
import "../css/styles.css";

function ToDosContainer() {
  const [toDoLists, setToDoLists] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5555/todolists")
      .then((response) => response.json())
      .then((data) => setToDoLists(data));
  }, []);

  const renderedToDoLists = toDoLists.map((tdl) => {
    return <ToDoList key={tdl.id} tdlist={tdl} />;
  });

  return <div className="flex-container">{renderedToDoLists}</div>;
}

export default ToDosContainer;
