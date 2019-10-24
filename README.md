##  Streamlit_DataScience_Apps
Streamlit Data Science and ML Apps in Python


### How to Deploy Streamlit Apps to Heroku

#### 1. Create An Account Heroku by signing up.
#### 2. Install Heroku CLI
#### 3. Create Your Github Repository for your app
#### 4. Build your app
#### 5. Login to Heroku From the CLI
```sh 
heroku Login
```
#### 6. Create Your 3 Required Files(setup.sh,Procfile,requirements.txt)
+ Place the code below in their respective files



##### Code for setup.sh
```sh
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

##### Code for setup.sh (Alternate with no credentials.toml)
```sh
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

##### Code For Procfile
```sh
web: sh setup.sh && streamlit run your_app.py
```

#### 7. Create App with CLI
```sh
heroku create name-of-your-app
```

#### 8. Commit and Push Your Code to Github
```sh
git add your app 
git commit -m "your comment description"
git push
```
#### 9. Push To Heroku to Deploy
```sh
git push heroku master
```


#### Credits:
[gabe_maldonado](https://discuss.streamlit.io/u/gabe_maldonado)

[Streamlit team](https://streamlit.io/)

#### Thanks For Your Time

####By 
+ Jesse E.Agbe(JCharis)
+ Jesus Saves@JCharisTech