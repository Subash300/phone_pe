#Phonepe Pulse Data Visualization and Exploration:A User-Friendly Tool Using Streamlit and Plotly

DEMO VIDEO: https://youtu.be/6PLoHVPtcVs

ABOUT PHONEPE:
phonepe1

PhonePe is an Indian digital payments and financial services company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer .The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016.

The PhonePe app is available in 11 Indian languages. Using PhonePe, users can send and receive money, recharge mobile, DTH, data cards, make utility payments, pay at shops, invest in tax saving funds, liquid funds, buy insurance, mutual funds, and digital gold.

PhonePe is accepted as a payment option by over 3.5 crore offline and online merchant outlets, constituting 99% of pin codes in the country.

Phonepe Pulse:
phonepebeat

PhonePe Pulse is a feature offered by the Indian digital payments platform called PhonePe.

PhonePe Pulse provides users with insights and trends related to their digital transactions and usage patterns on the PhonePe app. It offers personalized analytics, including spending patterns, transaction history, and popular merchants among PhonePe users.

This feature aims to help users track their expenses, understand their financial behavior, and make informed decisions.

Phonepe Pulse Data Visualisation:
Data visualization refers to the graphical representation of data using charts, graphs, and other visual elements to facilitate understanding and analysis

These visualizations are designed to present information in a visually appealing and easily digestible format, enabling users to quickly grasp trends, patterns, and insights from their transaction history.

Problem Statement:
The Phonepe pulse Github repository contains a large amount of data related to various metrics and statistics.The goal is to extract this data and process it to obtain insights and information that can be visualized in a user-friendly manner.

Approach:
1. Data extraction:
Clone the Github using scripting to fetch the data from the Phonepe pulse Github repository and store it in a suitable format such as CSV or JSON.
2. Data transformation:
Use a scripting language such as Python, along with libraries such as Pandas, to manipulate and pre-process the data.
This may include cleaning the data, handling missing values, and transforming the data into a format suitable for analysis and visualization.
3. Database insertion:
Use the "mysql-connector-python" library in Python to connect to a MySQL database and insert the transformed data using SQL commands.
4. Dashboard creation:
Use the Streamlit and Plotly libraries in Python to create an interactive and visually appealing dashboard.
Plotly's built-in geo map functions can be used to display the data on a map and Streamlit can be used to create a user-friendly interface with multiple dropdown options for users to select different facts and figures to display.
5. Data retrieval:
Use the "mysql-connector-python" library to connect to the MySQL database and fetch the data into a Pandas dataframe.
Use the data in the dataframe to update the dashboard dynamically.
6. Deployment:
Ensuring the solution is secure, efficient, and user-friendly.
Testing the solution thoroughly and deploy the dashboard publicly, making it accessible to users.
Technologies:
Github Cloning
Python
Pandas
MySQL
mysql-connector-python
Streamlit
Plotly
Dashboard:
It contains information about Phonepe in the ABOUT page and details about the Phonepe pulse Data Visualisation in the HOME page
ANALYSIS:
It provides information based on all India , States and Top categories
Under these it provides analysis based on the Transaction and User data in each category.
Provides information based on the ** year and Quarter**
INSIGHTS:
From the analysis, basic insights were given in user friendly manner.
Also provided with the annual report



🧩 1️⃣ Decoding Transaction Dynamics on PhonePe
💡 SQL Query Tasks:

1.Total Transactions by State and Quarter
2.Top 5 States by Transaction Volume
Growth Rate of Transactions (Quarter over Quarter)
Average Transaction Value per Payment Category
States Showing Decline in Transactions

📱 2️⃣ Device Dominance and User Engagement Analysis
💡 SQL Query Tasks:
Total Registered Users by Device Brand
App Opens vs Registrations (Engagement Ratio)
Top 3 Devices by Active Engagement
Least Utilized Devices (High Users but Low Opens)
Device Usage by Region Trend


🛡️ 3️⃣ Insurance Penetration and Growth Potential
💡 SQL Query Tasks:

Total Insurance Transactions by State
Average Premium per Policy
Top 5 States with Highest Premium Collection
Quarterly Insurance Growth
Identify Underpenetrated States

🌍 4️⃣ Transaction Analysis for Market Expansion
💡 SQL Query Tasks:

Total Transaction Value by State
Average Transaction Value per User
Top 10 States by Growth Rate
Category-wise Transaction Trends
Low Performing States for Expansion Focus


👥 5️⃣ User Engagement and Growth Strategy
💡 SQL Query Tasks:

Total Registered Users by State
App Opens vs Registered Users (Engagement %)
Top 5 States with Highest Active Users
Districts Showing Highest Growth in Users
Inactive User States (Low Engagement)













