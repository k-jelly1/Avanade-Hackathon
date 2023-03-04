import React from "react";
 
// We use Route in order to define the different routes of our application
import { Route, Routes } from "react-router-dom";
 
// We import all the components we need in our app
import Navbar from "./components/navbar";
import RecordList from "./components/recordList";
import View from "./components/view";
import Create from "./components/create";
 
const App = () => {
  return (
   <div>

  <Routes>
  <Route path="/create" element={<Create />} />
  <Route path="/view/:id" element={<View />} />
  <Route exact path="/" element={<RecordList />} />
     </Routes>

   </div>

 );
};
 
export default App;