import React from "react";
import { Switch, Route } from "react-router-dom";
// import ErrorPage from "./ErrorPage";
import GroupsPage from "./groupComponents/GroupsPage";
import ToDosPage from "./toDoComponents/ToDosPage";
import ToDoListDetail from "./toDoComponents/ToDoListDetail";
import Header from "./Header";
import NavBar from "./NavBar";
function App() {
  return (
    <>
      <Header />
      <NavBar />
      <Switch>
        <Route exact path="/groups">
          <GroupsPage />
        </Route>
        <Route exact path="/todolists">
          <ToDosPage />
        </Route>
        <Route exact path="/todolists/:id">
          <ToDoListDetail />
        </Route>
      </Switch>
    </>
  );
}

export default App;

// <Header />
//       <NavBar />
//       <Switch>
//         <Route exact path="/about">
//           <About />
//         </Route>
//         <Route exact path="/home">
//           <Home />
//         </Route>
//         <Route exact path="/groups">
//           <Groups />
//         </Route>
//         <Route exact path="/meetings">
//           <Meetings />
//         </Route>
//
//         <Route exact path="/">
//           <h1>Welcome to my app!</h1>
//         </Route>
//         <Route path="*">
//           <ErrorPage />
//         </Route>
//       </Switch>
