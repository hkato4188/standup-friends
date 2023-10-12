import React from "react";
import "../css/styles.css";

function GroupCard({ group }) {
  const { id, name, meetings, members } = group;

  return (
    <div className="group-card outline">
      <h1>Group Name: {name}</h1>
      <div>
        <ul>
          {meetings.map((m) => {
            return <p>Meeting Topic: {m.topic}</p>;
          })}
        </ul>
        <ul>
          {members.map((m) => {
            return <p>Attendees: {m.name}</p>;
          })}
        </ul>
      </div>
    </div>
  );
}

export default GroupCard;
