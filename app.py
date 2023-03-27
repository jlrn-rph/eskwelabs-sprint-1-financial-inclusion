import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st


def load_data():
    # Load the data
    data = pd.read_csv(
        "./data/ph_data.csv",
        encoding='ISO-8859-1'
    )
    return data


def introduction():
    # Define the title, research objectives, scope and limitations
    st.title(
        "Towards Financial Inclusion: Outreach & Usage"
    )
    st.subheader(
        """
        According to Debuque-Gonzales and Corpus (2021), the two basic dimensions of financial inclusion are Outreach and Usage. 

        Outreach refers to the supply-side data on the pervasiveness of formal financial accounts that include indicators on ownership of traditional financial accounts, fintech accounts, and credit cards. 

        Meanwhile, the usage dimension captures the extent of people’s usage of their respective accounts. 

        Key Objecttives
        
        1. What segment of the population has  formal financial access?
        2. For those without formal financial access, what are the reasons for not owning a bank account?
        """
    )

    # Load photo
    st.image("streamlit-photo-1.jpeg")

    # Load data
    data = load_data()

    # Display data
    st.markdown("**The Data**")
    st.dataframe(data)
    st.markdown("Source: Global Findex 2021 from World Bank.")

def viz_gender_gap():
     st.title(
        "Gender Gap in PH and SEA"
    )

def viz_without_bank_reasons():
     st.title(
        "Men vs Women Reasons Without Bank Account"
    )

def viz_gap_age():
     st.title(
        "Gender vs Age Groups"
    )

def viz_gap_education():
     st.title(
        "Gender vs Educational Attainment"
    )

def viz_gap_income():
    st.title(
        "Gender vs Income"
    )

# def data_visualization():
#     viz_gender_gap(),
#     viz_without_bank_reasons(),
#     viz_gap_age(),
#     viz_gap_education(),
#     viz_gap_income()
    

def clustering():
    st.title(
        "Clustering"
    )


def recommendations():
    # Write the title
    st.title(
        "What We Can Do"
    )


def the_team():
    # Feel free to write anything you want e.g what part you did in the project,
    # LinkedIn account, etc :D
    st.title(
        "The Team"
    )
    st.subheader("Ben Estera")
    st.subheader("Jox Latigar")
    st.subheader("Denise Montecastro")
    st.subheader("Justin Neypes")

list_of_pages = [
    "Introduction",
    # "Exploratory Data Analysis",
    "Gender Gap in PH and SEA",
    "Men vs Women Reasons Without Bank Account",
    "Gender vs Age Groups",
    "Gender vs Educational Attainment",
    "Gender vs Income",
    "Clustering",
    "Recommendations",
    "The Team"
]

st.sidebar.title(':scroll: Main Pages')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Introduction":
    introduction()

# elif selection == "Exploratory Data Analysis":
#     data_visualization()

elif selection == "Gender Gap in PH and SEA":
    viz_gender_gap()

elif selection == "Men vs Women Reasons Without Bank Account":
    viz_without_bank_reasons()

elif selection == "Gender vs Age Groups":
    viz_gap_age()   

elif selection == "Gender vs Educational Attainment":
    viz_gap_education() 

elif selection == "Gender vs Income":
    viz_gap_income() 

elif selection == "Clustering":
    clustering()

elif selection == "Recommendations":
    recommendations()

elif selection == "The Team":
    the_team()
