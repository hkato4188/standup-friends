import React from "react";
import { Link } from "react-router-dom";

import "../css/styles.css";

function ToDoList({ ...props }) {
  const { tdlist, onDelete } = props;
  const { id, description, items, users } = tdlist;

  const list_owners = users.map((u) => {
    return (
      <React.Fragment key={u.id}>
        {u.name} | {u.email}
        <br></br>
      </React.Fragment>
    );
  });

  return (
    <div className="group-card outline">
      <h1>Description: {description}</h1>
      <h3>Owners:</h3>
      <div>{list_owners}</div>
      <h4>No. of items: {items.length}</h4>
      <ul>
        {items.map((td) => {
          return <li key={td.id}>🗒️ {td.description.substring(0, 40)} ...</li>;
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
