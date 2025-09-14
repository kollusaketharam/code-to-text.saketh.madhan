import React from 'react';

export default function ExplanationOutput({ explanation }) {
  if (!explanation) return null;

  return (
    <div className="explanation-output">
      <h3>Explanation</h3>
      {Array.isArray(explanation) ? (
        <ul>
          {explanation.map((line, idx) => (
            <li key={idx}>{line}</li>
          ))}
        </ul>
      ) : (
        <p>{explanation}</p>
      )}
    </div>
  );
}
