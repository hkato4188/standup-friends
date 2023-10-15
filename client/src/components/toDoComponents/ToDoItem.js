import React from "react";

function ToDoItem({ ...props }) {
  const { todo, onDelete } = props;
  const { completed, description, id } = todo;

  return (
    <div>
      <h4>Task:</h4>
      <p>{description}</p>

      <p>
        Complete: {completed}
        <button onClick={() => onDelete(id)}>
          <span>🗑️</span>
        </button>
      </p>
    </div>
  );
}

export default ToDoItem;
