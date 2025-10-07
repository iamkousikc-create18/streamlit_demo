import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Welcome To Our Creations") 
st.header("Welcome To Our Creations Header")
st.subheader("Welcome To Our Creations Sub-Header")
st.write("Welcome To Our Creations Text")
st.markdown("Welcome To Our Creations Markdown")
st.caption("Welcome To Our Creations Caption")

st.image("ipl.jpg")
st.audio("myrec.m4a")
st.caption("Playing Audio....")
st.video("vid.mp4")
st.caption("Playing Video")


st.checkbox("I am Checkbox")
st.button("Click button")
st.radio("Your City",["Bangaluru","Mumbai","Kolkata","Delhi"])
st.selectbox("Your Stream",["AIML","Data Science","Cyber Security","BCA"])
st.multiselect("Your Favorite Sports",["Cricket","Football","Golf","Hockey"])
st.select_slider("Give Your Feedback",["bad","Good","Very Good","Excellent"])
st.slider("Your Marks Percentage %",0,100)

on=st.toggle("Activate Feature")
if on:
    st.write("Feature Activated")


number=st.number_input("Insert a number")
st.write("The current number is ",number)

d=st.date_input("When's Your Birthday",value=None)
st.write("Your Birthday is ",d)

t=st.time_input("Set Alarm",value=None)
st.write("Alarm is set for",t)

st.number_input("Enter Your Marks",0,100)
st.text_input("Enter text")
st.date_input("Exam date")
st.time_input("Exam time")
st.text_area("Description")
st.file_uploader("Upload File")
st.color_picker("Choose Your Favorite Color")

st.success("Success")
st.error("Error")
st.warning("Warning")
st.info("Information")
st.exception(RuntimeError("Runtime Error Exception"))

st.sidebar.title("Virat Vai")
st.sidebar.image("virat.jpg")

actor_images={"Hrithik":"hrithik.jpg","Ranbir":"ranbir.jpg",
              "Tiger":"tiger.jpg","Varun":"varun.jpg"}
selected_actor=st.selectbox("Choose Your Favorite Actor: ",list(actor_images.keys()))
st.image(actor_images[selected_actor],caption=selected_actor,use_container_width=True)

df=pd.DataFrame(np.random.randn(50,20),columns=("col %d" % i for i in range(20)))
st.dataframe(df)

dt=pd.DataFrame(np.random.randn(10,5),columns=("col %d" % i for i in range(5)))
st.table(dt)

col1,col2,col3=st.columns(3)
col1.metric("Temperature","70 °F","1.2 °F")
col2.metric("Wind","9 mph","-8%")
col3.metric("Humidity","86%","4%")

prompt=st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")


with st.status("Step 1"):
    st.write("Step 2")
    time.sleep(1)
    st.write("Step 3")
    time.sleep(1)
    st.write("Step 4")
    time.sleep(1)
st.button("Rerun")

chart_data=pd.DataFrame(np.random.randn(20,3),columns=["a","b","c"])
st.area_chart(chart_data)

chart_data=pd.DataFrame(np.random.randn(20,3),columns=["a","b","c"])
st.bar_chart(chart_data)

chart_data=pd.DataFrame(np.random.randn(20,3),columns=["a","b","c"])
st.line_chart(chart_data)

df=pd.DataFrame({
    'lat':[23.295982],'lon':[88.182342]
})
st.map(df)

chart_data=pd.DataFrame(np.random.randn(20,3),columns=["a","b","c"])
st.scatter_chart(chart_data)

with st.chat_message("user"):
    st.write("Namaste India")