import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import logo from './logo.png';

const Record = (props) => (
  <div className="col-md-4 mb-4">
    <div className="card h-100">
      <img className="card-img-top" src={props.record.image} alt={props.record.title} />
      <div className="card-body">
        <h5 className="card-title" style={{ fontSize: "1.2rem" }}>{props.record.title}</h5>
        <p className="card-text">{props.record.description}</p>
        <Link className="btn btn-primary" to={`/view/${props.record.id}`}>View</Link>
      </div>
    </div>
  </div>
);

export default function RecordList() {
  const [records, setRecords] = useState([]);

  useEffect(() => {
    async function getRecords() {
      const response = await fetch("http://127.0.0.1:8000/api/jobs/");
      if (!response.ok) {
        const message = `An error occurred: ${response.statusText}`;
        window.alert(message);
        return;
      }
      const records = await response.json();
      setRecords(records["Job Postings"]);
    }
    getRecords();
  }, []);

  function recordList() {
    return records.map((record) => {
      return (
        <Record
          record={record}
          key={record.id}
        />
      );
    });
  }

  return (
    <div className="App">
      <img style={{ "width": 15 + '%' }} alt="logo" src={logo}></img>
      <header className="App-header">
        <h3 className="Title">
          Job Postings
        </h3>
      </header>
      <div className="row row-cols-1 row-cols-md-3 g-4">
        {recordList()}
      </div>
    </div>
  );
}
