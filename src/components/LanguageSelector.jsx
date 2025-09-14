import React from 'react';

export default function LanguageSelector({ language, setLanguage }) {
  return (
    <select
      value={language}
      onChange={(e) => setLanguage(e.target.value)}
      className="language-selector"
    >
      <option value="python">Python</option>
      <option value="javascript">JavaScript</option>
      <option value="java">Java</option>
    </select>
  );
}
