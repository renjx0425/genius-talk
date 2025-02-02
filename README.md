# **GeniusTalk**  

**GeniusTalk** is an AI-powered project designed to revolutionize learning through interactive, conversational experiences with **Great Minds**. By leveraging **OpenAI** and **Murf APIs**, it combines advanced **natural language processing** with **high-quality voice synthesis** to create an engaging and immersive user experience.

## 🚀 **Features**  
✅ AI-driven conversational interactions  
✅ High-quality text-to-speech (TTS) capabilities  
✅ Seamless integration with OpenAI & Murf APIs  

## 🛠 **Prerequisites**  
Ensure you have the following installed before setting up **GeniusTalk**:  
- **Python** (version **3.8** or later)  
- **pip** (Python package manager)  


## ⚙️ **Setup Instructions**  

### **1️⃣ Clone the Repository**  
Run the following commands in your terminal:  

```sh
git clone https://github.com/renjx0425/genius-talk.git
cd genius-talk
```

### **2️⃣ Install Dependencies**  
Manually install the required Python libraries using:  

```sh
pip install openai flask requests
```

### **3️⃣ Configure API Keys**  
GeniusTalk requires API keys for external services. Update the following values in `app.py`:  

- **OpenAI API Key:** Replace `"YOUR_OPENAI_API_KEY"` with your actual OpenAI key:  

  ```python
  openai.api_key = "YOUR_OPENAI_API_KEY"
  ```

- **Murf API Key:** Replace `"YOUR_MURF_API_KEY"` with your actual Murf API key:  

  ```python
  MURF_API_KEY = "YOUR_MURF_API_KEY"
  ```

### **4️⃣ Run the Application**  
Start the backend server with:  

```sh
python app.py
```

### **5️⃣ Access the Application**  
Open your web browser and visit:  

👉 **http://localhost:5000**  

## 📁 **Project Structure**  

```
GeniusTalk/
│── src/               # Source files and assets
│── .DS_Store          # System-generated file (can be ignored)
│── GeniusTalk.pdf     # Project slides and documentation
│── README.md          # Project documentation
│── app.py             # Core backend logic
│── dataset.ipynb      # Data processing and experiments
│── index.html         # Main frontend interface
│── main.html          # Additional frontend structure
│── script.js          # Client-side JavaScript for dynamic functionality
│── style.css          # Frontend styles
```

## ❗ **Troubleshooting**  

🔹 Ensure your API keys are correctly configured.  
🔹 Verify that all required libraries are installed using `pip list`.  
🔹 If the application fails to start, check for **port conflicts** or **missing dependencies**.  


## 🤝 **Contribution Guidelines**  

We welcome contributions to improve **GeniusTalk**! Follow these steps:  

1. **Fork** the repository  
2. Create a **new branch** for your changes  
3. **Commit** your modifications  
4. **Submit a pull request (PR)** for review  

For questions or assistance, please contact:  
📧 **Ruby Ren** – [rubyren@alumni.upenn.edu](mailto:rubyren@alumni.upenn.edu)  
📧 **Yue Zhao** – [yz2000@upenn.edu](mailto:yz2000@upenn.edu)  


💡 **GeniusTalk** is designed to push the boundaries of AI-powered communication. We look forward to your contributions and feedback! 🚀✨  
