import React from "react";
import "./App.css";

class ButtonBox extends React.Component {

  render() {
    
    return (
      <div className = 'ButtonBox'>
        <button className = "GoodBoys" onClick = {this.props.onClickGood}> In Mask </button>
        <button className = "BadBoys" onClick = {this.props.onClickBad} > Without Mask </button>
        <button className = "Soso" onClick = {this.props.onClickSoso} > Incorrect </button>
        <button className = "All" onClick = {this.props.onClickAll}> All </button>
      </div>
    );
  }
}

export default ButtonBox;
