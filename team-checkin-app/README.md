# A *simple* team attendence/checkin application

- This repository consists the python code that is used to build. 
- It is developed with streamlit.
- Hosted on heroku for temp deployment

## Application description :
 - Application is used to enter and maintain the log of the team members.
 - This also produce a general stats for that week 
 - Every team member is assigned a unique passphrase (just like password) , only with that particular passphrase , the member can checkin. 
 - This makes it difficult for doing proxy

## Functionality :
 - The `record.csv` is used to maintain the entire log of team members
 - `week_log.csv` is used to maintain log of a particular week and will be recycled for every weekend.
 - `app.py` is the main functional app
 - `data.csv` contains the user details and pass phrases . (*this can be hidden or make the repo private*)
 - `Procfile`,`setup.sh` is used for the deployment
 - *all the remaining files are support files* 

## ScreenShots :
LightMode
![lightmode](https://github.com/pavan-elisetty/team-checkin-app/blob/main/images/1.jpg)
DarkMode
![DarkMode](https://github.com/pavan-elisetty/team-checkin-app/blob/main/images/2.jpg)

## Deployment :
[app](https://team-checkin-application.herokuapp.com/)

### Steps to Run the app:

1. Create a python virtual environment and activate it:
    ```
    python3 -m venv app
    source app/bin/activate
    ```
2. Install the required libraries:
    ```
    pip install -r requirements.txt
    ```
3. Run the app:
    ```
    streamlit run app.py
    ```
    *app runs on the local server*
    
4. Enter  `CTRL+C` once you are done.


[MIT License](https://github.com/pavan-elisetty/team-checkin-app/blob/main/LICENSE)
