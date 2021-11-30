import React from "react";
import "./App.css";

class Image extends React.Component {

  render() {
    
    return (
      <div className = "Image">
        <img src = {this.props.url} />
      </div>
      
     );
  }
}

export default Image;
