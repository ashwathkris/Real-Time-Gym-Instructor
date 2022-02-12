import React,{useEffect,useState} from "react";
import video from '../utils/test.mp4'

const Exercise=()=> {
  const [check,setCheck] = useState(true);

  return (
    <div>
    {(check)?
    <video width="750" height="500" autoPlay muted onEnded={()=>{
      setCheck(false)
    }}>
      <source src={video}  type="video/mp4"/>
    </video>:<img src="http://127.0.0.1:5000/video_feed" width="750" height="500"/>
  }
    </div>
  );
}

export default Exercise;
