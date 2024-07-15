import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
from st_on_hover_tabs import on_hover_tabs
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit_analytics
import base64
from streamlit_extras.mention import mention
from streamlit_extras.app_logo import add_logo
from streamlit_extras.echo_expander import echo_expander
import pandas as pd
#from pandas import json_normalize
import openpyxl
import numpy as np
from matplotlib import pyplot as plt
import pymysql
import sqlalchemy
import MySQLdb
#import mysqlclient
#import mysql.connector
#from sqlalchemy import create_engine
#import pyodbc
# from zlib_ng import zlib_ng
# from zlib_ng import gzip_ng
# from zlib_ng import gzip_ng_threaded
#import plotly_express as px
#AgGrid advanced streamlit table/dataframe formatter
#from st_aggrid import AgGrid, GridOptionsBuilder

# Set page title
st.set_page_config(page_title="Blues", page_icon = "ice_hockey_stick_and_puck", layout = "wide", initial_sidebar_state = "auto")


#Fetching the secrets
connection_info = st.secrets["connections"]["mysql"]

# Establishing the connection
conn= st.connection('mysql', type='sql')
conn = pymysql.connect(
    host=connection_info["host"],
    port=connection_info["port"],
    user=connection_info["username"],
    password=connection_info["password"],
    database=connection_info["database"],
    charset=connection_info["query"]["charset"]
)





# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_lottie(url, width, height):
    lottie_html = f"""
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.14/lottie.min.js"></script>
    </head>
    <body>
        <div id="lottie-container" style="width: {width}; height: {height};"></div>
        <script>
            var animation = lottie.loadAnimation({{
                container: document.getElementById('lottie-container'),
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: '{url}'
            }});
            animation.setRendererSettings({{
                preserveAspectRatio: 'xMidYMid slice',
                clearCanvas: true,
                progressiveLoad: false,
                hideOnTransparent: true
            }});
        </script>
    </body>
    </html>
    """
    return lottie_html

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

footer = """
footer{
    visibility:visible;
}
footer:after{
    content:'Copyright © 2023 St.Louis Blues';
    position:relative;
    color:black;
}
"""

