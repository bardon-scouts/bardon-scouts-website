import * as React from "react";
import { Link } from "gatsby";

import logo from "../img/scouts_logo.jpg";
import facebook from "../img/social/facebook.svg";
import instagram from "../img/social/instagram.svg";
import twitter from "../img/social/twitter.svg";
import vimeo from "../img/social/vimeo.svg";

const Footer = class extends React.Component {
  render() {
    return (
      <footer className="footer has-background-black has-text-white-ter">

        <ul>
            <li><a href="/#join">Why Join Scouts?</a></li>
            <li><a href="/#adventure">Get ready for adventure</a></li>
            <li><a href="/#units">Our units</a></li>
            <li><a href="/contact">Contact us</a></li>
        </ul>
          {/*
            <img className="logo"
              src={logo}
              alt="Scouts Australia"
            />
            */}
      </footer>
    );
  }
};

export default Footer;
