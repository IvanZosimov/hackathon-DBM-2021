import React from "react";
import "./App.css";
import Image from "./Image";

class ImageContainer extends React.Component {

  displayImages = () => {

    if (this.props.buttonState === 2){

    return this.props.images.map(image => {

      return (
      <div className = "ImageContainer">
        <Image url = {image.url} />
        <div classname = "Container">
          <p className = "RecDate"> Время съемки: {image.date} </p>
          <p className = "Accuracy"> Точность определения: {image.accuracy} </p>
        </div>
      </div>
      );

    });
  }

  if (this.props.buttonState === 1){

    return this.props.images.map(image => { 

      if (image.inMask === 1){

        return (
          <div className = "ImageContainer">
            <Image url = {image.url} />
            <div>
              <p className = "RecDate"> Время съемки: {image.date} </p>
              <p className = "Accuracy"> Точность определения: {image.accuracy} </p>
            </div>
          </div>
          );
      }
    
    });
  }

  if (this.props.buttonState === 0){

    return this.props.images.map(image => { 

      if (image.inMask === 0){

        return (
          <div className = "ImageContainer">
            <Image url = {image.url} />
            <div>
              <p className = "RecDate"> Время съемки: {image.date} </p>
              <p className = "Accuracy"> Точность определения: {image.accuracy} </p>
            </div>
          </div>
          );
      }
    
    });
  }

  if (this.props.buttonState === 3){

    return this.props.images.map(image => { 

      if (image.inMask === 2){

        return (
          <div className = "ImageContainer">
            <Image url = {image.url} />
            <div>
              <p className = "RecDate"> Время съемки: {image.date} </p>
              <p className = "Accuracy"> Точность определения: {image.accuracy} </p>
            </div>
          </div>
          );
      }
    
    });
  }
  
    
  }

  
  render() {
    
    return (
    <div className = "ImagePlace">
      {this.displayImages()}
    </div>  
          
    );
  }
}

export default ImageContainer;