# Load assets
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# Assets for Home Page
img_utown = Image.open("images/BluesHomePageLogo.png")
img_lh = Image.open("images/RetroLogo.png")
#Stanley Cups
SC1=Image.open("images/StanleyCup1.png")
SC2=Image.open("images/StanleyCup2.png")
#Team Page Logos
#Atlantic Division
Bruins_logo=Image.open("images/boston_bruins.png")
Sabres_logo=Image.open("images/buffalo_sabres_21.png")
RedWings_logo=Image.open("images/detroit_red_wings.png")
Panthers_logo=Image.open("images/florida_panthers.png")
Canadiens_logo=Image.open("images/montreal_canadiens.png")
Senators_logo=Image.open("images/ottawa_senators_21.png")
Lightning_logo=Image.open("images/tampa_bay_lightning.png")
MapleLeafs_logo=Image.open("images/toronto_maple_leafs.png")
#Metro Division
Canes_logo=Image.open("images/carolina_hurricanes.png")
CBJ_logo=Image.open("images/columbus_blue_jackets.png")
Devils_logo=Image.open("images/new_jersey_devils.png")
Islanders_logo=Image.open("images/new_york_islanders.png")
Rangers_logo=Image.open("images/new_york_rangers.png")
Flyers_logo=Image.open("images/philadelphia_flyers.png")
Penguins_logo=Image.open("images/pittsburgh_penguins.png")
Caps_logo=Image.open("images/washington_capitals.png")
#Central Division
Hawks_logo= Image.open("images/chicago_blackhawks.png")
Avs_logo=Image.open("images/colorado_avalanche.png")
Stars_logo=Image.open("images/dallas_stars.png")
Wild_logo=Image.open("images/minnesota_wild.png")
Preds_logo=Image.open("images/nashville_predators.png")
Blues_logo=Image.open("images/st_louis_blues.png")
Utah_logo=Image.open("images/utah_hockey_club.png")
Winnipeg_logo=Image.open("images/winnipeg_jets.png")
#Pacific Division
Ducks_logo=Image.open("images/anaheim_ducks.png")
Flames_logo= Image.open("images/calgary_flames.png")
Oilers_logo=Image.open("images/edmonton_oilers.png")
Kings_logo=Image.open("images/los_angeles_kings.png")
Sharks_logo=Image.open("images/san_jose_sharks.png")
Kraken_logo=Image.open("images/seattle_kraken.png")
Canucks_logo=Image.open("images/vancouver_canucks.png")
VGK_logo=Image.open("images/vegas_golden_knights.png")
#Dataframes for team pages
#Pacific Division
#Anaheim Ducks
# ducks_forwards=pd.read_csv("Anaheim Ducks/Cap Friendly Ducks Forwards.csv")
# ducks_defense=pd.read_csv("Anaheim Ducks/Cap Friendly Ducks Defense.csv")
# ducks_goalies=pd.read_csv("Anaheim Ducks/Cap Friendly Ducks Goalies.csv")
# ducks_ir = pd.read_csv("Anaheim Ducks/Cap Friendly Ducks IR.csv")
# ducks_DCB = pd.read_csv("Anaheim Ducks/Cap Friendly Ducks Dead Cap Buyout.csv")
# ducks_NRF = pd.read_csv("Anaheim Ducks/Cap Friendly Ducks Non-Roster Forwards.csv")
# ducks_NRD = pd.read_csv("Anaheim Ducks/Cap Friendly Ducks Non-Roster Defense.csv")
# ducks_NRG = pd.read_csv("Anaheim Ducks/Cap Friendly Ducks Non-Roster Goalies.csv")
#Calgary Flames
# Flames_forwards=pd.read_csv("Calgary Flames/Cap Friendly Flames Forwards.csv")
# Flames_defense=pd.read_csv("Calgary Flames/Cap Friendly Flames Defense.csv")
# Flames_goalies=pd.read_csv("Calgary Flames/Cap Friendly Flames Goalies.csv")
# Flames_DCB = pd.read_csv("Calgary Flames/Cap Friendly Flames Dead Cap Retained.csv")
# Flames_NRF = pd.read_csv("Calgary Flames/Cap Friendly Flames Non-Roster Forwards.csv")
# Flames_NRD = pd.read_csv("Calgary Flames/Cap Friendly Flames Non-Roster Defense.csv")
# Flames_NRG = pd.read_csv("Calgary Flames/Cap Friendly Flames Non-Roster Goalies.csv")

#AgGrid advanced table
#Create GridOptionsBuilder from dataframe and enable autoSizeColumns and resizable
# def configure_grid_options(df):
#     gb = GridOptionsBuilder.from_dataframe(df)
#     gb.configure_default_column(resizable=True, autoSizeColumns=True)
#     return gb.build()
#img_lottie_animation = Image.open("images/lottie_animation.gif")
# Assets for contact
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_abqysclq.json")

img_github = Image.open("images/icons8-github-100.png")

def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 20px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "github": "https://img.icons8.com/?size=100&id=12599&format=png&color=#d9d1d1"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    b_no_commas = b.replace(',', '')
    st.markdown(b_no_commas)

def txt4(a, b):
  col1, col2 = st.columns([1.5,2])
  with col1:
    st.markdown(f'<p style="font-size: 25px; color: white;">{a}</p>', unsafe_allow_html=True)
  with col2: #can't seem to change color besides green
    st.markdown(f'<p style="font-size: 25px; color: red;"><code>{b}</code></p>', unsafe_allow_html=True)

#####################

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg.png')   


