import React from "react";
import { useNavigate } from "react-router-dom";

const Nav = () =>{
  let navigate = useNavigate();
    return(
      <div className="ui menu">
      <div class="header item">
      <img style={{width:"60px",marginLeft:"2px"}} src="https://i.ibb.co/sVxhfm2/Screenshot-2022-02-12-at-9-46-42-PM.png" alt="Workflow" />
      <label style={{marginLeft:"15px",fontSize:"25px",fontFamily:"fantasy",color:"grey",fontWeight:"bold"}}>C-City </label>
      </div>
      <div style={{position:"relative",left:"825px"}}>
        <button style={{ margin:"20px",fontSize:"20px",color:"gray"}}
        onClick={()=>navigate("/home")}
        >Home</button>
        <button style={{ margin:"20px",fontSize:"20px",color:"gray"}} onClick={()=>navigate("/workout")}>Workouts</button>
                  <button style={{ margin:"20px",fontSize:"20px",color:"gray"}} onClick={()=>navigate("/createWorkouts")} >Create Workouts</button>
        </div>
      </div>
    );
}

export default Nav;