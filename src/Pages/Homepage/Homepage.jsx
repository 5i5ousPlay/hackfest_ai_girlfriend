import * as React from "react";
import Button from '@mui/material/Button';
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import "./Homepage.css";
import AI from "../../assets/AI.png"
import Chat from "../../assets/Fin MOMMYSemiTrans.png"
import Topbar from "../../Components/Topbar/Topbar";
import Carousell from "../../Components/Cards/Card.jsx";
import Iglesia from "../../Components/Footer/Footer.jsx";
function Homepage() {
      document.body.classList.add("overflow-hidden");

    return (
      <div id ="main">
        <Topbar />
      <Container fluid>
      <Row id ="mommywindow">
        <Col id="actualmommy">
          <img id="AI" src={AI} />
        </Col>
        <Col id=" chatsystem">
          <img id="Chatimg" src={Chat} />
        
        </Col>
      </Row>
      <Row id ="Storyline">
      <h2>STORYLINE</h2>
      <Carousell />
      </Row>
      </Container>
      <Iglesia/>
      
      </div>
        
    );
  }
  
  export default Homepage;
  