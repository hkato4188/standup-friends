import React from "react";
import { NavLink, Link } from "react-router-dom";

//The NavLink changes the URL
//Route conditionally renders a component when the URL matches the pattern given

function NavBar({ updateUser, user }) {
  const handleLogout = () => {
    updateUser(null);
    fetch("http://localhost:5555/logout", { method: "DELETE" });
  };

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
        <NavLink
          activeStyle={{ backgroundColor: "#7895CB" }}
          className="nav-btn nav-text"
          exact
          to="/logout"
          onClick={handleLogout}
        >
          Logout
        </NavLink>
      ) : null}
    </div>
  );
}

export default NavBar;
