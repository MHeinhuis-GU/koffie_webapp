import streamlit as st
import time
import csv
import os

# To run:
# $ python -m streamlit run src/testing_streamlit.py

# /explain Is it possible to turn this into a website that people can visit that all write to the same csv?

# Yes, it is possible to turn this Streamlit app into a website that people can visit and write to the same CSV file. Here are the steps to deploy it on Streamlit Cloud, which is a straightforward way to host Streamlit apps:

# Create a GitHub Repository:

# Create a new repository on GitHub and push your testing_streamlit.py script to it.
# Deploy on Streamlit Cloud:

# Go to Streamlit Cloud and sign in with your GitHub account.
# Create a new app and connect it to your GitHub repository containing the testing_streamlit.py script.
# Deploy the app.
# Share the URL:

# Once deployed, Streamlit Cloud will provide you with a URL that you can share with others.
# Ensure CSV File Accessibility:

# Make sure the coffee_data.csv file is accessible and has the correct permissions for writing data. If the file does not exist, the script will create it.
# Here is the updated script with a check to create the CSV file if it does not exist:

st.title("Manon's koffieonderzoek")

st.write(f"Welkom bij dit koffieonderzoek! Vul de onderstaande vragen in om deel te nemen. De wachtrij voordat je bij het koffiezetapperaat staat hoort er niet bij.")

# Selecteer drankje (koffie of thee)

drink = st.selectbox("Selecteer je drankje:", ["koffie", "thee"])


floor = st.selectbox(f"Selecteer de verdieping waar je de {drink} haalt:", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

machine = st.selectbox(f"Optioneel als er 2 machines zijn. Selecteer de koffiemachine waar je {drink} haalt:", ["enige", "raamkant", "hal kant"], index=0)

# This is an optional one to fill in, if none are selected, the value should become "enige"
# machine = st.selectbox("Optioneel als er 2 machines zijn. Selecteer de koffiemachine waar je koffie haalt:", ["enige", "raamkant", "hal kant"])



# start_time = st.button('Start Timer')
# if start_time:
#     start = tm.time()
#     st.write("Timer started...")

# stop_time = st.button('Stop Timer')
# if stop_time:
#     end = tm.time()
#     duration = int(end - start)
#     st.write(f"Timer stopped. Duration: {duration} seconds")
# else:
#     duration = st.slider("Select the duration of the coffee machine in seconds:", min_value=0, max_value=120, step=1)

st.write("Start de stopwatch om de tijd te meten die het koffiezetapperaat nodig heeft om je kopje te vullen. Als je dit zelf bij hebt gehouden kan je dit ook handmatig met de slider invullen.")

# Create a session state variable to store the stopwatch status and elapsed time
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0
if 'elapsed_time' not in st.session_state:
    st.session_state.elapsed_time = 0
if 'running' not in st.session_state:
    st.session_state.running = False

# Create a placeholder for the stopwatch display
stopwatch_placeholder = st.empty()

# Start the stopwatch
if st.button("Start"):
    if not st.session_state.running:  # If it's not already running, start it
        st.session_state.start_time = time.time() - st.session_state.elapsed_time  # Adjust the start time if resuming
        st.session_state.running = True

# Stop the stopwatch
if st.button("Stop"):
    if st.session_state.running:  # Only stop if it's running
        st.session_state.elapsed_time = time.time() - st.session_state.start_time
        st.session_state.running = False

# Reset the stopwatch
if st.button("Reset"):
    st.session_state.elapsed_time = 0
    st.session_state.running = False
    st.session_state.start_time = 0

# Update the display every second if the stopwatch is running
while st.session_state.running:
    elapsed_time = time.time() - st.session_state.start_time
    minutes = int(elapsed_time) // 60
    seconds = int(elapsed_time) % 60
    stopwatch_placeholder.text(f"Stopwatch: {minutes:02d}:{seconds:02d}")
    time.sleep(1)

# Display the current time if the stopwatch is not running
if not st.session_state.running:
    elapsed_time = st.session_state.elapsed_time
    minutes = int(elapsed_time) // 60
    seconds = int(elapsed_time) % 60
    stopwatch_placeholder.text(f"Stopwatch: {minutes:02d}:{seconds:02d}")

manual_duration = st.slider("Selecteer, in seconden, hoelang het koffiezetapperaat over je kopje deed:", min_value=0, max_value=120, step=1)


duration = int(st.session_state.elapsed_time) if st.session_state.elapsed_time > 1 else manual_duration

time = st.time_input("Selecteer de tijd van de dag:")

st.write(f"Je haalde {drink} op de {floor}e verdieping om {time}, wat {duration} seconden duurde, klik op Done om je response te delen. Bedankt voor het meedoen!")



# Define the file path
file_path = 'coffee_data.csv'

# Check if the file exists, if not create it with headers
if not os.path.exists(file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Floor', 'Drink', 'Machine', 'Time', 'Duration'])

if st.button('Done'):
    # Write the data to the CSV file
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([floor, drink, machine, time.strftime("%H:%M:%S"), duration])

    st.write(f"Data saved to {file_path}")

# Instructions to host the Streamlit app:
# 1. Make sure you have Streamlit installed: `pip install streamlit`
# 2. Save your script and run it using the command: `streamlit run src/testing_streamlit.py`
# 3. To allow others to access your app, you need to deploy it on a cloud platform like Streamlit Cloud, Heroku, or any other hosting service that supports Python applications.

# Example for deploying on Streamlit Cloud:
# 1. Create a Streamlit Cloud account at https://streamlit.io/cloud
# 2. Create a new app and connect it to your GitHub repository containing this script.
# 3. Deploy the app and share the generated URL with others.

# Example for deploying on Heroku:
# 1. Create a `requirements.txt` file with the following content:
# streamlit
# 2. Create a `Procfile` with the following content:
# web: streamlit run src/testing_streamlit.py
# 3. Install the Heroku CLI and log in: `heroku login`
# 4. Create a new Heroku app: `heroku create your-app-name`
# 5. Push your code to Heroku: `git push heroku main`
# 6. Open the app in your browser: `heroku open`