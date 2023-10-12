import React from "react";
import "../css/styles.css";

function ToDoListCard({ list }) {
  const { id, description, items, users } = list;
  console.log(list);
  return (
    <div className="group-card outline">
      <h1>Description: {description}</h1>
      <h3>Owners:</h3>
      <p>
        {users.map((u) => (
          <>
            {u.name} | {u.email}
          </>
        ))}
      </p>

      <div>
        <ul>
          {items.map((i) => {
            return (
              <div>
                <p>Item:</p>
                <h5>Topic: {i.description} </h5>
                <h6>*Completed: {i.completed}</h6>
              </div>
            );
          })}
        </ul>
      </div>
    </div>
  );
}

export default ToDoListCard;
