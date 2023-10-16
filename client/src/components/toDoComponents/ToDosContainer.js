import React, { useEffect, useState } from "react";
import ToDoList from "./ToDoList";
import "../css/styles.css";

function ToDosContainer() {
  const [toDoLists, setToDoLists] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/todolists")
      .then((response) => response.json())
      .then((data) => setToDoLists(data));
  }, []);

  function deleteList(id) {
    let updatedToDoListData = toDoLists.filter((todoList) => {
      return todoList.id !== id;
    });
    setToDoLists(() => [...updatedToDoListData]);
  }

  const renderedToDoLists = toDoLists.map((tdl) => {
    return <ToDoList key={tdl.id} tdlist={tdl} onDelete={deleteList} />;
  });

  return <div className="flex-container">{renderedToDoLists}</div>;
}

export default ToDosContainer;
