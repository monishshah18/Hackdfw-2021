import React, { useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import { useHistory } from "react-router-dom";
import {
  InputLabel,
  Box,
  MenuItem,
  FormControl,
  Select,
  TextField,
  Button
} from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  buyButton: {
    backgroundColor: "#428c14",
    color: "white",
    fontWeight: "bold",
    '&:hover': {
      backgroundColor: "#346b12",
      color: "white",
    }
  },
  sellButton: {
    backgroundColor: "#ce2727",
    color: "white",
    fontWeight: "bold",
    '&:hover': {
      backgroundColor: "#992020",
      color: "white",
    }
  }
}));

export default function User() {
  const classes = useStyles();
  let history = useHistory();

  const [state, setState] = useState("");
  const [pool, setPool] = useState("");

  const handleChange = (event) => {
    setState(event.target.value);
  };

  const handlePool = (event) => {
    setState(event.target.value);
  };

  return (
    <div style={{ textAlign: "center" }}>
      <div
        style={{
          marginTop: "20px",
          display: "flex",
          justifyContent: "space-evenly",
          marginBottom: "60px",
        }}
      >
        <Box sx={{ minWidth: 120, maxWidth: 150 }}>
          <FormControl variant="outlined" fullWidth>
            <InputLabel id="demo-simple-select-label">State</InputLabel>
            <Select
              labelId="demo-simple-select-label"
              id="demo-simple-select"
              value={state}
              label="state"
              onChange={handleChange}
            >
              <MenuItem value="tx">Texas</MenuItem>
              <MenuItem value="ca">California</MenuItem>
              <MenuItem value="az">Arizona</MenuItem>
            </Select>
          </FormControl>
        </Box>

        <Box sx={{ minWidth: 120, maxWidth: 150 }}>
          <FormControl variant="outlined" fullWidth>
            <InputLabel id="demo-simple-select-label">Pool</InputLabel>
            <Select
              labelId="demo-simple-select-label"
              id="demo-simple-select"
              value={pool}
              label="pool"
              onChange={handlePool}
            >
              <MenuItem value={1}>Pool 1</MenuItem>
              <MenuItem value={2}>Pool 2</MenuItem>
              <MenuItem value={3}>Pool 3</MenuItem>
            </Select>
          </FormControl>
        </Box>
      </div>

      <div style={{ display: "flex", justifyContent: "space-evenly" }}>
        <div
          style={{
            border: "solid 1px darkgrey",
            minWidth: "20%",
            padding: "20px",
            display: "grid"
          }}
        >
          <p>Buy</p>

          <TextField id="outlined-basic" label="Quantity" variant="outlined" style={{marginBottom: "20px"}}/> 
          <Button className={classes.buyButton} variant="contained">Buy</Button>
        </div>
        <div
          style={{
            border: "solid 1px darkgrey",
            minWidth: "20%",
            padding: "20px",
            display: "grid"
          }}
        >
          <p>Sell</p>

          <TextField id="outlined-basic" label="Quantity" variant="outlined" style={{marginBottom: "20px"}}/> 
          <Button className={classes.sellButton} variant="contained">Sell</Button>
        </div>
      </div>
    </div>
  );
}
