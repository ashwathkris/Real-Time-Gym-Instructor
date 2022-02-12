import React from "react";
import { useNavigate } from "react-router-dom";


const Card = ({data}) =>{
    let navigate = useNavigate();
    return(
        <div class="grid grid-flow-col auto-cols-max" style={{marginRight:"30px"}}>
        <div class="max-w-sm bg-white  border border-gray-100 shadow-md dark:bg-white-800 dark:border-gray-200">
        <img  src={data['image']} width="100%"/>
    <div class="p-5" >
        <h5 class="mb-2 text-2xl font-bold tracking-tight " style={{margin:"10px"}}>{data['title']}</h5>
        <p class="mb-3 font-normal  dark:text-gray-500" style={{margin:"10px"}}>{data['description']}</p>
        <button style={{margin:"10px"}} onClick={()=>{
            navigate("/exercise",{state:data['title']})
        }} className="ui medium basic right labeled icon purple button" >
        <i class="right arrow icon"></i>
            Start Exercise
        </button>
    </div>
</div>
</div>
    );
}

export default Card