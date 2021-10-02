import React, { useEffect, useState, Suspense } from "react";
import {
  BrowserRouter as Router,
  Route,
  Link,
  Redirect,
  Switch,
} from "react-router-dom";
import { useHistory } from "react-router-dom";
import {
  AppBar,
  Box,
  Toolbar,
  Typography,
  Button,
  IconButton,
} from "@material-ui/core";
// import { MuiThemeProvider, createMuiTheme, responsiveFontSizes } from '@material-ui/core/styles';
import CssBaseline from "@material-ui/core/CssBaseline";
import Landing from "./pages/Landing/index";
import Admin from "./pages/Admin/index";
import User from "./pages/User/index";
// import NotFoundPage from './pages/NotFoundPage/index'
import "./App.css";

function App() {
  return (
    <div>
      <AppBar position="static">
        <Toolbar>
          <IconButton
            size="large"
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
          >
            {/* <MenuIcon /> */}
          </IconButton>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Water Trading
          </Typography>
          {/* <Button color="inherit">Login</Button> */}
        </Toolbar>
      </AppBar>
      <Router>
        <Route path={`/admin`} exact component={Admin} />
        <Route path={`/user`} exact component={User} />
        <Route path={`/`} exact component={Landing} />
        {/* <Route path='*' exact component={NotFoundPage} /> */}
      </Router>
    </div>
  );
}

export default App;
