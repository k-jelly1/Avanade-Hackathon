import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./create.css";

export default function Create() {
  const navigate = useNavigate();
  const recordId = new URLSearchParams(window.location.search).get("recordId");
  const [record, setRecord] = useState(null);
  const [form, setForm] = useState({
    job_id: 0,
    q1: "",
    q2: "",
    q3: "",
    q4: "",
    resume: null,
  });

  useEffect(() => {
    async function fetchRecord() {
      const response = await fetch(`http://localhost:8000/api/jobs/${recordId}/`);
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
    const formData = new FormData();
    formData.append("job_id", recordId);
    formData.append("q1", form.q1);
    formData.append("q2", form.q2);
    formData.append("q3", form.q3);
    formData.append("q4", form.q4);
    formData.append("pdfFile", form.resume);
    
    await fetch(`http://127.0.0.1:8001/api/resumes/apply/`, {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to add candidate.");
        } else {
          window.alert("Your Application is submitted successfully");
        }
        navigate("/");
      })
      .catch((error) => {
        window.alert(error.message);
      });
    setForm({
      job_id: 0,
      q1: "",
      q2: "",
      q3: "",
      q4: "",
      resume: null,
    });
  }

  console.log (form);
  if (!record) {
    return <div>Loading...</div>;
  }

  return (
    <div className="container">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <h3 className="form-title">Application</h3>
          <form
            className="application-form"
            method="post"
            encType="multipart/form-data"
            onSubmit={onSubmit}
          >
        <div className="form-group">
          <label htmlFor="skills">1. Please provide a list of your relevant skills based on the job description.</label>
          <input
            type="text"
            className="form-control"
            id="skills"
            value={form.skills}
            onChange={(e) => updateForm({ skills: e.target.value })}
          />
        </div>
        <div className="form-group">
          <label htmlFor="motivation">2. What motivated you to apply for this job? We'd love to hear about your interest and enthusiasm for this position.</label>
          <textarea
            className="form-control"
            id="motivation"
            value={form.motivation}
            onChange={(e) => updateForm({ motivation: e.target.value })}
          ></textarea>
        </div>
        <div className="form-group">
          <label htmlFor="culture">3. Our company has a unique culture and values. Can you describe how your skills and experiences align with our company's culture?</label>
          <textarea
            className="form-control"
            id="culture"
            value={form.culture}
            onChange={(e) => updateForm({ culture: e.target.value })}
          ></textarea>
        </div>
        <div className="form-group">
          <label htmlFor="experience">4. How many years of experience do you have in this field or related areas?</label>
          <input
            type="number"
            className="form-control"
            id="experience"
            value={form.experience}
            onChange={(e) => updateForm({ experience: e.target.value })}
          />
        </div>
        <div className="form-group">
          <label htmlFor="resume">5. Please upload your resume using our secure template.</label>
          <input
            type="file"
            className="form-control-file"
            id="resume"
            onChange={(e) => updateForm({ resume: e.target.files[0] })}
            style={{marginBottom: '10px'}}
          />
        </div>
        <div className="form-group">
          <button type="submit" className="btn btn-primary">Submit</button>
          
        </div>
      </form>
    </div>
  </div>
</div>

  );
}


