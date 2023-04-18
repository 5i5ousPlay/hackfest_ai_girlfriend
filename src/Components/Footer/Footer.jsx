import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea, CardActions,TextField } from '@mui/material';
import React from "react";
import Grid from '@mui/material/Grid';

import { useState, useContext, useEffect, useStyles} from "react";
import "./Footer.css";
import Row from 'react-bootstrap/esm/Row';
import logo from "../../assets/Vector.png"
function Iglesia(){

  
    return(
        <Row id="Footer">
            <Row id ="KevGroup">
            <img id="logo" src={logo} />
            <h1 id="Iglesia">IGLESIA NI KEVIN</h1>
            </Row>
            <Row id = "Contact">
                <h2>Stay In Touch</h2>
                <Typography id="ContactBody" variant="subtitle1">join our newsletter to get updates on storylines, rewards, deals, and other financial advice</Typography>
            </Row>
            <Row id="textfield">
            <TextField id="outlined-basic"  variant="outlined" sx={{ input: { color: 'white' } }}/>
            </Row>
            
        </Row>

    );
    }
export default Iglesia;