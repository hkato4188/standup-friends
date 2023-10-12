import React from "react";
import ToDoListCard from "./ToDoListCard";
import "../css/styles.css";

function ToDoListsContainer({ toDoLists }) {
  const renderedToDoLists = toDoLists.map((list) => {
    return <ToDoListCard key={list.id} list={list} />;
  });

  return <div className="flex-container">{renderedToDoLists}</div>;
}

export default ToDoListsContainer;
