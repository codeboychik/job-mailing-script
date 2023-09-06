import os

import streamlit as st
from streamlit_player import st_player
import requests
from datetime import date
import json
import dotenv

dotenv.load_dotenv()

data = json.loads(
    requests.get(
        "https://api.nasa.gov/planetary/apod",
        params={
            "api_key": os.getenv('NASA_API_KEY'),
            "date": str(date.today()),
        },
    ).content.decode("utf-8")
)

st.set_page_config("Astronomy Picture of the Day", "expanded")
st.header(f"Astronomy Picture of the Day: {data['title']}")
st.subheader(f'Today\'s date: {data["date"].replace("-", ".")}')

if data['media_type'] == 'video':
    st_player(data["url"])
elif data['media_type'] == 'image':
    st.image(data['url'])

st.write(data['explanation'])
