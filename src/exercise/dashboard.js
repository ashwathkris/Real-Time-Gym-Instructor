import React from "react";
import { useLocation } from "react-router-dom";
import Nav from "../home/nav"

const Dashboard=()=> {
  let {state} = useLocation();
  return (
    <div>
    <Nav />
    <div style={{position:"relative",left:"420px",margin:"20px"}}>
    <div style={{marginLeft:"180px",fontSize:"30px",fontFamily:"sans-serif",fontWeight:"bold"}}>Session Summary!</div>
    <div class="flex-container">
    <img src={`data:image/png;base64,${state}`} />
    </div>
    </div>
    </div>
  );
}

export default Dashboard;
