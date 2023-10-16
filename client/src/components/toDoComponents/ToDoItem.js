import React from "react";
import "../css/styles.css";

function ToDoItem({ ...props }) {
  const { todo, onDelete, onEdit } = props;
  const { completed, description, id } = todo;

  return (
    <div>
      <h4>Task: </h4>

      <h4>Complete: {completed}</h4>
      <h2 className={completed ? "strikethrough" : "null"}>{description}</h2>
      <p>
        <button
          onClick={() => {
            onEdit(id, completed);
          }}
        >
          <span>✏️</span>
        </button>
        <button
          onClick={() => {
            onDelete(id);
          }}
        >
          <span>🗑️</span>
        </button>
      </p>
    </div>
  );
}

export default ToDoItem;
