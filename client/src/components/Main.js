import React, { useContext } from "react";
import { Switch, Route } from "react-router-dom";

import "./css/styles.css";

import NavBar from "./NavBar";
import Login from "./Login";
import About from "./About";
import GroupsPage from "./groupComponents/GroupsPage";
import ToDoListDetail from "./toDoComponents/ToDoListDetail";
import ToDosPage from "./toDoComponents/ToDosPage";

import { UserContext } from "../context/user";

import SwansonQuote from "./swansonComponents/SwansonQuote";
import AddToDoList from "./toDoComponents/AddToDoList";

function Main() {
  const { user } = useContext(UserContext);

  return (
    <div>
      <NavBar />
      <h4 className="user-name">User: {user.name}</h4>
      <Switch>
        <Route exact path="/login">
          <Login />
        </Route>
        <Route exact path="/groups">
          <GroupsPage />
        </Route>
        <Route exact path="/todolists">
          <ToDosPage />
        </Route>
        <Route exact path="/todolists/:id">
          <ToDoListDetail />
        </Route>
        <Route exact path="/add_todolist">
          <AddToDoList />
        </Route>
        <Route exact path="/">
          <About />
        </Route>
        <Route exact path="/swansonquote">
          <SwansonQuote />
        </Route>
      </Switch>
    </div>
  );
}

export default Main;
