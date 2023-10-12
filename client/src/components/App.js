import React from "react";
import { Switch, Route } from "react-router-dom";
// import ErrorPage from "./ErrorPage";
import GroupsPage from "./groupComponents/GroupsPage";
import ToDoListsPage from "./listComponents/ToDoListsPage";

function App() {
  return (
    <>
      <Switch>
        <Route exact path="/groups">
          <GroupsPage />
        </Route>
        <Route exact path="/todo_lists">
          <ToDoListsPage />
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
