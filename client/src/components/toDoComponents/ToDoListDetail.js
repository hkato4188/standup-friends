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
      .then((response) => response.json())
      .then((data) => setToDos(data));
  }, [id]);

  const renderedToDos = toDos.map((td) => {
    return <ToDoItem key={td.id} tditem={td} />;
  });

  function handleChange(e) {
    const newInput = e.target.value;
    setInputText(newInput);
  }

  function addItem(e) {
    e.preventDefault();
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

  return (
    <div className="group-card outline">
      <h1>Hello</h1>
      <hr></hr>
      {renderedToDos}
      <input onChange={handleChange} type="text" value={inputText} />
      <button onClick={addItem}>
        <span>Add</span>
      </button>
    </div>
  );
}

export default ToDoListDetail;
