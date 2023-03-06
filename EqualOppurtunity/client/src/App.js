import React from "react";
import { Route, Routes} from "react-router-dom";
import Navbar from "./components/navbar";
import RecordList from "./components/recordList";
import View from "./components/view";
import Create from "./components/create";
import Main from "./components/main";
import Employer from "./components/employer";

const App = () => {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/create" element={<Create />} />
        <Route path="/view/:id" element={<View />} />
        <Route path="/record" element={<RecordList />} />
        <Route path="/employer" element={<Employer />} />
        <Route path="/" element={<Main />} />
      </Routes>
     
    </div>
  );
};

export default App;
