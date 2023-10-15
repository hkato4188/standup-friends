import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import ToDoItem from "./ToDoItem";
import "../css/styles.css";

function ToDoListDetail() {
  const { id } = useParams();
  const [toDos, setToDos] = useState([]);
  const [inputText, setInputText] = useState("");
  useEffect(() => {
    fetch(`http://localhost:5555/todolists/${id}`)
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
      fetch(`http://localhost:5555/todos`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          description: inputText,
          list_id: id,
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
    fetch(`http://localhost:5555/todos/${id}`, {
      method: "DELETE",
    });
    let updatedToDoData = toDos.filter((todo) => {
      return todo.id !== id;
    });
    setToDos(() => [...updatedToDoData]);
  }

  const toDoItemArray = toDos.map((td) => {
    return <ToDoItem key={td.id} todo={td} onDelete={deleteItem} />;
  });

  return (
    <div className="group-card outline">
      <h1>Hello</h1>
      <hr></hr>
      {toDoItemArray}
      <input onChange={handleChange} type="text" value={inputText} />
      <button onClick={addItem}>
        <span>Add</span>
      </button>
    </div>
  );
}

export default ToDoListDetail;
