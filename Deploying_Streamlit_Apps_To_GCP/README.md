### Requirements For Deployment
+ Dockerfile
+ app.yaml : configuration
+ Gcloud sdk


#### Commands
#### List Projects
```bash
gcloud projects list
```

#### To change to the project you created you can use
```bash
gcloud config set project your_projectname
```
#### To check for the current project you use
```bash
gcloud config get-value project
```

#### To deploy our app we will be using
```bash
gcloud app deploy
```


#### By
+ Jesse E.Agbe(JCharis)
+ Jesus Saves @JCharisTech