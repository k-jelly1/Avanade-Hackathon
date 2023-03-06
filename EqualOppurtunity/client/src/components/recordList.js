import React, { useEffect, useState } from "react";

const Record = (props) => (
  <tr>
    <td>{props.record.title}</td>
    <td><a href={`/view/${props.record.id}`}>View</a></td>
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
      <h3>Job Postings</h3>
      <table className="table">
        <thead>
          <tr>
            <th>Title</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {recordList()}
        </tbody>
      </table>
    </div>
  );
}
