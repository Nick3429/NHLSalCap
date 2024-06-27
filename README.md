# NHLSalCap
Created to upload my first streamlit app which accesses the individual NHL player salary cap information and present it on a streamlit web app.

The Streamlit app will contain 7 pages: A home page, an active players page, a cost per point page, a cost per save page, a trades page, a retained salary page, and a teams page. The idea is to have the most important aspects of the now taken down CapFriendly website inclued in this streamlit web app.

At my current state, I have scraped all of the information off CapFriendly and put it into a variety of different csv files which will then be added to the MySQL database eventually. Even though the data has been collected, I need to clean and format it as it is somewhat disorganized. I am going to scrape all the information and get into csv files before putting it into database to make sure I can get as much information off cap friendly as possible.

Current step, clean the csv files and get them into the MySQL Database. That way once the database it fully set up, I just have to sent it to the streamlit frontend to get presented.
