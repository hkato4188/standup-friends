import React, { useContext } from "react";
import { NavLink, Link } from "react-router-dom";
import { UserContext } from "../context/user";


function NavBar() {
  const { user, updateUser } = useContext(UserContext);

  function handleLogout() {
    updateUser(null);
    fetch("/logout", { method: "DELETE" });
  }

  return (
    <div className="nav-container">
      <NavLink
        activeStyle={{ backgroundColor: "#7895CB" }}
        className="nav-btn nav-text"
        exact
        to="/"
      >
        About
      </NavLink>
      <NavLink
        activeStyle={{ backgroundColor: "#7895CB" }}
        className="nav-btn nav-text"
        exact
        to="/swansonquote"
      >
        Swanson Quote
      </NavLink>
      <NavLink
        activeStyle={{ backgroundColor: "#7895CB" }}
        className="nav-btn nav-text"
        exact
        to="/add_todolist"
      >
        Add ToDo List
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
