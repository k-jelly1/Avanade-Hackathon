import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function Create() {
  const navigate = useNavigate();
  const recordId = new URLSearchParams(window.location.search).get("recordId");
  const [record, setRecord] = useState(null);
  const [form, setForm] = useState({
    first_name: "",
    middle_name: "",
    last_name: "",
    email_address: "",
    street_Address: "",
    street_Address1: "",
    city: "",
    postal_code: "",
    country: "",
    province: "",
    region: "",
    number: "",
  });

  useEffect(() => {
    async function fetchRecord() {
      const response = await fetch(`http://localhost:5000/record/${recordId}`);
      const data = await response.json();
      setRecord(data);
    }
    fetchRecord();
  }, [recordId]);

  function updateForm(value) {
    setForm((prev) => {
      return { ...prev, ...value };
    });
  }

  async function onSubmit(e) {
    e.preventDefault();
    const newCandidate = { ...form };
    await fetch(`http://localhost:5000/record/${recordId}/applications/add`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newCandidate),
    }).then((response) => {
      if (!response.ok) {
        throw new Error("Failed to add candidate.");
      }
      else {
        window.alert("Your Application is submitted successfully");
      }
      navigate("/");
    }).catch((error) => {
      window.alert(error.message);
    });
    setForm({
      first_name: "",
      middle_name: "",
      last_name: "",
      email_address: "",
      street_Address: "",
      street_Address1: "",
      city: "",
      postal_code: "",
      country: "",
      province: "",
      region: "",
      number: "",
    });
    navigate("/");
  }

  if (!record) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h3>Application</h3>
      <form onSubmit={onSubmit}>
        <div className="form-group">
          <label htmlFor="name">First Name</label>
          <input
            type="text"
            className="form-control"
            id="name"
            value={form.first_name}
            onChange={(e) => updateForm({ first_name: e.target.value })}
          />
        </div>
       
       
        <div className="form-group">
         <label htmlFor="name">Middle Name</label>
         <input
           type="text"
           className="form-control"
           id="name"
           value={form.middle_name}
           onChange={(e) => updateForm({ middle_name: e.target.value })}
         />
       </div>


       <div className="form-group">
         <label htmlFor="name">Last Name</label>
         <input
           type="text"
           className="form-control"
           id="name"
           value={form.last_name}
           onChange={(e) => updateForm({ last_name: e.target.value })}
         />
       </div>

       <div className="form-group">
         <label htmlFor="name">Email Address</label>
         <input
           type="text"
           className="form-control"
           id="name"
           value={form.email_address}
           onChange={(e) => updateForm({ email_address: e.target.value })}
         />
       </div>

       <div className="form-group">
         <label htmlFor="name">Street Address (line 1)</label>
         <input
           type="text"
           className="form-control"
           id="name"
           value={form.street_Address}
           onChange={(e) => updateForm({ street_Address: e.target.value })}
         />
       </div>

       <div className="form-group">
         <label htmlFor="name">Address (line 2)</label>
         <input
           type="text"
           className="form-control"
           id="name"
           value={form.street_Address1}
           onChange={(e) => updateForm({ street_Address1: e.target.value })}
         />
       </div>

       <div className="form-group">
         <label htmlFor="name">City</label>
         <input
           type="text"
           className="form-control"
           id="name"
           value={form.city}
           onChange={(e) => updateForm({ city: e.target.value })}
         />
       </div>

       <div className="form-group">
         <label htmlFor="name">Zip/Postal code</label>
         <input
           type="text"
           className="form-control"
           id="name"
           value={form.postal_code}
           onChange={(e) => updateForm({ postal_code: e.target.value })}
         />
       </div>

       <div className="form-group">
         <label htmlFor="name">Cellular Number</label>
         <input
           type="text"
           className="form-control"
           id="name"
           value={form.number}
           onChange={(e) => updateForm({ number: e.target.value })}
         />
       </div>

        <div className="form-group">
          <input
            type="submit"
            value="Submit"
            className="btn btn-primary"
          />
        </div>
      </form>
    </div>
  );
}


