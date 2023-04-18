import Routes from "./Routes/Routes";
import { BrowserRouter as Router } from "react-router-dom";
import "./Fonts/Quicksand.ttf"


function App() {
  return (
    <div>
      <Router>
        <Routes />
      </Router>
    </div>
  )
}

export default App
