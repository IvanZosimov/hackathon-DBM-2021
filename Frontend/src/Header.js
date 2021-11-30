import React from "react";
import "./App.css";

const date = new Date().toLocaleDateString();


class Header extends React.Component {

  render() {
    
    return (
      <div className = 'Header'> 
        <p className = 'Date'>{date}</p>
        <p className = 'Hp'>Don't break a mask!</p>
        
      </div>
    );
  }
}

export default Header;
