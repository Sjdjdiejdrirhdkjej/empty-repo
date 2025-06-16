import React, { useState } from 'react';
import ChatWindow from './components/ChatWindow';
import MessageInput from './components/MessageInput';
import './styles/App.css';

function App() {
  const [messages, setMessages] = useState([]);

  const handleSendMessage = (message) => {
    // Add user message to the state
    setMessages(prevMessages => [...prevMessages, { text: message, sender: 'user' }]);

    // Simulate AI response
    setTimeout(() => {
      const aiResponse = `AI response to: "${message}"`;
      setMessages(prevMessages => [...prevMessages, { text: aiResponse, sender: 'ai' }]);
    }, 1000);
  };

  return (
    <div className="app">
      <h1>AI Chat App</h1>
      <ChatWindow messages={messages} />
      <MessageInput onSendMessage={handleSendMessage} />
    </div>
  );
}

export default App;