# Sidebar: If using streamlit_option_menu
with st.sidebar:
    with st.container():
        l, m, r = st.columns((1,3,1))
        with l:
            st.empty()
        with m:
            st.image(img_lh, width=175)
        with r:
            st.empty()
    
    choose = option_menu(
                        "Options", 
                        ["Home Page", "Active Players", "Cost Per Point", "Cost Per Save", "Trades", "Retained Salary", "Teams"],
                         icons=['globe fill', 'people', 'currency-dollar', 'piggy-bank-fill', 'repeat', 'percent', 'trophy fill'],
                         menu_icon="music-note-list", 
                         default_index=0,
                         styles={
        "container": {"padding": "0!important", "background-color": "#041E42"},
        "icon": {"color": "#d9d1d1", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#f44336"},
        "nav-link-selected": {"background-color": "#041E42"},
    }
    )
    github_url = "https://github.com/Nick3429/NHLSalaryCap"
    with st.container():
        l, m, r = st.columns((0.11,2,0.1))
        with l:
            st.empty()
        with m:
            st.markdown(
                social_icons(30, 30, GitHub=github_url),
                unsafe_allow_html=True)
        with r:
            st.empty()

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.title("St. Louis Blues Analytics")
# Create header
if choose == "Home Page":
    #aboutme.createPage()
    with st.container():
        left_column, middle_column, right_column = st.columns((1,0.2,0.5))
        with left_column:
            st.header("Home Page")
            st.subheader("What is included in this Website")
            st.write("This Website will serve as the internal analytics and Salary Cap system for the St. Louis Blues. In the navigation bar on the left, it will contain 7 pages: Homepage, Active Players, Cost per Point, Cost per Save, Trades, Retained Salary, and a Teams Page.")
            st.write(" The Active Players Tab will allow you to find any contract information out on any player in the league. It will also allow you to filter by players who will be free agents after their contract expires or  RFA's after their contract expires so you can find potential players to target in the offseason. In addition, player stats will be included as well in this page. This page serves as the ultimate page to find out contract information or statistical information on any player.")
            st.write(" The Cost per Point page will allow you to see which players are giving you the most bang for your buck in terms of their point production, goal production, assists production, and time on ice. Allows you to evaluate players from a points against salary perspective.")
            st.write("The Cost per Save page will allow you to evaluate goalies in terms of which ones give you the most bang for their buck. Same idea as the Cost per point page but just for goalies.")
            st.write("The trades page will allow you to find every trade that occured in the league during the past 3 seasons.")
           # st.write("📄 [Resume (1 page)](https://drive.google.com/file/d/164EEVH6BmvC89q2M4WsBNF1JyddDAbNY/view?usp=sharing)")
        with middle_column:
            st.empty()
        with right_column:
            st.image(img_utown)
elif choose == "Active Players":   
    #overview.createPage()
    figure=plt.figure()
    st.markdown("<h1 style='text-align: center;'> Active Players </h1>",unsafe_allow_html=True)
    season_options = ["Regular Season 2030-31","Regular Season 2029-30","Regular Season 2028-29","Regular Season 2027-28","Regular Season 2026-27","Regular Season 2025-26","Regular Season 2024-25","Regular Season 2023-24", "Regular Season 2022-23", "Regular Season 2021-22", "Regular Season 2020-21","Regular Season 2019-20", "Regular Season 2018-19", "Regular Season 2017-18", "Regular Season 2016-17"]
    with st.container():
        season=st.selectbox("Pick a season", options = season_options)

        #Map season option to corresponding table name
        season_to_table_map={
            "Regular Season 2030-31": "cf 2030-31 active players data",
            "Regular Season 2029-30": "cf 2029-30 active players data",
            "Regular Season 2028-29": "cf 2028-29 active players data",
            "Regular Season 2027-28": "cf 2027-28 active players data",
            "Regular Season 2026-27": "cf 2026-27 active players data",
            "Regular Season 2025-26": "cf 2025-26 active players data",
            "Regular Season 2024-25": "cf 2024-25 active players data",
            "Regular Season 2023-24": "cf 2023-24 active players data",
            "Regular Season 2022-23": "cf 2022-23 active players data",
            "Regular Season 2021-22": "cf 2021-22 active players data",
            "Regular Season 2020-21": "cf 2020-21 active players data",
            "Regular Season 2019-20": "cf 2019-20 active players data",
            "Regular Season 2018-19": "cf 2018-19 active players data",
            "Regular Season 2017-18": "cf 2017-18 active players data",
            "Regular Season 2016-17": "cf 2016-17 active players data"
        }
        # Get the table name based on the selected season
        table_name = season_to_table_map.get(season)
        if table_name:
            try:
                query = f"SELECT * FROM `{table_name}`"  # Query to get data from the corresponding table
                #engine=get_connection()
                #df = pd.read_sql(query, con=engine)
                df = pd.read_sql(query, conn)
                st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit without the index
            except pymysql.MySQLError as e:
                st.error(f"Error executing query: {e}")
            finally:
                   conn.close()
                   #connection.close()
                #    if 'engine' in locals():
                #        engine.dispose()  # Properly close the SQLAlchemy engine


# Create section for Cost Per Point
elif choose == "Cost Per Point":
    figure=plt.figure()
    st.markdown("<h1 style='text-align: center;'> Player Cost Per Point </h1>",unsafe_allow_html=True)
    season_options = ["Regular Season 2023-24", "Regular Season 2022-23", "Regular Season 2021-22", "Regular Season 2020-21","Regular Season 2019-20", "Regular Season 2018-19", "Regular Season 2017-18", "Regular Season 2016-17"]
    with st.container():
        season=st.selectbox("Pick a season", options = season_options)

        #Map season option to corresponding table name
        season_to_table_map={
            "Regular Season 2023-24": "cf cost per point 2023-24",
            "Regular Season 2022-23": "cf cost per point 2022-23",
            "Regular Season 2021-22": "cf cost per point 2021-22",
            "Regular Season 2020-21": "cf cost per point 2020-21",
            "Regular Season 2019-20": "cf cost per point 2019-20",
            "Regular Season 2018-19": "cf cost per point 2018-19",
            "Regular Season 2017-18": "cf cost per point 2017-18",
            "Regular Season 2016-17": "cf cost per point 2016-17"
        }
        # Get the table name based on the selected season
        table_name = season_to_table_map.get(season)
        if table_name:
            try:
                query = f"SELECT * FROM `{table_name}`"  # Query to get data from the corresponding table
                #df = pd.read_sql(query, get_connection())
                df = pd.read_sql(query, conn)
                st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit without the index
            except pymysql.MySQLError as e:
                st.error(f"Error executing query: {e}")
            finally:
                   conn.close()
                   #get_connection.close()

# Create section for Cost Per Save
elif choose == "Cost Per Save":
    st.markdown("<h1 style='text-align: center;'> Goalie Cost Per Save </h1>",unsafe_allow_html=True)
    #st.markdown("----",unsafe_allow_html=True)
    season_options = ["Regular Season 2023-24", "Regular Season 2022-23", "Regular Season 2021-22", "Regular Season 2020-21","Regular Season 2019-20", "Regular Season 2018-19", "Regular Season 2017-18", "Regular Season 2016-17"]
    with st.container():
        season=st.selectbox("Pick a season", options = season_options)

        #Map season option to corresponding table name
        season_to_table_map={
            "Regular Season 2023-24": "cf cost per save 2023-24",
            "Regular Season 2022-23": "cf cost per save 2022-23",
            "Regular Season 2021-22": "cf cost per save 2021-22",
            "Regular Season 2020-21": "cf cost per save 2020-21",
            "Regular Season 2019-20": "cf cost per save 2019-20",
            "Regular Season 2018-19": "cf cost per save 2018-19",
            "Regular Season 2017-18": "cf cost per save 2017-18",
            "Regular Season 2016-17": "cf cost per save 2016-17"
        }
        # Get the table name based on the selected season
        table_name = season_to_table_map.get(season)
        if table_name:
            try:
                query = f"SELECT * FROM `{table_name}`"  # Query to get data from the corresponding table
                #df = pd.read_sql(query, get_connection())
                df = pd.read_sql(query, conn)
                st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit without the index
            except pymysql.MySQLError as e:
                st.error(f"Error executing query: {e}")
            finally:
                   conn.close()
                   #get_connection.close()

# Create section for Trades
elif choose == "Trades":
    st.header("Trades")

# Create section for Retained Salary
elif choose == "Retained Salary":
    with st.container():
        st.markdown("<h1 style='text-align: center;'> Retained Salary </h1>",unsafe_allow_html=True)
        #st.header("Retained Salary")
        col1, col2, col3 = st.columns((1, 4, 1))
        #if get_connection():
        if conn:
            try:
                query = "SELECT * FROM `capfriendly retainedsalary`"  # Replace 'yourtable' with your actual table name
                #df = pd.read_sql(query, get_connection())
                df = pd.read_sql(query, conn)
                df= df.reset_index(drop=True)
                with col2:
                    st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
            except pymysql.MySQLError as e:
                st.error(f"Error executing query: {e}")
            finally:
                conn.close()
                #get_connection().close()
    
elif choose == "Teams":
    st.header("Teams")
    selected_options = ["Anaheim Ducks", "Boston Bruins", "Buffalo Sabres", "Calgary Flames", "Carolina Hurricanes","Chicago Blackhawks", "Colorado Avalanche", "Columbus Blue Jackets", "Dallas Stars", "Detroit Red Wings", "Edmonton Oilers", "Florida Panthers", "Los Angeles Kings", "Minnesota Wild", "Montreal Canadiens", "Nashville Predators", "New Jersey Devils","New York Islanders", "New York Rangers","Ottawa Senators","Philadelphia Flyers", "Pittsburgh Penguins", "San Jose Sharks","Seattle Kraken", "St. Louis Blues", "Tampa Bay Lightning", "Toronto Maple Leafs", "Utah Hockey Club","Vancouver Canucks", "Vegas Golden Knights","Washington Capitals","Winnipeg Jets"
                        ]
    selected = st.selectbox("Pick a team to view their cap situation", options = selected_options)
    st.write("Current selection:", selected)
    if selected == "Anaheim Ducks":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            #with blank_col1:
                #st.image(SC1)
            with main_col:
                st.image(Ducks_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Pat Verbeek*")
                st.write("*Head Coach: Greg Cronin*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly ducks forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly ducks defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly ducks goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly ducks ir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly ducks dead cap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly ducks non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly ducks non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly ducks non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Calgary Flames":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Flames_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Craig Conroy*")
                st.write("*Head Coach: Ryan Huska*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly flames forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly flames defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly flames goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly flames dead cap retained`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly flames non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly flames non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly flames non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Edmonton Oilers":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Oilers_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: None*")
                st.write("*Head Coach: Kris Knoblauch*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly oilers forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly oilers defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly oilers goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly oilers deadcap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly oilers non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly oilers non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly oilers non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Los Angeles Kings":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Kings_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Rob Blake*")
                st.write("*Head Coach: Jim Hiller*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly kings forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly kings defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly kings goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly kings dead cap retained`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly kings dead cap terminated penalty`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly kings non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly kings non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly kings non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "San Jose Sharks":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Sharks_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Mike Grier*")
                st.write("*Head Coach: Ryan Warsofsky*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly sharks forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly sharks defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly sharks goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly sharks ir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly sharks dead cap retained`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly sharks dead cap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly sharks non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly sharks non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly sharks non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Seattle Kraken":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Kraken_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Ron Francis*")
                st.write("*Head Coach: Dan Bylsma*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly kraken forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly kraken defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly kraken goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly kraken non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly kraken non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly kraken non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Vancouver Canucks":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Canucks_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Patrik Allvin*")
                st.write("*Head Coach: Rick Tocchet*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canucks forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canucks defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canucks goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canucks ltir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canucks dead cap retained`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canucks dead cap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canucks non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canucks non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canucks non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Vegas Golden Knights":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(VGK_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Kelly McCrimmon*")
                st.write("*Head Coach: Bruce Cassidy*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly vgk forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly vgk defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly vgk goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly vgk ltir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly vgk non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly vgk non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly vgk non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Chicago Blackhawks":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Hawks_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Kyle Davidson*")
                st.write("*Head Coach: Luke Richardson*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly blackhawks forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly blackhawks defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly blackhawks goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly blackhawks ir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly blackhawks deadcap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly blackhawks deadcap retained`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly blackhawks non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly blackhawks non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly blackhawks non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Colorado Avalanche":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Avs_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Chris MacFarland*")
                st.write("*Head Coach: Jared Bednar*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly avs forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly avs defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly avs goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly avs ir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly avs player assistance program`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly avs non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly avs non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly avs non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Dallas Stars":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Stars_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Jim Nill*")
                st.write("*Head Coach: Pete DeBoer*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly stars forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly stars defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly stars goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly stars dead cap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly stars non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly stars non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly stars non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Minnesota Wild":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Wild_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Bill Guerin*")
                st.write("*Head Coach: John Hynes*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly wild forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly wild defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly wild goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly wild ir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly wild dead cap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly wild non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly wild non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly wild non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Nashville Predators":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Preds_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Barry Trotz*")
                st.write("*Head Coach: Andrew Brunette*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly preds forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly preds defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly preds goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly preds deadcapbuyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly preds deadcapretained`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly preds non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly preds non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly preds non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "St. Louis Blues":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Blues_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Doug Armstrong*")
                st.write("*Head Coach: Drew Bannister*")
                st.write("Cap Hit: ")
                st.write("Cap Space: ")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly blues forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                              # st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly blues defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly blues goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly blues non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly blues non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly blues non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Utah Hockey Club":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Utah_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Bill Armstrong*")
                st.write("*Head Coach: Andre Tourigny*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly utah forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly utah defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly utah goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly utah ltir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly utah dead cap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly utah dead cap retained`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly utah non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly utah non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly utah non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Winnipeg Jets":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Winnipeg_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Kevin Cheveldayoff*")
                st.write("*Head Coach: Scott Arniel*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly jets forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly jets defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly jets goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly jets deadcap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly jets non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly jets non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly jets non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Carolina Hurricanes":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Canes_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Eric Tulsky*")
                st.write("*Head Coach: Rod Brind'Amour*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canes forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canes defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canes goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canes non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canes non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canes non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Columbus Blue Jackets":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(CBJ_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Don Waddell*")
                st.write("*Head Coach: *")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly cbj forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly cbj defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly cbj goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly cbj ir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly cbj player assistance program`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly cbj dead cap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly cbj non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly cbj non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly cbj non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "New Jersey Devils":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Devils_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Tom Fitzgerald*")
                st.write("*Head Coach: Sheldon Keefe*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly devils forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly devils defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly devils goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly devils ir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly devils dead cap recapture penalty`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly devils non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly devils non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly devils non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "New York Islanders":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Islanders_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Lou Lamoriello*")
                st.write("*Head Coach: Patrik Roy*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly islanders forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly islanders defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly islanders goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly islanders ir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly islanders dead cap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly islanders non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly islanders non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly islanders non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "New York Rangers":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Rangers_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Chris Drury*")
                st.write("*Head Coach: Peter Laviolette*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly rangers forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly rangers defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly rangers goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly rangers dead cap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly rangers non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly rangers non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly rangers non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Philadelphia Flyers":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Flyers_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Daniel Briere*")
                st.write("*Head Coach: John Tortorella*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly flyers forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly flyers defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly flyers goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly flyers ir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly flyers ltir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly flyers dead cap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly flyers dead cap retained`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly flyers buried penalty`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly flyers non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly flyers non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly flyers non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Pittsburgh Penguins":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Penguins_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Kyle Dubas*")
                st.write("*Head Coach: Mike Sullivan*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly penguins forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly penguins defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly penguins goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly penguins ir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly penguins ltir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly penguins dead cap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly penguins dead cap retained`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly penguins non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly penguins non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly penguins non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Washington Capitals":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Caps_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Brian MacLellan*")
                st.write("*Head Coach: Spencer Carbery*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly capitals forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly capitals defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly capitals goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly capitals ltir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly capitals dead cap retained`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly capitals non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly capitals non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly capitals non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Boston Bruins":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Bruins_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Don Sweeney*")
                st.write("*Head Coach: Jim Montgomery*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly bruins forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly bruins defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly bruins goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly bruins ir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly bruins dead cap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly bruins non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly bruins non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly bruins non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Buffalo Sabres":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Sabres_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Kevyn Adams*")
                st.write("*Head Coach: Lindy Ruff*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly sabres forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly sabres defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly sabres goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly sabres ir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly sabres dead cap Buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly sabres non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly sabres non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly sabres non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Detroit Red Wings":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(RedWings_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Steve Yzerman*")
                st.write("*Head Coach: Derek Lalonde*") 
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly red wings forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly red wings defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly red wings goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly red wings dead cap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly red wings non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly red wings non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly red wings non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Florida Panthers":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Panthers_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Bill Zito*")
                st.write("*Head Coach: Paul Maurice*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly panthers forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly panthers defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly panthers goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly panthers dead cap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly panthers non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly panthers non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly panthers non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Montreal Canadiens":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Canadiens_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Kent Hughes*")
                st.write("*Head Coach: Martin St. Louis*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canadiens forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canadiens defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canadiens goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canadiens ir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canadiens ltir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canadiens dead cap retained`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canadiens non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canadiens non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly canadiens non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Ottawa Senators":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Senators_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Steve Staios*")
                st.write("*Head Coach: Travis Green*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly senators forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly senators defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly senators goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly senators ir`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly senators dead cap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly senators dead cap retained`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly senators non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly senators non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly senators non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Tampa Bay Lightning":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(Lightning_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Julien BriseBois*")
                st.write("*Head Coach: Jon Cooper*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly lightning forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly lightning defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly lightning goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly lightning dead cap buyout`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly lightning non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly lightning non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly lightning non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
    if selected == "Toronto Maple Leafs":
        with st.container():
            blank_col1, main_col= st.columns((0.45,0.55))
            with main_col:
                st.image(MapleLeafs_logo)
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((1.25,1.35,0.4))
            with main_col:
                st.write("*General Manager: Brad Treliving*")
                st.write("*Head Coach: Craig Berube*")
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                st.divider()
        with st.container():
            blank_col1, main_col, blankcol3= st.columns((0.5,2,0.5))
            with main_col:
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly maple leafs forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly maple leafs defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly maple leafs goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly maple leafs non-roster forwards`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.subheader("Non-Roster")
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly maple leafs non-roster defense`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
                 if conn:
                           try:
                               query = "SELECT * FROM `cap friendly maple leafs non-roster goalies`"  # Replace 'yourtable' with your actual table name
                               df = pd.read_sql(query, conn)
                               df= df.reset_index(drop=True)
                               st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
                           except pymysql.MySQLError as e:
                               st.error(f"Error executing query: {e}")
                        #    finally:
                        #        conn.close()
        

#st.markdown("*Copyright © 2023 St. Louis Blues*")

