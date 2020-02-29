# face_detection_app
+ Streamlit App with OpenCV

### How to Deploy on Heroku
+ To deploy on heroku you will need the basic 3 requirements and a new requirement for the OpenCV
+ This is due to the fact that opencv requires some dependencies that you need to install.

### 3 Basic Requirements
+ Procfile
+ setup.sh
+ requirements.txt or pipfile

### Requirements For OpenCV
+ Buildpack
 - To check if you have the buildpack installed you can use
```bash
heroku run bash
apt --help
```
 - If it shows the help, that means you have the buildpack for apt installed
 - If you do not have it you can use this command to install the buildpack
 ```bash
 heroku buildpacks:add --index 1 https://github.com/heroku/heroku-buildpack-apt
 ```

+ Aptfile
- You can then include a file called Aptfile which contains the basic dependences/copy and paste into Aptfile
```
libsm6
libxrender1
libfontconfig1
libice6
```
+ NB: This is the same as installing with apt on a paid account
```bash
apt-get install libsm6 libxrender1 libfontconfig1 libice6
```

#### Deploying
+ Then just like before you run after adding to your repo you can push to heroku to deploy by
```bash
git push heroku master
```


#### By
+ Jesus Saves @JCharisTech
+ Jesse E.Agbe(JCharis)

