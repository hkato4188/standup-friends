import React, { useEffect, useState } from "react";
import ToDoListsContainer from "./ToDoListsContainer";

function ToDoListsPage() {
  const [toDoLists, setToDoLists] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5555/todolists")
      .then((response) => response.json())
      .then((data) => setToDoLists(data));
  }, []);

  return (
    <>
      <h1>You have reached the ToDo Lists Page:</h1>
      <ToDoListsContainer toDoLists={toDoLists} />
    </>
  );
}

export default ToDoListsPage;
