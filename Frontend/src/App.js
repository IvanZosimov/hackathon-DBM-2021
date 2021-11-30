import React from "react";
import "./App.css";
import Header from './Header';
import ButtonBox from './ButtonBox';
import Main from './Main';
import Footer from './Footer';




const connection_string = "http://127.0.0.1:5000/";



class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      images: [],
      buttonState: 2,
       
    };
  }

  getInfo = () => {

    fetch(connection_string).then((response) => {

      return response.json();

    }).then((data) => {this.setState({images : data})});

  }

  onClickAll = () => {

    this.getInfo();
    this.setState({buttonState : 2});
    

  }

  onClickBad = () => {

    this.getInfo();
    this.setState({buttonState : 0});

  }

  onClickGood = () => {

    this.getInfo();
    this.setState({buttonState : 1});

  }

  onClickSoso = () => {

    this.getInfo();
    this.setState({buttonState : 3});

  }
  
  renderMain = () => {
    return (
      <Main
        images = {this.state.images}
        buttonState = {this.state.buttonState}
        
      /> 
    );
  }

   renderButtonBox = () => {
    return (
      <ButtonBox
        onClickAll = {() => this.onClickAll()}
        onClickGood = {() => this.onClickGood()}
        onClickBad = {() => this.onClickBad()}
        onClickSoso = {() => this.onClickSoso()}
        
      /> 
    );
  }

  
  componentDidMount() {

    this.getInfo();

  } 

  render() {
    
    return (
      <div>
         <Header/>
         {this.renderButtonBox()} 
         {this.renderMain()}
         <Footer/> 
         
      </div>
    );
  }
}

export default App;
