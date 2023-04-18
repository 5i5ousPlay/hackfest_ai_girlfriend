import Homepage from "../Pages/Homepage/Homepage";
import Storyline from "../Pages/Storyline/Storyline";
import { Route, Routes } from "react-router-dom";
import React from "react";

function Index(){
    return(
        <div className="App">

                <Routes>
                <Route>
                    <Route path="/" element={<Homepage />} />
                    <Route path="/storyline" element={<Storyline />} />

                </Route>
                </Routes>
        </div>
    )
}
export default Index