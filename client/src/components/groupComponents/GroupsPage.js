import React, { useEffect, useState } from "react";
import GroupsContainer from "./GroupsContainer";
import "../css/styles.css";
function GroupsPage() {
  const [groups, setGroups] = useState([]);

  useEffect(() => {
    fetch("/groups")
      .then((response) => response.json())
      .then((data) => setGroups(data));
  }, []);

  return (
    <>
      <h1>You have reached the Groups Page:</h1>
      <GroupsContainer groups={groups} />

      <div style={{ display: "grid", placeItems: "center" }}>
        <h1 style={{ textAlign: "center" }}>
          📐📚📋🖌️🗂️📌📘 Groups 🖍️🗒️📒📏📕📓✏️
        </h1>
      </div>
    </>
  );
}

export default GroupsPage;
