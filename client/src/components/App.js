import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
// import ErrorPage from "./ErrorPage";
import GroupsPage from "./groupComponents/GroupsPage";
import ToDosPage from "./toDoComponents/ToDosPage";
import ToDoListDetail from "./toDoComponents/ToDoListDetail";
import Header from "./Header";
import NavBar from "./NavBar";
import Login from "./Login";
import DiscussionQuestions from "./DiscussionQuestions";
import About from "./About";
function App() {
  const [user, setUser] = useState(null);

  const fetchUser = () => {
    // 8.✅ Create a GET fetch that goes to '/auto_login'

    fetch("http://127.0.0.1:5555/auto_login").then((r) => {
      if (r.statusText !== "NO CONTENT") {
        r.json().then(setUser);
      } else {
        console.log("no user logged in");
      }
    });
  };

  useEffect(() => {
    fetchUser();
  }, []);
  const updateUser = (user) => setUser(user);

  // 9.✅ Return a second block of JSX
  // If the user is not in state return JSX and include <GlobalStyle /> <Navigation/> and  <Authentication updateUser={updateUser}/>

  return (
    <>
      <Header />
      {user ? <h4>Welcome {user.name}</h4> : null}
      <NavBar updateUser={updateUser} user={user} />
      <Switch>
        <Route exact path="/login">
          <Login updateUser={updateUser} />
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
        <Route exact path="/discussionquestions">
          <DiscussionQuestions />
        </Route>
        <Route exact path="/">
          <About />
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
