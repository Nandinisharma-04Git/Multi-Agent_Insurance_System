## Multi-Agent Insurance System

A small demo web application that simulates multiple AI agents collaborating to recommend insurance policies.

### Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, vanilla JavaScript
- **Data store**: `policies.json`

### Features

- **Landing page** explaining the multi-agent concept.
- **User input form** for age, income, family members, insurance type, coverage amount, and risk preference.
- **Agents (simulated)**:
  - **Input Agent**: validates input.
  - **Recommendation Agent**: scores and picks the top 3 matching policies.
  - **Comparison Agent**: renders a comparison table.
  - **Query Agent**: answers questions with rule-based responses.
- **Chat assistant** with predefined, rule-based answers.

### Project Structure

```text
project/
  app.py
  policies.json
  requirements.txt
  templates/
      index.html
      form.html
      result.html
  static/
      style.css
      script.js
```

### How to Run Locally

1. **Open a terminal in the project folder**  
   `c:\Users\lenovo\OneDrive\文档\Dewvops WEB`

2. **Create and activate a virtual environment (recommended)**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**

   ```bash
   python app.py
   ```

5. **Open the app in your browser**

   Go to `http://127.0.0.1:5000` and:

   - Use the **"Find Best Insurance Policy"** button on the landing page.
   - Fill in the form and submit to see:
     - Top 3 recommended policies as cards.
     - A comparison table with premium, coverage, and key benefits.
   - Use the **chat** box to ask questions such as:
     - "Does this policy cover hospitalization?"
     - "Is accident coverage included?"

