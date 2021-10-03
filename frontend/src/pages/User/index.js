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
  Button,
} from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  buyButton: {
    backgroundColor: "#428c14",
    color: "white",
    fontWeight: "bold",
    "&:hover": {
      backgroundColor: "#346b12",
      color: "white",
    },
  },
  sellButton: {
    backgroundColor: "#ce2727",
    color: "white",
    fontWeight: "bold",
    "&:hover": {
      backgroundColor: "#992020",
      color: "white",
    },
  },
}));

export default function User() {
  const classes = useStyles();
  let history = useHistory();

  const [price, setPrice] = useState(25);
  const [currGal, setCurrGal] = useState(100);
  const [state, setState] = useState("tx");
  const [pool, setPool] = useState("Dallas");

  const [buyQuant, setBuyQuant] = useState(0);
  const [sellQuant, setSellQuant] = useState(0);

  const handleChange = (event) => {
    setState(event.target.value);
  };

  const handlePool = (event) => {
    setPool(event.target.value);
  };

  function buyWater() {
    if (buyQuant <= 10000) {
      fetch(`http://17bc-35-196-47-216.ngrok.io/buy_api?buyamt=${buyQuant}`, {
        method: "GET",
        headers: {},
        // body: { } https://cors-anywhere.herokuapp.com/
      })
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          var val = Number(currGal) + Number(buyQuant);
          setCurrGal(val);
          setPrice(data.base);
        })
        .catch((err) => {
          console.log(err);
        });
    } else {
      alert("Pool limit exceeded.");
    }
  }

  function sellWater() {
    if (sellQuant <= currGal) {
      fetch(
        `http://17bc-35-196-47-216.ngrok.io/sell_api?sellamt=${sellQuant}`,
        {
          method: "GET",
          headers: {},
          // body: { } https://cors-anywhere.herokuapp.com/
        }
      )
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          var val = Number(currGal) - Number(sellQuant);
          setCurrGal(val);
          setPrice(data.base);
        })
        .catch((err) => {
          console.log(err);
        });
    } else {
      alert("Not enough gallons.")
    }
  }

  return (
    <div style={{ textAlign: "center" }}>
      <div
        style={{
          marginTop: "50px",
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
              <MenuItem value="Dallas">Dallas</MenuItem>
              <MenuItem value="San Antonio">San Antonio</MenuItem>
              <MenuItem value="Houston">Houston</MenuItem>
            </Select>
          </FormControl>
        </Box>
      </div>

      <div>
        <h1>
          {pool} water cost: ${price} per gallon
        </h1>
      </div>

      <div>
        <h1>Amount of water available currently: {currGal} gallons</h1>
      </div>

      <div
        style={{
          display: "flex",
          justifyContent: "space-evenly",
          marginTop: "50px",
        }}
      >
        <div
          style={{
            border: "solid 1px darkgrey",
            minWidth: "20%",
            padding: "20px",
            display: "grid",
          }}
        >
          <p>Buy</p>

          <TextField
            id="outlined-basic"
            label="Quantity"
            variant="outlined"
            style={{ marginBottom: "20px" }}
            value={buyQuant}
            onChange={(e) => {
              setBuyQuant(e.target.value);
            }}
          />
          <Button
            onClick={buyWater}
            className={classes.buyButton}
            variant="contained"
          >
            Buy
          </Button>
        </div>
        <div
          style={{
            border: "solid 1px darkgrey",
            minWidth: "20%",
            padding: "20px",
            display: "grid",
          }}
        >
          <p>Sell</p>

          <TextField
            id="outlined-basic"
            label="Quantity"
            variant="outlined"
            style={{ marginBottom: "20px" }}
            value={sellQuant}
            onChange={(e) => {
              setSellQuant(e.target.value);
            }}
          />
          <Button
            onClick={sellWater}
            className={classes.sellButton}
            variant="contained"
          >
            Sell
          </Button>
        </div>
      </div>
    </div>
  );
}
