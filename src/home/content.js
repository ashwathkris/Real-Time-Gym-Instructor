import React from "react";
import { useNavigate } from "react-router-dom";
import Card from './card'


var data=[
{"title":"Left Bicep Curl","description":"The biceps curl mainly targets the biceps brachii, brachialis and brachioradialis muscles.","image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTW4NAe4BA8gQx3WoVZ1p0e9ydmRnk6GLu59w&usqp=CAU"},
{"title":"Right Bicep Curl","description":"The biceps curl mainly targets the biceps brachii, brachialis and brachioradialis muscles.","image":"https://barbend.com/wp-content/uploads/2019/10/bicep-curl-featured.jpg"},
{"title":"Plank","description":"The biceps curl mainly targets the biceps brachii, brachialis and brachioradialis muscles.","image":"https://fitandelegant.com/wp-content/uploads/2019/10/What-is-Plank-Exercise-and-why-is-it-Effective.jpg"},
{"title":"Pushups","description":"The biceps curl mainly targets the biceps brachii, brachialis and brachioradialis muscles.","image":"https://strengthbuzz.com/wp-content/uploads/2020/01/Push-Up-Workout.jpg"},
]

const Content = () =>{
    let navigate = useNavigate();
    return(
        <div>
        <div style={{marginLeft:"25px",fontSize:"30px",fontFamily:"sans-serif",fontWeight:"bold"}}>Recommended</div>
        <div style={{alignItems: "Stretch",display: "flex",flexDirection: "row",flexWrap: "nowrap",overflowX: "auto",overflowY: "hidden",padding:"10px",margin:"10px"}}>
        {data.map((item)=><Card data={item}  />)}
</div>
</div>
    );
}

export default Content