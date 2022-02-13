import axios from "axios";
import React,{useRef,useState} from "react";
import { useLocation } from "react-router-dom";
import Nav from "../home/nav"

const CreateWorkout=()=> {
  let {state} = useLocation();
  const imageInput = useRef();
  const [file, setFile] = useState({});
  const [count, setCount] = useState(0);


  return (
    <div>
    <Nav />
    <div style={{display:"block",
      marginTop: "50px",
      marginLeft: "10px",
      marginRight:"0px",
      width: "100%"}}>
    <div class="flex flex-row w-full" >
  <div class="grid flex-grow h-32 w-15 card bg-base-300 rounded-box place-items-center" > 
  <img src="/pose.png" alt="pose" height="100%"/>
  </div> 
  <div class="divider divider-vertical"></div> 
  <div class="grid flex-grow h-32  card bg-base-300 rounded-box place-items-center" style={{marginRight:"70px"}}>
  <div  className="ui  input">
  <input 
  type="text"
  placeholder="Name of Exercise"
  onChange={(e)=>{setFile({...file,"title":e.target.value})}}
  />
  </div>
  <div className="ui small input focus" style={{ margin: '10px' }}>
  <input
    type="file"
    onChange={(e)=>{setFile({...file,"image":e.target.files[0]})}}
  />
</div>
<div  className="ui small  input">
  <input 
  type="number"
  placeholder="Enter no of joints"
  onChange={(e)=>{setCount(e.target.value)}}
  />
  </div>
  <div>
    {(count)?Array(count*3).fill().map((val,index)=>(<div>
        <div className="ui small input focus" style={{ margin: '10px' }}>
              <input
                type="text"
                placeholder="Point"
              />
            </div>
        </div>)):null}
    </div>
    <div style={{margin: '10px'}}>
        <button className="ui big green button">
        Create Exercise
        </button>
    </div>
  </div>
</div>
</div>
</div>
  );
}

export default CreateWorkout;
