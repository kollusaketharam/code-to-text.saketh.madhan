import React from 'react';

export default function CodeInput({ code, setCode }) {
  return (
    <textarea
      value={code}
      onChange={(e) => setCode(e.target.value)}
      placeholder="Paste your code here..."
      className="code-input"
    />
  );
}
