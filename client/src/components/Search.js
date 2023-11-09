import React from "react";

function Search({ onSearch }) {
  return (
    <div className="searchbar">
      <label htmlFor="search">Search ToDo Lists: </label>

      <input
        type="text"
        id="search"
        placeholder="Type a name to search..."
        onChange={onSearch}
      />
    </div>
  );
}

export default Search;
