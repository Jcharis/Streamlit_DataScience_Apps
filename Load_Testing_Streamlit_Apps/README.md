### Load Testing Streamlit Apps using Locust
+ Load testing is a kind of performance testing which determines a system’s or an application’s performance under real-life load conditions.
+ It is the process of simulating multiple users using your app at the same time or concurrently.

#### Requirements
+ Your streamlit app.py file
+ locust_file.py : instructions about endpoints
```bash
pip install streamlit locust
```

#### Usage
```bash
streamlit run app.py 
```
In another terminal you can run
```bash
locust -f locust_file.py
```

#### To Do
+ load testing individual sections of the streamlit app 

#### .
+ Jesus Saves @JCharisTech
+ Jesse E.Agbe(JCharis)

