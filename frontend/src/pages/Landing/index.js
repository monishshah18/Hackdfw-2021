import React, { useState, useEffect } from "react";
import { makeStyles } from "@material-ui/core/styles";
import { useHistory } from "react-router-dom";
import {
  AppBar,
  Box,
  Toolbar,
  Typography,
  Button,
  IconButton,
} from "@material-ui/core";
import water from "../../assets/water.png";

const useStyles = makeStyles((theme) => ({}));

export default function Landing() {
  const classes = useStyles();
  let history = useHistory();

  return (
    <Box sx={{ flexGrow: 1 }}>
      
      <img src={water} alt="water"/>

      <div style={{ textAlign: "center", marginTop: "10%", marginBottom: "100px" }}>
        <div style={{ marginBottom: "5%" }}>
          <Button
            variant="contained"
            color="primary"
            onClick={() => {
              history.push(`/user`);
            }}
          >
            Consumers
          </Button>
        </div>
        <div>
          <Button
            variant="outlined"
            color="primary"
            onClick={() => {
              history.push(`/admin`);
            }}
          >
            Central Authority
          </Button>
        </div>
      </div>
    </Box>
  );
}
