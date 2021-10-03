import React, { useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import { useHistory } from "react-router-dom";
import GoogleMapReact from "google-map-react";
import Marker from "./Marker.tsx";

const useStyles = makeStyles((theme) => ({}));

// const AnyReactComponent = ({ text }) => <div>{text}</div>;

export default function Admin() {
  const classes = useStyles();
  let history = useHistory();

  const [center, setCenter] = useState({ lat: 32.7939054, lng: -96.8728261 });
  const [zoom, setZoom] = useState(5);

  // var data = {
  //   center: {
  //     lat: 59.95,
  //     lng: 30.33,
  //   },
  //   zoom: 11,
  // };

  return (
    <div
      style={{
        height: "50vh",
        width: "50%",
        marginLeft: "auto",
        marginRight: "auto",
        marginTop: "10%",
      }}
    >
      <GoogleMapReact
        bootstrapURLKeys={{ key: "" }}
        defaultCenter={center}
        defaultZoom={zoom}
      >
        <Marker
          lat={32.7939054}
          lng={-96.8728261}
          color="yellow"
          name="Pool 1"
        />

        <Marker lat={29.4817349} lng={-98.7945951} color="blue" name="Pool 2" />

        <Marker lat={29.8174782} lng={-95.681482} color="red" name="Pool 3" />

        {/* <Polyline 
          path={[ 
            {lat:32.7939054, lng:-96.8728261},
            {lat:29.4817349, lng:-98.7945951},
          ]} 
          options={{ 
          strokeColor: '#00ffff',
          strokeOpacity: 1,
          strokeWeight: 2,
          icons: [{ 
            icon: "hello",
            offset: '0',
            repeat: '10px'
            }],
          }}
        /> */}
      </GoogleMapReact>
    </div>
  );
}
