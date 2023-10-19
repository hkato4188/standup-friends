import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import ToDoItem from "./ToDoItem";
import "../css/styles.css";

function ToDoListDetail() {
  const { id } = useParams();
  const [toDos, setToDos] = useState([]);
  const [inputText, setInputText] = useState("");

  useEffect(() => {
    fetch(`/todolists/${id}`)
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw response;
      })
      .then((data) => setToDos(data))
      .catch((error) => {
        console.error("Error fetching data: ", error);
      });
  }, [id]);

  function handleChange(e) {
    const newInput = e.target.value;
    setInputText(newInput);
  }

  function addItem(e) {
    e.preventDefault();
    if (inputText !== "") {
      fetch(`/todos`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          description: inputText,
          list_id: parseInt(id),
        }),
      })
        .then((r) => r.json())
        .then((data) => {
          setToDos([...toDos, data]);
        })
        .then(setInputText(""));
    }
  }

  function deleteItem(id) {
    fetch(`/todos/${id}`, {
      method: "DELETE",
    });
    let updatedToDoData = toDos.filter((todo) => {
      return todo.id !== id;
    });
    setToDos(() => [...updatedToDoData]);
  }

  function updateCompleteStatus(id, status) {
    let result = toDos.map((td) => {
      if (td.id !== id) {
        return td;
      } else {
        return {
          ...td,
          completed: status,
        };
      }
    });
    setToDos(result);
  }

  function editItem(id, status) {
    let tdCompletedPatch = !status;

    fetch(`/todos/${id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        completed: tdCompletedPatch,
      }),
    }).then(() => {
      updateCompleteStatus(id, tdCompletedPatch);
    });
  }

  const toDoItemArray = toDos.map((td) => {
    return (
      <ToDoItem key={td.id} todo={td} onDelete={deleteItem} onEdit={editItem} />
    );
  });

  return (
    <div className="list-div">
      <hr></hr>
      <div className="list-card">
        {toDoItemArray}
        <input onChange={handleChange} type="text" value={inputText} />
        <button onClick={addItem}>
          <span>Add</span>
        </button>
      </div>
    </div>
  );
}

export default ToDoListDetail;
