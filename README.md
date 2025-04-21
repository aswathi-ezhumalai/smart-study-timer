# Smart Study Timer Web App using Gaussian Mixture Model (GMM)

The **Smart Study Timer** is a web application designed to help users optimize their study sessions by providing personalized recommendations for focus and break times. This app leverages the **Gaussian Mixture Model (GMM)**, a machine learning algorithm, to analyze user inputs and suggest an effective study-break schedule.

---

## Features

- **User Input**: Users can input their focus time, break time, and the number of distractions during study sessions.
- **Machine Learning**: The backend uses the GMM algorithm to analyze the data and provide tailored suggestions.
- **Responsive Design**: The app is fully responsive and works seamlessly on all devices.
- **Modern UI**: A clean and visually appealing interface with gradient backgrounds and intuitive form design.

---

## Technologies Used

### Frontend:
- **HTML5**: For structuring the web page.
- **CSS3**: For styling and responsive design.
- **JavaScript**: For handling form submission and dynamic updates.

### Backend:
- **Python**: For server-side logic.
- **Flask**: A lightweight web framework for handling HTTP requests and responses.
- **Machine Learning**: Gaussian Mixture Model (GMM) for clustering and prediction.

---

## How It Works

1. **User Input**: The user provides the following inputs:
   - Focus Time (in minutes)
   - Break Time (in minutes)
   - Number of Distractions

2. **Data Processing**: The inputs are sent to the backend via a POST request.

3. **GMM Algorithm**:
   - The GMM algorithm clusters the data and identifies patterns.
   - Based on the analysis, it provides a suggestion for an optimal study-break schedule.

4. **Output**: The suggestion is displayed on the screen for the user.

---

## Installation and Setup

### Prerequisites:
- Python 3.x
- Flask
- Basic knowledge of running Python scripts

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/aswathi-ezhumalai/smart-study-timer.git
   cd smart-study-timer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask server:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

### File Structure

The project directory is organized as follows:

```
smart-study-timer/
│
├── backend/
│   ├── app.py
│   ├── gmm_model.pkl
│   ├── requirements.txt
│   └── study_utils.py
├── backend/
│   ├── index.html
│   └── style.css
├── .render.yaml
├── .gitignore
├── README.md

```

## Gaussian Mixture Model (GMM)
**The Gaussian Mixture Model (GMM)** is a probabilistic model that assumes all data points are generated from a mixture of several Gaussian distributions with unknown parameters. It is used in this project to cluster user inputs and provide personalized study-break recommendations.

## Future Enhancements
- Add user authentication for saving preferences.
- Integrate a database to store historical data.
- Provide visualizations for user performance over time.
- Add support for multiple languages.
# License
This project is licensed under the MIT License. See the LICENSE file for details.