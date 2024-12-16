# GeniusTalk

GeniusTalk is an AI-powered project designed to revolutionize content delivery through interactive, conversational experiences. By leveraging OpenAI and Murf APIs, it enables advanced natural language processing and high-quality voice synthesis to enhance user engagement.

## Features
- AI-driven conversational interactions.
- High-quality text-to-speech capabilities.

## Prerequisites
1. **Python** (version 3.8 or above).

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/GeniusTalk.git
cd GeniusTalk
```

### 2. Install Dependencies
Install the following Python libraries manually:
- `openai`
- `flask`
- `requests`

Use the following command:
```bash
pip install openai flask requests
```

### 3. Configure API Keys
GeniusTalk requires API keys for external services. Update the following files:

- **OpenAI API Key:**
  Open `app.py` and replace the placeholder with your OpenAI API key:
  ```python
  openai.api_key = "YOUR_OPENAI_API_KEY"
  ```

- **Murf API Key:**
  Open `app.py` and update the Murf API key:
  ```python
  MURF_API_KEY = "YOUR_MURF_API_KEY"
  ```

### 4. Run the Application
Start the backend application with:
```bash
python app.py
```

### 5. Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

## Project Structure
- **`app.py`**: Core backend logic.
- **`audio_test.py`**: Scripts for testing audio features.
- **`index.html`**: Main frontend interface.
- **`style.css`**: Frontend styles.
- **`script.js`**: Client-side JavaScript for dynamic functionality.
- **`src/`**: Additional resources and supporting code.

## Troubleshooting
- Ensure your API keys are configured correctly.
- Verify that all required libraries are installed.
- If the application fails to start, check for potential port conflicts.

## Contribution Guidelines
We welcome contributions to enhance GeniusTalk! To contribute:
1. Fork the repository.
2. Make your changes in a new branch.
3. Submit a pull request for review.

---
For questions or assistance, please reach out to Jingxuan Ren at renjx@upenn.edu and Yue Zhao at yz2000@upenn.edu.
