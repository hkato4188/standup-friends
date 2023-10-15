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

  function deleteList(id) {
    fetch(`http://localhost:5555/todolists/${id}`, {
      method: "DELETE",
    });
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
