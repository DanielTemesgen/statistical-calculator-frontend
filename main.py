from typing import List

import streamlit as st
import requests


@st.cache
def calculate(numbers: List[float]) -> requests.Response:
    """Performs the statistical calculation by sending in the array of numbers to the API.

    Args:
        numbers: list of numbers to send to the API.

    Returns:
        a requests response object that can be queried.
    """
    url = 'https://7z8boxyi92.execute-api.us-east-1.amazonaws.com'
    endpoint = '/prod/stats/'
    query = {'numbers': numbers}
    r = requests.get(url + endpoint, params=query)
    return r


def display(numbers: List[float]):
    """Display a success message if the API has a positive status and an error if not.
    Either way the response is displayed.

    Args:
        numbers:
    """
    response = calculate(numbers)
    if response.status_code == 200:
        st.success("The statistical description:")
    else:
        st.error('API Error (see below)')

    st.write(response.json())


st.write("# Statistical Calculator")

raw_num = st.text_area(
    label='Insert a list of numbers separated by a comma.',
    value='1,2,3,42',
    height=10)

try:
    parsed_numbers = [int(num) for num in raw_num.strip(" ").split(',')]
except ValueError as e:
    st.error('Insert a list of numbers separated by a comma.')
else:
    display(parsed_numbers)
