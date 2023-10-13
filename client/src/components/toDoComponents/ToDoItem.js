import React from "react";

function ToDoItem({ tditem }) {
  const { completed, description, id } = tditem;
  console.log(tditem);
  return (
    <div>
      <h4>Task:</h4>
      <p>{description}</p>
      <p>Complete: {completed}</p>
    </div>
  );
}

export default ToDoItem;
