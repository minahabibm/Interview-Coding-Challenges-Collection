import React, {useState, useEffect} from "react";

function Components(props){

  var [date,setDate] = useState(new Date());
  useEffect(() => {
    var timer = setInterval(()=>setDate(new Date()), 1000 )
    return function cleanup() {
      clearInterval(timer)
    }  
  });

  if ( typeof props.input === "undefined" || props.input === false){
    const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October" ,"November", "December"]
    const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return(
      <div>
        <p>{days[date.getDay()]}, {months[date.getMonth()]} {date.getDate()}, {date.getFullYear()} {date.toLocaleTimeString()}</p>
        <p> Date : {date.toLocaleDateString()}</p>
        <p> Time : {date.toLocaleTimeString()}</p>
      </div>
    );
  } else if (Array.isArray(props.input) === true){

    return(
      <ul>
        {props.input.map((data) => (
          <div>{data}</div>
        ))}
      </ul>
    );
  } else {
    return(
      <div>{props.input}</div>
    );
  };

};

export default Components;