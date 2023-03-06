import React from "react";
import {Link } from "react-router-dom";
import "./main.css";

export default function main() {

    return (
<div className="button-container1">
<Link to="/record">
  <button className="button1">Job seeker</button>
</Link>
<Link to="/Employer">
  <button className="button1">Employer</button>
</Link>
</div>
    )
};