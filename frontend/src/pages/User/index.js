import React, { useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import { useHistory } from "react-router-dom";
import {
  InputLabel,
  Box,
  MenuItem,
  FormControl,
  Select,
} from "@material-ui/core";

const useStyles = makeStyles((theme) => ({}));

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
    <div style={{ marginTop: "20px", marginLeft: "20px", display: "flex", justifyContent: "space-evenly" }}>
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
  );
}
