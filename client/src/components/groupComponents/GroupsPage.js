import React, { useEffect, useState } from "react";
import GroupsContainer from "./GroupsContainer";

function GroupsPage() {
  const [groups, setGroups] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/groups")
      .then((response) => response.json())
      .then((data) => setGroups(data));
  }, []);

  return (
    <>
      <h1>You have reached the Groups Page:</h1>
      <GroupsContainer groups={groups} />
    </>
  );
}

export default GroupsPage;
