import React from "react";
import "../css/styles.css";

function ToDoItem({ ...props }) {
  const { todo, onDelete, onEdit } = props;
  const { completed, description, id } = todo;

  return (
    <>
      <div className="inline">
        <span className="memo">🗒️ 📌 </span>
        <h2 className={completed ? "strikethrough" : "null"}>{description}</h2>
      </div>
      <div>
        <button
          className="todo-button"
          onClick={() => {
            onEdit(id, completed);
          }}
        >
          Complete:<span>✏️</span>
        </button>
        <button
          className="todo-button"
          onClick={() => {
            onDelete(id);
          }}
        >
          Delete: <span>🗑️</span>
        </button>
      </div>
    </>
  );
}

export default ToDoItem;
