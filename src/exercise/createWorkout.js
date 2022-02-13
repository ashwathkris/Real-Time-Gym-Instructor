import axios from "axios";
import React,{useRef,useState} from "react";
import { useLocation } from "react-router-dom";
import Nav from "../home/nav"

const CreateWorkout=()=> {
  let {state} = useLocation();
  const imageInput = useRef();
  const [file, setFile] = useState({});

  const handleImage = (e) => {
    const formData = new FormData();
    formData.append('file', e.target.files[0])
    console.log(formData)
    // setFile(formData)
  };

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
  <div className="ui small input focus" style={{ margin: '10px' }}>
  <input
    type="file"
    onChange={handleImage}
  />
</div>
  </div>
</div>
</div>
</div>
  );
}

export default CreateWorkout;
