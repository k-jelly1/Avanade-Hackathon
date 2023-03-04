import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import logo from './logo.png';

const Record = (props) => (
 <tr>
   <td>{props.record.title}</td>
   <td>{props.record.short_description}</td>
   <td>{props.record.description}</td>
   <td>{props.record.preferred_experience}</td>
   <td>
     <Link className="btn btn-link" to={`/view/${props.record.id}`}>View</Link>
   </td>
 </tr>
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
      console.log("resordsssss"); // add this line to log the records array
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
      <table className="table table-striped" style={{ marginTop: 20 }}>
      <thead>
  <tr>
    <th>Title</th>
    <th>Short Description</th>
    <th>Description</th>
    <th>Preferred Experience</th>
    <th></th>
  </tr>
</thead>

        <tbody>{recordList()}</tbody>
      </table>
    </div>
  );
}
