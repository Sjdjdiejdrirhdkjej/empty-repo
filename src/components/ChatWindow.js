import React from 'react';
import Message from './Message';
import '../styles/ChatWindow.css';

const ChatWindow = ({ messages }) => {
  return (
    <div className="chat-window">
      {messages.map((message, index) => (
        <Message key={index} text={message.text} sender={message.sender} />
      ))}
    </div>
  );
};

export default ChatWindow;
