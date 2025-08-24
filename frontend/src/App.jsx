import React, { useState } from 'react';
import './App.css';
import LanguageSelector from './components/LanguageSelector';
import CodeInput from './components/CodeInput';
import ExplanationOutput from './components/ExplanationOutput';
import { getExplanation } from './api';

export default function App() {
  const [language, setLanguage] = useState('python');
  const [code, setCode] = useState('');
  const [explanation, setExplanation] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleExplain = async () => {
    if (!code.trim()) {
      setError('Please enter some code.');
      return;
    }
    setError('');
    setLoading(true);
    try {
      const result = await getExplanation(code, language);
      setExplanation(result.explanation);
    } catch (err) {
      setError(err.message);
    }
    setLoading(false);
  };

  return (
    <div className="app-container">
      <h1>Code-to-Text Teaching Assistant</h1>
      <LanguageSelector language={language} setLanguage={setLanguage} />
      <CodeInput code={code} setCode={setCode} />
      <button onClick={handleExplain} disabled={loading}>
        {loading ? 'Explaining...' : 'Get Explanation'}
      </button>
      {error && <p className="error">{error}</p>}
      <ExplanationOutput explanation={explanation} />
    </div>
  );
}
