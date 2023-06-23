#load libraries

import pandas as pd
from google.cloud import pubsub_v1
import json
import time
import datetime
import random
import uuid


project_id = "google-project-id" #google cloud project id
topic_id = "python_bigquery" # pubsub topic name

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

def random_dataset():

    while True:
        current_datetime = datetime.datetime.now()
        datetime_series = pd.Series(current_datetime)
        # Gender generator
        gender_options = ['Male','Female']
        random_gender = random.choice(gender_options)
        gender_series = pd.Series(random_gender)
        # Age generator
        random_age = random.randint(18, 65)
        age_series = pd.Series(random_age)
        # State generator
        state_options = ['CA','NY','TX','FL','IL','PA','OH','GA','NC','MI','NJ','VA','WA','AZ','MA','TN','IN','MO','MD','WI','CO','MN','SC','AL','LA','KY','OR','OK','CT','UT','IA','NV','AR','MS','KS','NM','NE','WV','ID','HI','ME','NH','RI','MT','DE','SD','ND','AK','DC','VT','WY']
        random_state = random.choice(state_options)
        state_series = pd.Series(random_state)
        #ID generator
        random_id = uuid.uuid4()
        id_series = pd.Series(random_id)
        #salary generator
        random_salary = random.randint(40000, 200000)
        salary_series = pd.Series(random_salary)
        #marital status generator
        marital_options = ['Married','Single','Divorced','Widowed']
        random_marital = random.choice(marital_options)
        marital_series = pd.Series(random_marital)
        #number of children generator
        random_children = random.randint(0, 5)
        children_series = pd.Series(random_children)
        #number of cars generator
        random_cars = random.randint(0, 3)
        cars_series = pd.Series(random_cars)
        # random weight generator
        random_weight = random.randint(100, 300)
        weight_series = pd.Series(random_weight)
        # random height generator
        random_height = random.randint(150, 200)
        height_series = pd.Series(random_height)
        # random weather generator
        weather_options = round(random.uniform(-20, 100),2)
        weather_series = pd.Series(weather_options)
        # pandas dataframe
        df = pd.concat([datetime_series,id_series,gender_series,weight_series,height_series,age_series,salary_series,state_series,marital_series,children_series,cars_series,weather_series],axis=1)
        df.columns = ['DateTime','ID','Gender','Weight','Height','Age','Salary','State','Marital Status','Number of Children','Number of Cars','Weather']
        # convert to json
        df_json = df.to_json(orient='records',force_ascii=False, default_handler=str)
        # publish to pubsub
        data = json.dumps(df_json).encode('utf-8')
        publisher.publish(topic_path, data=data)

        time.sleep(30)


if __name__ == '__main__':
    random_dataset()



