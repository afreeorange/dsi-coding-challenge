import React, { Component } from 'react';
import ReactDOM from 'react-dom';
//import './index.css';
//import App from './App';
//import registerServiceWorker from './registerServiceWorker';

/*ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();*/

class App extends Component {
  constructor() {
    super()
  }
  render() {
    return (
      <h1>BOO!</h1>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
