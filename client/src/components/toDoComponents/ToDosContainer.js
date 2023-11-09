import React, { useEffect, useState } from "react";
import ToDoList from "./ToDoList";
import Search from "../Search";
import "../css/styles.css";

function ToDosContainer() {
  const [toDoLists, setToDoLists] = useState([]);
  const [searchValue, setSearchValue] = useState("");
  useEffect(() => {
    fetch("/todolists")
      .then((response) => response.json())
      .then((data) => setToDoLists(data));
  }, []);

  function handleSearch(e) {
    setSearchValue(e.target.value);
  }

  function deleteList(id) {
    fetch(`/todolists/${id}`, {
      method: "DELETE",
    });
    let updatedToDoListData = toDoLists.filter((todoList) => {
      return todoList.id !== id;
    });
    setToDoLists(() => [...updatedToDoListData]);
  }

  // function addList(id) {
  //   fetch(`/todolists/${id}`, {
  //     method: "DELETE",
  //   });
  //   let updatedToDoListData = toDoLists.filter((todoList) => {
  //     return todoList.id !== id;
  //   });
  //   setToDoLists(() => [...updatedToDoListData]);
  // }

  function updateListOwner(lId, uId, list_owner) {
    fetch("/edit_list_owner", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        user_id: uId,
        list_id: lId,
      }),
    })
      .then((r) => r.json())
      .then((data) => {
        let result = toDoLists.map((tdl) => {
          if (tdl.id !== lId) {
            return tdl;
          } else {
            let result = tdl.users.filter((o) => o.id !== uId);
            return {
              ...data,
            };
          }
        });
        setToDoLists(result);
      });
  }

  const filteredToDoLists = toDoLists.filter((l) => {
    return (
      searchValue === "" || l.description.toLowerCase().includes(searchValue)
    );
  });
  const renderedToDoLists = filteredToDoLists.map((tdl) => {
    return (
      <ToDoList
        key={tdl.id}
        tdlist={tdl}
        onUpdateOwner={updateListOwner}
        onDelete={deleteList}
      />
    );
  });

  return (
    <>
      <div className="search-container">
        <Search onSearch={handleSearch} />
      </div>
      <div className="flex-container">{renderedToDoLists}</div>
    </>
  );
}

export default ToDosContainer;
