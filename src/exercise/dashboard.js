import React,{useEffect,useState} from "react";
import { useLocation } from "react-router-dom";
import axios from "axios";
import { Line } from 'react-chartjs-2';

const Dashboard=()=> {
  const [check,setCheck] = useState(true);
  let {state} = useLocation();
//   console.log(state)
//   let final=[]
//   for(var i=0;i<state['x'].length;i++){
//       final.push({x:state['x'][i],y:state['y'][i]})
//   }
//   console.log(final)
console.log(state)
  return (
    <div class="flex-container">
    <img src={`data:image/png;base64,${state}`} />
    </div>
  );
}

export default Dashboard;
