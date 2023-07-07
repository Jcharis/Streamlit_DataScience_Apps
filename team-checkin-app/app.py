import streamlit as st
import pandas as pd
import base64
import os
import datetime
import sqlalchemy as sa
from pathlib import Path
import psycopg2

#creating sql alchemy engine
engine = sa.create_engine('',echo=False) #add your heroku postgres url
def check_if_weekend(today):
    try:
        isinstance(today, datetime.datetime)
        upper_limit = today + datetime.timedelta(days=(6 - today.weekday()))
        lower_limit = today + datetime.timedelta(days=(5 - today.weekday()))
        if today >= lower_limit <= upper_limit:
            return True
        else:
            return False
    except ValueError:
        pass


today_date = datetime.datetime.today()
weekend = check_if_weekend(today_date)


if weekend==True:
    os.remove('week_log.csv')
    try:
        engine.execute('DROP TABLE table2')
    except:
        pass
    new_week_log = pd.DataFrame(columns=['Name', 'Time', 'Days', 'Hours', 'Reason', 'Team'],index=None)
    new_week_log.to_csv('week_log.csv', mode='w', header=True,index=None)
    new_week_log.to_sql('table2',con=engine,index=False,index_label=None,if_exists='replace')
else:
    try:
        new_week_log=pd.read_sql('table2',con=engine,index_col=None)
    except:
        new_week_log = pd.DataFrame(columns=['Name', 'Time', 'Days', 'Hours', 'Reason', 'Team'])
        new_week_log.to_sql('table2', con=engine, index=False, index_label=None, if_exists='replace')
        new_week_log = pd.read_sql('table2', con=engine, index_col=None)


st.title('Work Checkin System')

st.sidebar.image('logo.jpg')
st.sidebar.markdown("""
    ***XYZ Team***
""")

data=pd.read_csv('data.csv',header=[0])
if os.path.exists('record.csv'):
    try:
        record=pd.read_sql('table1',con=engine,index_col=None)
    except:
        record=pd.read_csv('record.csv',index_col=None)
        record.to_sql('table1',con=engine,index=False,index_label=None,if_exists='append')
else:
    record = pd.DataFrame(columns=['Name', 'Time', 'Days', 'Hours', 'Reason', 'Team'],index=None)
    record.to_csv('record.csv', mode='w', header=True,index=None)
    record.to_sql('table1',con=engine,index=False,index_label=None,if_exists='replace')
st.write(record)
#st.write(pd.read_sql('table1',con=engine,index_col=None))

days=['mon','tue','wed','thurs','fri','sat','sun']
teams=['Development','PR','management']
st.warning('Avoid duplication, ignore if not applicable')
st.error('During the time of weekend it will reset itself and you wont be able to do any changes , dont checkin during the weekends')


def input_values():
    data2 = pd.read_csv('data.csv', header=[0])

    if st.sidebar.checkbox('Work for this week'):
            selected_name = st.sidebar.selectbox('Name', options=data['Members'])
            days_selected=st.sidebar.multiselect('Days free to work',options=days)
            hours=st.sidebar.slider('No.of hours per week will be able to work',1.0,1.0,8.0)
            team_willing=st.sidebar.multiselect('Team willing to work in',options=teams)
            password=str(st.sidebar.text_input('enter the passphrase')).lower()

            if st.sidebar.button('Submit details'):
                y=data2.loc[data2.Members == str(selected_name)]
                z=y.iloc[:,-1].values
                if password==str(z[0]):
                    st.balloons()
                    input_data={
                        'Name':[str(selected_name)],
                        'Time':[str(datetime.datetime.today())],
                        'Days':[str(days_selected)],
                        'Hours':[str(hours)],
                        'Reason':['None'],
                        'Team':[str(team_willing)]
                    }
                    input_df=pd.DataFrame(input_data)
                    input_df.to_csv('record.csv', mode='a', header=False,index=None)
                    input_df.to_sql('table1',if_exists='append',con=engine,index=False,index_label=None)
                    record_changed = pd.read_sql('table1',con=engine,index_col=None)
                    record_reverse = record_changed.iloc[::-1]
                    st.subheader('Continous Log')
                    st.write(record_reverse.head())
                    input_df.to_csv('week_log.csv', mode='a', header=False,index=None)
                    input_df.to_sql('table2', if_exists='append', con=engine, index=False, index_label=None)
                    record_changed_wl = pd.read_sql('table2',con=engine,index_col=None)
                    record_reverse_wl = record_changed_wl.iloc[::-1]
                    st.subheader('Weekly Log')
                    st.write(record_reverse_wl.head())
                else:
                    st.sidebar.warning('Wrong passphrase')
    elif st.sidebar.checkbox('Cannot Work this week'):
            selected_name = st.sidebar.selectbox('Name', options=data['Members'])
            reason=st.sidebar.text_input('Reason')
            password = str(st.sidebar.text_input('enter the passphrase')).lower()
            if st.sidebar.button('Submit details'):
                y = data2.loc[data2.Members == str(selected_name)]
                z = y.iloc[:, -1].values
                if password == str(z[0]):
                    st.balloons()
                    input_data={
                        'Name':[str(selected_name)],
                        'Time':[str(datetime.datetime.today())],
                        'Days':['None'],
                        'Hours':0,
                        'Reason':[str(reason)],
                        'Team':['None']
                    }
                    input_df=pd.DataFrame(input_data)
                    input_df.to_csv('record.csv', mode='a', header=False,index=None)
                    input_df.to_sql('table1', if_exists='append', con=engine, index=False, index_label=None)
                    record_changed = pd.read_sql('table1',con=engine,index_col=None)
                    record_reverse=record_changed.iloc[::-1]
                    st.subheader('Continous Log')
                    st.write(record_reverse.head())
                    input_df.to_csv('week_log.csv', mode='a', header=False,index=None)
                    input_df.to_sql('table2', if_exists='append', con=engine, index=False, index_label=None)
                    record_changed_wl = pd.read_sql('table2',con=engine,index_col=None)
                    record_reverse_wl = record_changed_wl.iloc[::-1]
                    st.subheader('Weekly Log')
                    st.write(record_reverse_wl.head())
                else:
                    st.sidebar.warning('Wrong passphrase')

input_values() # input values function

def filedownload():
    log=pd.read_sql('table1',con=engine,index_col=None)
    csv = log.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="teamlog.csv">Download Team entire Log File</a>'
    return href

def filedownload_week():
    log=pd.read_sql('table2',con=engine,index_col=None)
    csv = log.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="teamlog_week.csv">Download Team week Log File</a>'
    return href

new_log_df=pd.read_sql('table2',con=engine,index_col=None)
people_data=data.copy()


st.write('Total no.of work hours reported {}'.format(new_log_df['Hours'].sum()))

col1,col2,col3=st.beta_columns(3)
with col1:
    st.header('Team updated')
    unique_names=new_log_df['Name'].unique()
    st.write(unique_names)
with col2:
    st.header('Team Not updated')
    name1 = set(new_log_df['Name'])
    name2 = set(people_data['Members'])
    diff = sorted(name2 - name1)
    st.write(pd.DataFrame(diff))
with col3:
    data={
        'Updated':new_log_df['Name'].nunique(),
        'Not-Updated':people_data['Members'].nunique()-new_log_df['Name'].nunique()
    }
    st.header('Comparision between updation for current week')
    st.bar_chart(data=pd.DataFrame(data,index=[0]),use_container_width=True)
    bar_df=pd.DataFrame(data,index=[0])


st.markdown(filedownload_week(), unsafe_allow_html=True)

st.markdown(filedownload(), unsafe_allow_html=True)
