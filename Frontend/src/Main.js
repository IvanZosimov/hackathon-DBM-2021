import React from "react";
import "./App.css";
import ImageContainer from "./ImageContainer";

class Main extends React.Component {

  
  render() {

    return (
      <div className = 'Main'>
          <ImageContainer
              images = {this.props.images}
              buttonState = {this.props.buttonState}
              />
      </div>
    );

        
  }
}

export default Main;
