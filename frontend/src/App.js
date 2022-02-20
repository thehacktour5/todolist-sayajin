import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Hack's Todo List</h1>

      <form>
        <input type="text" placeholder="Write a message!"></input>
        <button type="submit">Add</button>
      </form>

      <ul className="todoList">
        <li>Item</li>
      </ul>

    </div>
  );
}

export default App;
