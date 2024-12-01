import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Your Network, {st.session_state['first_name']}.")
st.write('')
st.write('')

if st.button('Find More Mentees', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/15_Mentor_Find_Mentees.py')