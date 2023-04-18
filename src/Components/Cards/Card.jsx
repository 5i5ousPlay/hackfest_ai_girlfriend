import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea, CardActions } from '@mui/material';
import React from "react";
import Grid from '@mui/material/Grid';

import { useState, useContext, useEffect, useStyles} from "react";
import "./Card.css";

function Carousell(){

  const navigateStoryline = () => {
    // 👇️ navigate to /
    navigate('/');
  };
    return(
      <div >
<Grid container rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>
  <Grid item xs={3}>
  <Card sx={{ maxWidth: 345 }}>
      <CardActionArea>

        <CardMedia
          component="img"
          height="140"
          image=".\src\assets\Card1.png"
          alt=""
        />
<CardContent>
          <Typography gutterBottom variant="h5" component="div">
            Spring Festival
          </Typography>
          <Typography variant="body2" color="text.secondary">
            length: 35 Minutes
          </Typography>
        </CardContent>
      </CardActionArea>
      <CardActions>
      </CardActions>
    </Card>
  </Grid>
  <Grid item xs={3}>
  <Card sx={{ maxWidth: 345 }}>
      <CardActionArea>
        <CardMedia
          component="img"
          height="140"
          image=".\src\assets\gym.jpg"
          alt=""
        />
       <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            Workout Session
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Length:25 Minutes
          </Typography>
          </CardContent>
      </CardActionArea>
      <CardActions>

      </CardActions>
    </Card>
  </Grid>
  <Grid item xs={3}>
  <Card sx={{ maxWidth: 345 }}>
      <CardActionArea>
        <CardMedia
          component="img"
          height="140"
          image=".\src\assets\garden.jpg"
          alt=""
        />
<CardContent>
          <Typography gutterBottom variant="h5" component="div">
            Secret Garden
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Length: 30 Minutes
          </Typography>
       
        </CardContent>
      </CardActionArea>
      <CardActions>

      </CardActions>
    </Card>
  </Grid>
  <Grid item xs={3}>
  <Card sx={{ maxWidth: 345 }}>
      <CardActionArea>
        <CardMedia
          component="img"
          height="140"
          image=".\src\assets\dream.jpg"
          alt=""
        />
<CardContent>
          <Typography gutterBottom variant="h5" component="div">
            Lost Dreams
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Length: 15 Minutes
          </Typography>
        
        </CardContent>
      </CardActionArea>
      <CardActions>

      </CardActions>
    </Card>
  </Grid>
</Grid>
    
</div>
   );
}

export default Carousell;