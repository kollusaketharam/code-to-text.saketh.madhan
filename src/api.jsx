import axios from 'axios';

const API_BASE = 'http://127.0.0.1:8000'; // Backend FastAPI URL

export const getExplanation = async (code, language) => {
  try {
    const response = await axios.post(`${API_BASE}/explain`, {
      code,
      language
    });
    return response.data;
  } catch (error) {
    console.error(error);
    throw new Error(error.response?.data?.detail || 'Error connecting to API');
  }
};
