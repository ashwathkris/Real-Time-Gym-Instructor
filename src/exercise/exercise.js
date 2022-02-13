import React,{useState,useRef} from "react";
import video from '../utils/test.mp4'
import { useLocation } from "react-router-dom";
import { Navigate, useNavigate } from "react-router-dom";
import axios from "axios";
import Nav from "../home/nav"


const Exercise=()=> {
  const [check,setCheck] = useState(true);
  const [start,setStart] = useState(true); 

  let navigate = useNavigate();
  const vid = useRef(null)
  const [seconds, setSeconds] = useState(0)

    const startTimer = () => {
            setInterval(() => {
                setSeconds(seconds => seconds + 1)
            }, 1000)
    }
  let {state} = useLocation();
  var source=`http://127.0.0.1:5000/video_feed?key=${state}`
  console.log(source)
  return (
    <div>
    <Nav />
    <div style={{display:"block",
      marginTop: "20px",
      marginLeft: "20px",
      marginRight:"0px",
      width: "100%"}}>
    <div class="flex flex-row w-full" >
  <div class="grid flex-grow h-32 w-45 card bg-base-300 rounded-box place-items-center" >{(check)?
    <video ref={vid} style={{objectFit:"cover"}}  width="900" height="500" muted onEnded={()=>{
      startTimer()
      setCheck(false)
    }}>
      <source    src={video}  type="video/mp4"/>
    </video>:<img src={source} width="900" height="500"/>
  }</div> 
  <div class="divider divider-vertical"></div> 
  <div class="grid flex-grow h-32 w-25 card bg-base-300 rounded-box place-items-center" style={{marginRight:"70px"}}>
  <div>{(start)?<div style={{fontSize:"100px",fontWeight:"bold"}}>00:00</div>:<div style={{fontSize:"100px",fontWeight:"bold"}}>{ new Date(seconds * 1000).toISOString().substr(14, 5)}</div>}</div>
  {(start)?<div style={{marginTop:"50px"}}>
  <button class="ui big purple button" onClick={()=>{
    setStart(false)
    vid.current && vid.current.play();
  }}>Start Exercise</button>
  </div>:
  <div style={{marginTop:"50px"}}>
  <button class="ui big red button" onClick={()=>{
    clearInterval(setSeconds(0))
    axios.get(`http://127.0.0.1:5000/results?key=${state}`).then((res)=>{
      navigate("/dashboard",{ state:res.data })
    })
  }}>End Exercise</button>
  </div>}

  </div>
</div>
</div>
</div>
  );
}

export default Exercise;
