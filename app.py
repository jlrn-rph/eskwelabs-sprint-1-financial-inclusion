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

    # Load photo
    st.image("./assets/header.png")

    st.markdown(
        """
        Historically, according to the Alliance for Financial Inclusion (2017), there have always been a prominent gap between men and women.

        Upon checking the Southeast Asia region of the Global Findex 2021 data, we observed that the Philippines has the highest gender gap with a 7.7 percentage point difference.
        """
    )

    st.subheader("Research Objectives")
    st.image("./assets/objectives.png")

    st.subheader("Methodology")
    st.image("./assets/methodology.png")
    st.markdown(
        """
        To answer our research objectives, we utilized the 2021 Global Findex database with the sample size of 1000 for the Philippines. We wrangled the data using Python Pandas. We conducted feature engineering for us to better categorize our variables and to be able to perform exploratory data analysis. Lastly, we clustered our profiles using unsupervised machine learning, specifically K-Modes clustering.
        """
    )

    # Load data
    data = load_data()

    # Display data
    st.markdown("**Philippine Data**")
    with st.expander("View Data"):
        st.dataframe(data)
        st.caption("*Source: Global Findex 2021 from World Bank*")

    st.subheader("Scope and Limitations")
    st.image("./assets/scope.png")
    
    st.markdown(
        """
        According to a study by Debuque-Gonzales and Corpus, formal financial accounts include indicators on ownership of traditional financial accounts, fintech accounts, and credit cards. But to further simplify our analysis, we limited the definition to Filipinos who own either an account at a financial institution or a mobile account.
        """
    )

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
    st.title("Clustering")
    st.subheader("Who are the underserved amongst the  Filipino women?")
    st.image("./assets/underserved.png")
    st.markdown(
        """
        We used have multiple demographic variables to make sense of the groups of females and the patterns of their financial inclusion to understand who is underserved amongst Filipino women. We utilized an unsupervised machine learning algorithm, K-Modes clustering, to cluster categorical variables.
        """
    )
    st.image("./assets/clusters.png")
    st.markdown(
        """
        After using the K-Modes clustering and utilizing the elbow method, we have identified 5 clusters of FIlipino women.

        To provide a more in-depth description of the clusters, we've divided them into three:
        
        1. Those who have both bank and mobile accounts 
        2. Those who have bank accounts but no mobile accounts
        3. Those who don't have both mobile and bank accounts
        """
    )

    # Cluster 1
    st.subheader("Cluster 1: Both have bank and mobile accounts")
    st.image("./assets/clusters-1.png")
    st.markdown(
        """
        Sunshine Reyes, a 29-year-old marketing manager who belongs to the richest 20%, completed tertiary education, has a bank account and a mobile account, is highly proficient with technology, is financially literate, has a diversified investment portfolio, and aims to achieve financial independence and build wealth.
        """
    )

    # Clusters 2 & 3
    st.subheader("Cluster 2 and 3: Both have bank accounts but no mobile accounts")
    st.image("./assets/clusters-2-3.png")
    st.markdown(
        """
        Daphne Rodriguez, a 45-year-old lawyer who belongs to the richest 20%, completed tertiary education, has a bank account, owns a smartphone but prefers to conduct financial transactions in person or through her bank account, is financially literate, has invested in various financial products, and wants to diversify her portfolio.

        Joan Santos, a 22-year-old freelance graphic designer who belongs to the second richest 20%, completed secondary education, has a bank account, owns a smartphone but does not have a mobile account, is financially responsible, and is interested in exploring more affordable financial services and products.

        ***Policy Recommendations***

        Seeing that both of them have a bank account at a financial institution, we recommend policies to encourage them to use a mobile bank account:
        
        1. **To provide incentives to encourage the use of mobile banking**, such as waiving transaction fees or offering cash-back rewards. This will encourage more people to use mobile banking and help shift them away from cash-based transactions.

        2. **To simplify the mobile banking registration process and making it more accessible to users.** They can create a user-friendly registration process that requires minimal documentation and can be done easily through mobile devices.
        """
    )

    # Clusters 4 & 5
    st.subheader("Cluster 4 and 5: Don't have both mobile and bank accounts")
    st.image("./assets/clusters-4-5.png")
    st.markdown(
        """
        Glyza Garcia is a 45-year-old sari-sari store owner with a completed secondary education, belonging to the middle 20% income bracket. She does not have a bank or mobile account, relies on cash savings, and is interested in learning more about financial management to improve her business and family's well-being.

        Alyssa Dela Cruz is an 18-year-old student who has completed her secondary education and currently pursuing a degree in Education, with limited financial resources and no bank or mobile account. 

        ***Policy Recommendations***

        Seeing that both of them don't have a bank account at a financial institution or mobile bank account, we recommend the following: 
        
        1. **Provide Financial Literacy Education Programs** in the school curriculum for the students and community-based programs for the adults to help them better understand financial concepts, manage their finances effectively, and make informed decisions about financial products and services. 

        2. **Youth-friendly financial services** with low to no fees, special promotions, and reward programs for students to encourage them to start saving early and help them develop good financial habits.

        3. **Entrepreneurship Education and Training** for the adults to provide accessible and affordable upskilling programs specifically for blue-collar workers which can lead to better financial decisions and more successful businesses.
        """
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
    st.subheader("Justin Louise Neypes")
    st.caption("*[LinkedIn](https://www.linkedin.com/in/jlrnrph/)*")
    st.markdown(
        """
        * Took charge of designing and deploying the Sprint 1 project on Streamlit, an open-source app framework for data scientists and machine learning engineers.
        * Produced informative data visualizations showcasing the relationship between gender gap and educational attainment, as well as the factors that determine whether men and women have bank accounts or not.
        * Crafted distinct personas to aid in clustering, which helped identify patterns and insights from the data, thus providing a better understanding of the target audience and their financial behavior.
        """
    )

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
