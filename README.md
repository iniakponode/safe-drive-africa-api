# SafeDriveAfrica API Documentation

Welcome to the official readme file for the API developed as a part of the PhD research project led by Thompson Iniakpokeikiye Peter in the Department of Computing Science, School of Natural and Computing Sciences at the University of Aberdeen, Scotland, United Kingdom.

# Project Overview:
The API serves as a pivotal component of a comprehensive research endeavor supervised by Professor Ehud Reiter and Dr. Yi Dewei. This innovative project, generously sponsored by the human resources training division of the Tertiary Education Trust Fund (TetFund) in Nigeria. The research focuses on advancing safe driving behavior in Non-Western countries. 

# Project Objectives:
The PhD research project is focused on identifying the peculiarities with unsafe driving in non-western countries, Nigeria as case study. This research endeavour is basically concerned with collection of real time drivers’ behaviour data from Nigeria as well as the development of AI/NLG powered mobile applications that can automatically generate driving behaviour feedback for drivers, to encourage safer driving in Nigeria and which can be adapted in other African countries.

# Applications Developed:

## Driving Data Collection App (DDCAP):
The DDCAP is a sensor-based mobile application meticulously designed to collect real-time raw driving data, including metrics such as acceleration, speed, geolocation, and more. Moreover, it features interactive forms that enable drivers to provide feedback regarding the factors influencing their driving behavior on a trip-by-trip basis.

## Harsh Braking Factors Explanation and Feedback App (HBEFA):
The HBEFA is an application that uses AI algorithms to ascertain the impact of reported driving influences on a driver's tendency towards harsh braking. This app evaluates the intensity of contribution to the tendency of harsh braking behavior per reported influencing factor.

# API Details:

The API is developed to serve as the backend infrastructure for all applications that will be developed in the course of the research project, beginning with the HBEFA app. Its functionalities encompass experiment participant registration, report generation, and user interactions with the generated reports.

# Technical Specifications:
The API is constructed using the FastAPI framework and follows a well-structured modular design pattern. This approach ensures scalability, maintainability, and adaptability to evolving requirements.

# Continuous Updates:
The API is an evolving component of this research project. Continuous updates are planned to refine and enhance its features in alignment with the research objectives.

Thank you for your interest in our API. For further inquiries or collaboration opportunities, please contact Thompson Iniakpokeikiye Peter at i.thompson.21@abdn.ac.uk.

## Table of Contents
Features
Installation
Usage
Endpoints
Documentation
Contributing
License
Features


### User Registration:

Automatic user registration with an auto-generated token and creation timestamp.

### Report Management:

Generation and storage of qualitative and quantitative reports.
User selection of report type and comment.
Retrieval of report instances with selected report type and comments.

### User Management:

* Retrieval of user information by token.
* Retrieval of user reports.
* Deletion of users.
* Installation

### Clone the repository:

* bash
* Copy code
* git clone https://github.com/iniakponode/safe-drive-africa-api.git

### Install the dependencies:

* bash
* Copy code
* pip install -r requirements.txt

### Run the FastAPI application:

* bash
* Copy code
* uvicorn main:app --host 0.0.0.0 --port 8000
* Usage

### Register a User:

* Endpoint: /register/
* Method: POST
* Payload: User registration data
* Returns: User details including token and creation timestamp.

### Get User Information:

* Endpoint: /users/{token}/
* Method: GET
* Returns: User information based on the provided token.

### Generate Reports:

* Endpoint: /reports/
* Method: POST
* Payload: Generated report data (Qualitative or Quantitative).
* Returns: Report details.

### Get User Reports:

* Endpoint: /users/{user_id}/reports/
* Method: GET
* Returns: List of reports associated with the user.

### Get Report with User Comment:

* Endpoint: /reports/{report_id}/
* Method: GET
* Returns: Report details including user-selected report type and comment.

### Delete User:

* Endpoint: /users/{token}/
* Method: DELETE
* Returns: Message confirming the user's deletion.

#### Documentation
#### API Documentation
#### Redoc Documentation

# Contributing
Contributions to the project are welcome. Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License. See LICENSE for more information.
