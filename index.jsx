import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

function Home() {
  return (
    <div>
      <h1>What ya building?</h1>
      <p>Prompt, run, edit, and deploy full-stack web and mobile apps.</p>
      {/* Rest of the content */}
    </div>
  );
}

export default Home;
