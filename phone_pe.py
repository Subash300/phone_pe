# [Dash board libraries]
import streamlit as st

# [clone libraries]

import requests

# [pandas, numpy and file handling libraries]
import pandas as pd
import numpy as np
import json

# [SQL libraries]
import pymysql

# [Dash board libraries]
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu

from PIL import Image

# ==============================================         /   /   CONNECTION SQL   /   /         ================================================== #

# CONNECT TO SQL

conn = pymysql.connect(host='localhost', user='root', password='root', db='phonepe_pe')
cursor = conn.cursor()



# ==============================================         /   /   DASHBOARD   /   /         ================================================== #

selected = option_menu(
    menu_title="Main Menu",
    options=["Home", "About","Analysis","Insights"],
    icons = ["bar-chart","house","toggles","at"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
    # styles={"container": {"width": "100%"},
    #                            "icon": {"color": "white", "font-size": "24px"},
    #                            "nav-link": {"font-size": "24px", "text-align": "center", "margin": "-2px"},
    #                            "nav-link-selected": {"background-color": "#6F36AD"}}
)


st.set_page_config(layout="wide")





# --- HOME TAB ---
if selected == "Home":
    col1, col2 = st.columns(2)
    with col1:
        img_path = r"D:\phone_pe\249336164-fa39d457-d483-495b-bec7-467abfe66e39.jpg"
        st.image(Image.open(img_path), width=500)
    with col2:
        st.title(':violet[PHONEPE PULSE DATA VISUALISATION]')
        st.subheader(':violet[Phonepe Pulse]:')
        st.write('PhonePe Pulse is a feature offered by the Indian digital payments platform called PhonePe. '
                 'PhonePe Pulse provides users with insights and trends related to their digital transactions and usage patterns on the PhonePe app.')
        st.subheader(':violet[Phonepe Pulse Data Visualisation]:')
        st.write('Data visualization refers to the graphical representation of data using charts, graphs, and other visual elements to facilitate understanding and analysis in a visually appealing manner. '
                 'The goal is to extract this data and process it to obtain insights and information that can be visualized in a user-friendly manner.')
        st.markdown("## :violet[Done by] : SUBASH S")
        st.markdown("[Inspired from](https://www.phonepe.com/pulse/)")
        st.markdown("[Githublink](https://github.com/beingbvh)")
        st.markdown("[LinkedIn](https://www.linkedin.com/in/balavignesh-s-s-6133b727a/)")
    st.write("---")

# --- ABOUT TAB ---
if selected == "About":
    col1, col2 = st.columns(2)
    img_path = r"D:\phone_pe\249336164-fa39d457-d483-495b-bec7-467abfe66e39.jpg"
    col1.image(Image.open(img_path), width=500)
    
    with col1:
        st.subheader(
            "PhonePe is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. "
            "PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. "
            "The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. "
            "It is owned by Flipkart, a subsidiary of Walmart."
        )
        st.markdown("[DOWNLOAD APP](https://www.phonepe.com/app-download/)")
    
    with col2:
        video_path = r"D:\phone_pe\pulse-video.mp4"
        st.video(video_path)

        # ANALYSIS TAB
if selected == "Analysis":
    st.title(':violet[ANALYSIS]')
    st.subheader('Analysis done on the basis of All India ,States and Top categories between 2020 and 2024')
    select = option_menu(None,
                         options=["INDIA", "STATES", "TOP CATEGORIES" ],
                         default_index=0,
                         orientation="horizontal",
                         styles={"container": {"width": "100%"},
                                   "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px"},
                                   "nav-link-selected": {"background-color": "#6F36AD"}})
    
    if select == "INDIA":
        tab1, tab2 , tab3 = st.tabs(["TRANSACTION","USER","INSURANCE"])

        # TRANSACTION TAB
        with tab1:
            col1, col2, col3 = st.columns(3)
            with col1:
                in_tr_yr = st.selectbox('**Select Year**', ('2020', '2021', '2022', '2023', '2024'), key='in_tr_yr')
            with col2:
                in_tr_qtr = st.selectbox('**Select Quarter**', ('1', '2', '3', '4','5'), key='in_tr_qtr')
            with col3:
                in_tr_tr_typ = st.selectbox('**Select Transaction type**',
                                            ('Recharge & bill payments', 'Peer-to-peer payments',
                                             'Merchant payments', 'Financial Services', 'Others'), key='in_tr_tr_typ')
            # SQL Query
            # Transaction Analysis bar chart query
            cursor.execute(
                f"SELECT State, Transaction_amount FROM aggregated_transaction WHERE Year = '{in_tr_yr}' AND Quarter = '{in_tr_qtr}' AND Transaction_type = '{in_tr_tr_typ}';")
            in_tr_tab_qry_rslt = cursor.fetchall()
            df_in_tr_tab_qry_rslt = pd.DataFrame(np.array(in_tr_tab_qry_rslt), columns=['State', 'Transaction_amount'])
            df_in_tr_tab_qry_rslt1 = df_in_tr_tab_qry_rslt.set_index(pd.Index(range(1, len(df_in_tr_tab_qry_rslt) + 1)))

       
        