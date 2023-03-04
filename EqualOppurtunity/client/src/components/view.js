import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router";

export default function View() {
 const [form, setForm] = useState({
   name: "",
   position: "",
   level: "",
   records: [],
 });
 const params = useParams();
 const navigate = useNavigate();
 
 useEffect(() => {
   async function fetchData() {
     const id = params.id.toString();
     const response = await fetch(`http://localhost:5000/record/${params.id.toString()}`);
 
     if (!response.ok) {
       const message = `An error has occurred: ${response.statusText}`;
       window.alert(message);
       return;
     }
 
     const record = await response.json();
     if (!record) {
       window.alert(`Record with id ${id} not found`);
       navigate("/");
       return;
     }
 
     setForm(record);
   }
 
   fetchData();
 
   return;
 }, [params.id, navigate]);

 
 // These methods will update the state properties.
 
 // This following section will display the form that takes input from the user to update the data.
 return (
   <div>
       <div className="form-group">
         <label htmlFor="position">Position: </label>
         <text> {form.position}
         </text>
       </div>
       <div className="form-group">
         <label htmlFor="Location">Location: </label>
         <text> {form.city},
         </text>
         <text> {form.country}
         </text>
       </div>
       <br />

       <div className="form-group">
        <input
          type="submit"
          value="Apply"
          className="btn btn-primary"
          onClick={() => navigate(`/create?recordId=${params.id}`)}
        />
      </div>
   </div>
 );
}