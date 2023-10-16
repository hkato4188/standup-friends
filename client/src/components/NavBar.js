import React from "react";
import { NavLink, Link } from "react-router-dom";

//The NavLink changes the URL
//Route conditionally renders a component when the URL matches the pattern given

function NavBar({ updateUser, user }) {
  function handleLogout() {
    //   updateUser(null);
    //   fetch("http://127.0.0.1:5555/logout", { method: "DELETE" });
  }

  return (
    <div className="nav-container">
      <NavLink
        activeStyle={{ backgroundColor: "#7895CB" }}
        className="nav-btn nav-text"
        exact
        to="/about"
      >
        About
      </NavLink>
      <NavLink
        activeStyle={{ backgroundColor: "#7895CB" }}
        className="nav-btn nav-text"
        exact
        to="/discussionquestions"
      >
        Discussion Questions
      </NavLink>
      {user ? (
        <NavLink
          activeStyle={{ backgroundColor: "#7895CB" }}
          className="nav-btn nav-text"
          exact
          to="/groups"
        >
          Groups
        </NavLink>
      ) : null}
      {user ? (
        <NavLink
          activeStyle={{ backgroundColor: "#7895CB" }}
          exact
          className="nav-btn nav-text"
          to="/todolists"
        >
          ToDo Lists
        </NavLink>
      ) : null}
      {!user ? (
        <NavLink
          activeStyle={{ backgroundColor: "#7895CB" }}
          className="nav-btn nav-text"
          exact
          to="/login"
        >
          Login Signup
        </NavLink>
      ) : null}
      {user ? (
        <a
          activeStyle={{ backgroundColor: "#7895CB" }}
          className="nav-btn nav-text"
          href="/logout"
          onClick={handleLogout}
        >
          Logout
        </a>
      ) : null}
    </div>
  );
}

export default NavBar;
