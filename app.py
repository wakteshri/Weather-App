import streamlit as st
import requests
from dotenv import load_dotenv
import os#environment is variable of operaating system
load_dotenv()
API_KEY=os.getenv("WEATHER_API_KEY") 
st.set_page_config(page_title="Wheather App",page_icon="⛅")

st.title("Weather App ⛅")
st.write("enter the city name and click on the  button to fetch the wheather data")

city=st.text_input("enter the city name ")
if( st.button("fetch wheather data")):
    API_URL=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response=requests.get(API_URL)
    if(response.status_code==200):
        st.success("Data fetch successfully")
        data=response.json()#  data is dictionaty 
        response=requests.get(API_URL)
        print(response.json())#.json method used to convert the response into json format{}//dictionary 
        
        #extract data in variables
        temperature = data['main']['temp']  
        humidity = data['main']['humidity']  
        wind_speed = data['wind']['speed']  
        condition =data["weather"][0]["main"]
        country=data["sys"]["country"]
        name=data["name"]

        #display the data 
        st.header(f"{name},{country}")
        col1,col2=st.columns(2)
        col3,col4,=st.columns(2)
        #col5=st.columns(2)

        col1.metric("Temperature",f"{temperature}🌡️℃")
        col2.metric("Humidity",f"{humidity}💧%")
        col3.metric("Wind speed",f"{wind_speed}💨m/s")
        col4.metric("Condition",f"{condition}⛅")
        #col5.metric("Country",f"{country}")
    else:
        st.error("invalid city name ")
    
