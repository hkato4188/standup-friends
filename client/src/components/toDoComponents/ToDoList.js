import React from "react";
import { Link } from "react-router-dom";

import "../css/styles.css";

function ToDoList({ ...props }) {
  const { tdlist, onDelete } = props;
  const { id, description, items, users } = tdlist;

  const list_owners = users.map((u) => {
    return (
      <>
        {u.name} | {u.email}
        <br></br>
      </>
    );
  });

  return (
    <div className="group-card outline">
      <h1>Description: {description}</h1>
      <h3>Owners:</h3>
      <p>{list_owners}</p>
      <h4>No. of items: {items.length}</h4>
      <ul>
        {items.map((td) => {
          return <div>🗒️ {td.description.substring(0, 40)} ...</div>;
        })}
      </ul>
      <button>
        <Link to={`/todolists/${id}`}>Get to work!</Link>
      </button>
      <button onClick={() => onDelete(id)}>Delete</button>
    </div>
  );
}

export default ToDoList;
