import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router";

export default function View() {
 const [form, setForm] = useState({
   title: "",
   short_description: "",
   description:"",
   preferred_Experience:"",
   records: [],
 });
 const params = useParams();
 const navigate = useNavigate();


 useEffect(() => {
  async function fetchData() {
    try {
      const response = await fetch(`http://127.0.0.1:8000/api/jobs/${params.id.toString()}`);
      if (!response.ok) {
        throw new Error(`An error has occurred: ${response.statusText}`);
      }
      const record = await response.json();
      console.log('record:', record);
      console.log('record title:', record["Job "].title);
      console.log('des:', record.description);
      setForm(record["Job "]);
    } catch (error) {
      console.error(error);
      window.alert(error.message);
      navigate('/');
    }
  }


  fetchData();
  
  return () => {
    console.log('cleanup');
  };
}, [params.id, navigate]);

  
 // This following section will display the form that takes input from the user to update the data.
 return (
   <div>
       <div className="form-group">
         <label htmlFor="title">Title: </label>
         <text> {form.title}
         </text>
       </div>
       <div className="form-group">
         <label htmlFor="description">Description: </label>
         <text> {form.description}
         </text>
        </div>         

        <div className="form-group">
         <label htmlFor="experience">Preferred Experience: </label>
         <text> {form.preferred_experience}
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
