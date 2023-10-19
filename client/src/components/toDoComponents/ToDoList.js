import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { UserContext } from "../../context/user";
import "../css/styles.css";

function ToDoList({ ...props }) {
  const { user } = useContext(UserContext);
  const { tdlist, onDelete, onUpdateOwner } = props;
  const { id, description, items, users } = tdlist;

  const list_owners = users.map((u) => {
    return (
      <React.Fragment key={u.id}>
        {u.name} | {u.email}
        <br></br>
      </React.Fragment>
    );
  });

  const owner_ids = users.map((m) => m.id);
  const list_owner = owner_ids.includes(user.id);

  return (
    <div
      className={
        list_owner ? "group-card outline-highlight" : "group-card outline"
      }
    >
      <h1>Description: {description}</h1>
      <h3>Owners:</h3>
      <div>{list_owners}</div>
      <h4>No. of items: {items.length}</h4>

      {items.slice(0, 3).map((td) => {
        return (
          <h5 key={td.id}>
            <span className="memo">🗒️</span> {td.description.substring(0, 40)}{" "}
            ...
          </h5>
        );
      })}

      <div className="button-container">
        <button
          className="toggle-button"
          onClick={() => onUpdateOwner(id, user.id, list_owner)}
        >
          {!list_owner ? "Join" : "Leave"}
        </button>

        {list_owner ? (
          <>
            <Link className="toggle-button" to={`/todolists/${id}`}>
              Get to work
            </Link>
            <button className="toggle-button" onClick={() => onDelete(id)}>
              Delete
            </button>
          </>
        ) : null}
      </div>
    </div>
  );
}

export default ToDoList;
