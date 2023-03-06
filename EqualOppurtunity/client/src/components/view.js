import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router";
import "./view.css";

export default function View() {
  const [form, setForm] = useState({
    title: "",
    job_overview: "",
    description:"",
    requirments:"",
    good_to_have: "",
    benefits: "",
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
        console.log('record title:', record["Job"].title);
        console.log('des:', record.description);
        setForm(record["Job"]);
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

  return (
    <div className="container">
      <div className="card">
        <h1 className="title">{form.title}</h1>
        <div className="label">Job Overview:</div>
          <div className="value">{form.job_overview}</div>
        <div className="form-group">
          <div className="label">Requirments:</div>
          <div className="value">{form.requirments}</div>
        </div>
        <div className="form-group">
          <div className="label">Good To Have</div>
          <div className="value">{form.good_to_have}</div>
        </div>
        <div className="form-group">
          <div className="label">Benefits:</div>
          <div className="value">{form.benefits}</div>
        </div>
        <div className="button-container">
          <button className="button" onClick={() => navigate(`/create?recordId=${params.id}`)}>
            Apply
          </button>
        </div>
      </div>
    </div>
  );
}
