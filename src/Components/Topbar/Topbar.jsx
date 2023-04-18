import * as React from "react";
import Button from '@mui/material/Button';
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { IconButton } from '@mui/material';
import "./Topbar.css";
import logo from "../../assets/Vector(1).png";
function Topbar() {
  const navigateHome = () => {
    // 👇️ navigate to /
    navigate('/');
  };
    return (
      <Container>
      <Row>
        <Col>
              <Row id = "topbar">
                <img id="logoblack" src={logo} />
                  <Button variant="text" id="click" style={{ color: "#00071B" }}>
                    Blog
                  </Button>
 
                  <Button variant="text" id="click" style={{ color: "#00071B" }}>
                    Market
                  </Button>
                
                  <Button variant="text" id="click" style={{ color: "#00071B" }}>
                    Forms
                  </Button>
                
                  <Button variant="text" id="click" style={{ color: "#00071B" }}>
                    Storyline
                  </Button>
                  <Button variant="text" id="click"style={{ color: "#00071B" }}>
                    Contact Us
                  </Button>
                  <Button
                    id="storyline"
                    variant="contained"
                    onClick={() => storyLine()}
                  >
                    Logout
                  </Button>
              </Row>
              <Col id ="mommywindow">
              </Col>
        </Col>
      </Row>
      </Container>
        
    );
  }
  
  export default Topbar;
  