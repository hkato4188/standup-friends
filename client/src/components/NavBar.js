import React from "react";
import { NavLink } from "react-router-dom";

//The NavLink changes the URL
//Route conditionally renders a component when the URL matches the pattern given

function NavBar() {
  return (
    <div className="nav-container">
      <NavLink
        activeStyle={{ backgroundColor: "#7895CB" }}
        className="nav-btn nav-text"
        exact
        to="/groups"
      >
        Groups
      </NavLink>
      <NavLink
        activeStyle={{ backgroundColor: "#7895CB" }}
        exact
        className="nav-btn nav-text"
        to="/todolists"
      >
        ToDo Lists
      </NavLink>
    </div>
  );
}

export default NavBar;
