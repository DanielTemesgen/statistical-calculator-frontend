from typing import List

import streamlit as st
import requests


@st.cache
def calculate(numbers: List[float]):
    url = 'https://7z8boxyi92.execute-api.us-east-1.amazonaws.com'
    endpoint = '/prod/stats/'
    query = {'numbers': numbers}
    r = requests.get(url + endpoint, params=query)
    return r


st.write("# Statistical Calculator")

raw_num = st.text_area(
    label='Insert a list of numbers separated by a comma.',
    value='1,2,3',
    height=10)

try:
    parsed_numbers = [int(num) for num in raw_num.strip(" ").split(',')]
except ValueError as e:
    st.error('Insert a list of numbers separated by a comma.')
else:
    st.success("The statistical description:")
    st.write(calculate(parsed_numbers).json())
