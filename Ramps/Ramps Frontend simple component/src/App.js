import React from "react";
import "./styles.css";
import Components from './component'

export default function App() {
  //let data =  ["helloworld", 0,"knock",1,2,3,"knock",4,5, "who'sThere"];
  //let data =  "hello World"
  let data = false;
  return (
    <div className="App">
      <h1>Ramp's simple React component</h1>
      <Components input = {data} ></Components>
    
    </div>
  );
}
