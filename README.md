# Educational Chatbot
An AI-powered chatbot designed to assist users in exploring educational courses, providing personalized recommendations, and answering queries related to various learning topics.​

## 📚 About the Project
The Educational Chatbot is an intelligent assistant designed to guide learners through a vast database of online courses, helping them discover content tailored to their interests and needs. The goal is to simplify course discovery and make learning more accessible and personalized.

## 🔍 Problem It Solves
With the growing number of online courses available on platforms like Udemy, it becomes challenging for learners to find the right course quickly. This chatbot addresses that by:

- Understanding user queries in natural language.
- Filtering and recommending relevant courses.
- Providing a chat-based interface that's more intuitive than traditional search.

## 🧠 How It Works
- User Interaction: A user types a question or interest area into the chatbot (e.g., "I want to learn web development").
- Text Processing: The input is processed using NLP techniques to understand user intent.
- Data Matching: The bot scans a dataset of Udemy courses (udemy_course_data.csv) to find the most relevant matches.
- Response Generation: A friendly response is generated, listing course names, ratings, or prices based on the query.
- Interface: Built with Streamlit, the chatbot is accessible via a clean, browser-based UI. Backend support is provided via FastAPI.

## 🏗️ Technologies Used
- Python –> Core programming language.
- Streamlit –> Frontend interface for the chatbot.
- FastAPI –> For building scalable API services.
- Pandas –> Data handling and manipulation.
- Scikit-learn / NLP Libraries –> For natural language understanding and text matching.

## Features
- Course Recommendations: Suggests courses based on user interests and queries.
- Interactive Chat Interface: Engages users in a conversational manner to provide information.
- Data-Driven Insights: Utilizes course data to offer informed suggestions.
- Modular Architecture: Structured codebase for easy maintenance and scalability.


## Installation
1- Clone the Repository:

<pre>git clone https://github.com/Spark1ST/Educational_Chatbot.git
cd Educational_Chatbot </pre>

2- Create a Virtual Environment:

<pre>python -m venv venv
source venv/bin/activate </pre>

  
3- Install Dependencies:
<pre> pip install -r requirements.txt </pre>

## Usage
1- Prepare the Data:

Ensure the udemy_course_data.csv file is present in the root directory. This file contains the course data used by the chatbot.​

2- Run the Application:

<pre>python app.py</pre>
3- Access the Chatbot:

Open your web browser and navigate to (https://educationalchatbot-dvpthkchgkg75ibd5ajapx.streamlit.app/) to interact with the chatbot interface.

# Live DEMO
Try out the chatbot in action here:  
👉 [Educational Chatbot Demo](https://drive.google.com/file/d/1BlsZy7jFnmtCU1sZ8s58pJnWZ81xe_5m/view)
