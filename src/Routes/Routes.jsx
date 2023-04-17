import Homepage from "../Pages/Homepage/Homepage";
import { Route, Routes } from "react-router-dom";
import React from "react";

function Index(){
    return(
        <div className="App">

                <Routes>
                <Route>
                    <Route path="/" element={<Homepage />} />

                </Route>
                </Routes>
        </div>
    )
}
export default Index