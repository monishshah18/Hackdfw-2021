import React, { useState } from 'react';
import { makeStyles } from "@material-ui/core/styles";
import { useHistory } from 'react-router-dom'

const useStyles = makeStyles((theme) => ({
  
}))

export default function User() {
  const classes = useStyles();
  let history = useHistory();

  return (
    <h1>Hey user!</h1>
  )
}
