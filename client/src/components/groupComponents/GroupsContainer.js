import React from "react";
import GroupCard from "./GroupCard";
import "../css/styles.css";

function GroupsContainer({ groups }) {
  const renderedGroups = groups.map((group) => {
    return <GroupCard key={group.id} group={group} />;
  });

  return <div className="flex-container">{renderedGroups}</div>;
}

export default GroupsContainer;
