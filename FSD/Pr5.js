Program: a
Counter_Func.jsx
import { useState } from "react";

const Counter_Func = () => {
  const [count, setCount] = useState(0);

  const increment = () => {
    setCount((prevCount) => prevCount + 1);
  };

  const decrement = () => {
    setCount((prevCount) => prevCount - 1);
  };

  return (
    <div>
      <h2>Counter</h2>
      <button onClick={decrement}>Decrement</button>
      <span style={{ margin: "0 10px" }}>{count}</span>
      <button onClick={increment}>Increment</button>
    </div>
  );
};

export default Counter_Func;



App.jsx

import React from "react";
import Counter_Func from "./Components/Counter_Func";
import "./App.css";

const App = () => {
  return (
    <div className="App">
      <Counter_Func />
    </div>
  );
};

export default App;



Program: b
Counter_Class.jsx
import { Component } from "react";

export class Counter_Class extends Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0,
    };
  }

  increment = () => {
    this.setState((prevState) => ({
      count: prevState.count + 1,
    }));
  };

  decrement = () => {
    this.setState((prevState) => ({
      count: prevState.count - 1,
    }));
  };

  render() {
    const { count } = this.state;
    return (
      <div>
        <h2>Counter by class component</h2>
        <button onClick={this.decrement}>Decrement</button>
        <span style={{ margin: "0 10px" }}>{count}</span>
        <button onClick={this.increment}>Increment</button>
      </div>
    );
  }
}

export default Counter_Class;

App.jsx
import React from "react";
import './App.css'
import Counter_Class from "./Components/Counter_Class";

const App = () => {
  return (
    <div className="App">
      <Counter_Class/>
    </div>
  );
};

export default App;

