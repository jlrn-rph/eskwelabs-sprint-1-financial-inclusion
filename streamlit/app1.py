# import matplotlib.pyplot as plt
# import pandas as pd
# import plotly.express as px
import streamlit as st


def gender_gap_ph():
    # Write the title
    st.title(
        "The Philippines has the highest gender gap in Southeast Asia (SEA)"
    )

    # Partition the page into 2
    col1, col2, col3 = st.columns(3)

    col1.metric(
        label='% of Filipino men with accounts',
        value='60%'
    )
    col3.metric(
        label='% of Filipino women with accounts',
        value='67%'
    )

    # Display text
    st.markdown("Historically, there has always been a prominent gap between men and women according to the Alliance for Financial Inclusion (2017).")
    st.markdown("In terms of financial inclusion, the SEA gender gap is as follows:")

    # Add photo
    st.image("sea-gender-gap.png")



def research_objectives():
    # Write the title
    st.title(
        "Research Objectives"
    )

    st.markdown("Now that we have established that there is indeed a gender gap, our research objectives are as follows:")

    # Add photo
    st.image("research-objective.png")

def documentation():
    # Write the title
    st.title(
        "Documentation: An Obstacle For Women"
    )

    st.markdown("The top two reasons for not having an account "
                " are the same for both genders which are: (1) lack of funds and (2) too expensive."
                " What is specific to women, however, is the lack of documentation, which hinders them from opening an account.")

    # Add graph
    st.image("doc.png")


    st.markdown("\n"
                "Upon examining further, it was observed that 4 out 10 Filipino women lack the required documentation for opening accounts. "
                "Why is this so? And why this is documented more on women compared to men?"
                )

    # Add photo
    st.image("4outof10.png")

    st.markdown("""
                \n
                It may be perceived  that stay-at-home women don't need IDs.
                In addition, women who work in informal sectors such as cash-based small businesses like sari-sari stores,
                carinderia, palengke, among others, may not have the need to apply for IDs due to several requirements. 
                """
                )
    st.markdown("""
                \n
                Lastly, it may also be assumed that men have gendered expectations to do formal work, 
                and thus, the need for a bank account for payroll. 
                """
                )

def EDA():

    # Write the title
    st.title(
        "Exploring Age, Income and Education"
    )

    st.markdown("""
                Through exploratory data analysis, we have determined that three variables, **age, educational attainment,**
                 and **household income group** may explain why gender gap exists.
                """
                )

    # Age EDA
    st.subheader(
        """
        Gender Gap Highest Among Filipino Adults
        """
    )

    st.markdown("""
                 As observed from the graph, there is an apparent gender gap among Filipino adults,
                 with a 9.57 percentage point difference.
                 Such may be attributed to the general labor market participation of adult women. 
                 Usually, women are constrained by time-consuming domestic and care responsibilities. 
                 They also usually take up the role of a housewife which gives them a secondary role to economic activities. 
                 """
                )

    # Partition the page into 2
    col1, col2, col3 = st.columns(3)

    col1.metric(
        label='% of male adults with accounts',
        value='73%'
    )
    col3.metric(
        label='% of female adults with accounts',
        value='64%'
    )

    # Add graph
    st.image("age-EDA.png")


    # Education EDA

    st.subheader(
        """
        Gender Gap Highest Among Filipinos Who Attained Secondary Education
        """
    )

    st.markdown("""
                    Gender gap is highest among those who attained secondary education, with a percentage point difference of 8.49. 
                    Women who attained secondary education may tend to work in the informal sectors, 
                    work that usually do not require formal documentations. We can tie this up to their obstacle of 
                    lack of documentation to create an account, 
                    as mentioned in the previous section. 
                     """
                )

    # Partition the page into 2
    col1, col2, col3 = st.columns(3)

    col1.metric(
        label='% of male with accounts',
        value='61%'
    )
    col3.metric(
        label='% of female with accounts',
        value='53%'
    )

    # Add graph
    st.image("educ-EDA.png")


    # Income EDA

    st.subheader(
        """
        Gender Gap Highest Among Middle-Income and Poorest
        """
    )

    st.markdown("""
                The gender gap is highest among middle class to the poorest.
                Among the upper middle class and the richest, however, the gender gap is minimal. 

                """
                )

    st.markdown("""
                Usually, upper middle and richest have the formal documentations to work 
                 and have the funds to open an account. Their financial states are generally stable, 
                 hence the gender gap in terms of financial inclusion may be minimal.
                 """
                )

    st.markdown("""
                Since poorer income households experience financially instability, they generally focus on survivability. 
                They don't have bank accounts due to the top three reasons mentioned earlier,
                 which are (1) lack of funds and (2) too expensive. 
                 """
                )

    # Partition the page into 2
    col1, col2, col3 = st.columns(3)

    col1.metric(
        label='% of poorest males with accounts',
        value='49%'
    )
    col3.metric(
        label='% of poorest females with accounts',
        value='35%'
    )

    # Add graph
    st.image("income-EDA.png")

def conclusion():
    # Write the title and the subheader
    st.title(
        "Summary and Conclusion"
    )

    # Conclusion 1
    st.subheader(
        """
        How financially included are women in the Philippines?
        """
    )

    st.markdown(
        """
        By using exploratory data analysis, it was observed that gender gap was high in terms of account ownership
        among:
        1. Filipino adults
        2. Filipinos whose highest educational attainment is secondary education
        3. Filipinos among the poor to middle class
        """
    )

    # Conclusion 2
    st.subheader(
        """
        What are the profiles of women who are not financially included?
        """
    )

    st.markdown(
        """
        Using K-modes clustering, it was observed that **2 out of 5 profiles** of women are underserved. These were
        women from the middle class who attained secondary education. One of the profiles was an adult while the other
        one was considered part of the youth age group (ages 15-30 years old).
        """
    )

    # Conclusion 3
    st.subheader(
        """
        What can we do to bridge the gap?
        """
    )

    st.markdown(
        """
        1. Promote fintech, especially mobile financial accounts, as they require minimal documentation compared to formal financial institutions.
        2. Mitigate risks associated with fintech through enhanced consumer protection, data privacy, among others
        3. Address the country's inadequate internet infrastructure and high cost of internet services.
        4. Requirements for formal banks must be eased up. Institutionalize alternative identification by government and banks.
        5. Targeted financial programs, promos, incentives for females from different socio-economic strata.
        6. Incentivize the fintech industry by investing in start-ups or new players.
        """
    )




list_of_pages = [
    "FI Gender Gap in the Philippines",
    "Research Objectives",
    "Documentation: An Obstacle For Women",
    "Exploratory Data Analysis",
    "Conclusion"
]

st.sidebar.title(':scroll: Main Pages')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "FI Gender Gap in the Philippines":
    gender_gap_ph()

elif selection == "Research Objectives":
    research_objectives()

elif selection == "Documentation: An Obstacle For Women":
    documentation()

elif selection == "Exploratory Data Analysis":
    EDA()

elif selection == "Conclusion":
    conclusion()

