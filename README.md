# 🎵 Popatoms
looking for the future by looking at the past

### 👥 The Team
Gabriela: https://www.linkedin.com/in/gabriela-casero-59233a131/
Almudena: https://www.linkedin.com/in/almudenamcastro/

### Business Opportunity: 
Every year the music market changes and new trends appear that change how we listen to music. 
This project aims to analyze the major musical hits of the past 50 years to understand the influence of various factors on the popularity of songs, as well as their evolution. Using data extracted from the Spotify API and the Billboard API, we explore features such as energy, tempo, duration, and other attributes to understand their relationship with chart success.

### 💡 Initial Hypothesis: 
We believe that: 

- Music tracks have decreased their duration 
(probably due to the influence of TikTok and similar apps)
- Music has become more calm (tempo is slower).
- Nonetheless, music loudness hasn’t probably decreased
- Minor keys have become more frequent during the last years.
- The most common metric is 4/4 (by far).
- Music has become more repetitive during the last few years.
- There are more vindictive topics, specially related with feminism.

Presentation with more info: https://www.canva.com/design/DAGQjz4IelY/GuO8nIyDawsMBsXLvI5mQA/view?utm_content=DAGQjz4IelY&utm_campaign=designshare&utm_medium=link&utm_source=editor

## Project content
### 📁 Files Structure
The project is organized into the following key files and folders:

- `df....csv`: Saved data frames.  
- `main.py`: The main project file that runs the overall analysis, data collection, preprocessing, and analysis.
- `functions.py`: Contains helper functions to interact with the APIs, process data, and manipulate the results.
- `requirements.txt`: A list of dependencies required to run the project.
- `README.md`: This file describes the purpose of the project and how to run it.

### 📊 Data Sources

- **Spotify API**: From this API, we obtained data related to song features, such as tempo, energy, duration, mode, and others.
- **Billboard API**: From this API, we extracted the historical rankings of the most popular songs, enabling a temporal analysis.
  
The analysis focused on understanding how these attributes and features change over time and their impact on popularity.

### 🛠️ Tools Used

- **Language**: Python
- **APIs**: Spotify, Billboard
- **Libraries**:
  - `requests`: For interacting with APIs
  - `pandas`: For data manipulation
  - `matplotlib` / `seaborn`: For data visualization
  - `dotenv`: To manage API credentials
  - `jupyter`: For exploratory analysis


## 📈 Results and Conclusions

- Music popularity increased dramatically after 1960. 
- Music accousticness has decreased over the years. 
- Music loudness has increased significantly. 

## How to run the Code

### 🔧 Installation and Setup

Clone this repository:

```bash
git clone https://github.com/your-user/your-project.git
cd your-project
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```
Set up your Spotify and Billboard API keys. You need to create a .env file in the project root and add your credentials:

```bash
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
BILLBOARD_API_KEY=your_billboard_api_key
```

### 🚀 Running the Project

Run the main file: To begin the analysis and data extraction, execute the `main.py` file:

```bash
python main.py
```

Exploratory Data Analysis (EDA): If you want to visualize graphs and explore the data, open the `eda.ipynb` notebook with Jupyter:

```bash
jupyter notebook eda.ipynb
```

### 📝 Contributions

If you want to contribute to this project, feel free to send a pull request or report issues. All feedback and suggestions are welcome.

## Other sources: 
- https://www.latimes.com/entertainment/tv/showtracker/la-et-st-beatles-ed-sullivan-50-years-20140202-story.html

