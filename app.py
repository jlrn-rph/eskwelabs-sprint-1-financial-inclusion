import pandas as pd
import streamlit as st

st.set_page_config(page_title='Bridging the Gender Gap Towards Financial Inclusion in the PH: A Data-Driven Approach')

#  Function that loads the data from a CSV file into a Pandas DataFrame
def load_data():
    data = pd.read_csv(
        "./data/ph_data.csv",
        encoding='ISO-8859-1'
    )
    return data

# Function that provides an overview of the project, including research objectives, scope, and limitations
# It also displays visualizations of key metrics and displays the dataset
def introduction():
    st.image("./assets/header.png")

    st.markdown(
        """
        Historically, according to the Alliance for Financial Inclusion (2017), there have always been a prominent gap between men and women.

        Upon checking the Southeast Asia region of the Global Findex 2021 data, we observed that the Philippines has the highest gender gap with a 7.7 percentage point difference.
        """
    )
    col1, col2, col3 = st.columns(3)

    col1.metric(
        label='% of Filipino men with accounts',
        value='60%'
    )
    col3.metric(
        label='% of Filipino women with accounts',
        value='67%'
    )

    st.image("./assets/sea-gender-gap.png")

    st.subheader("Research Objectives")
    st.image("./assets/objectives.png")

    st.subheader("Methodology")
    st.image("./assets/methodology.png")
    st.markdown(
        """
        To answer our research objectives, we utilized the 2021 Global Findex database with the sample size of 1000 for the Philippines. We wrangled the data using Python Pandas. We conducted feature engineering for us to better categorize our variables and to be able to perform exploratory data analysis. Lastly, we clustered our profiles using unsupervised machine learning, specifically K-Modes clustering.
        """
    )

    data = load_data()
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

# Function that explores the relationship between age, income, education, and financial inclusion 
# among genders in the Philippines. It provides visualizations of key findings and interprets the results
def viz_variables():
    st.title("Exploring Age, Income and Education")
    st.markdown(
        """
        Through exploratory data analysis, we have determined that three variables, **age, educational attainment,** and **household income group** may explain why gender gap exists.
        """
    )

    # Age EDA
    st.subheader("Gender Gap Highest Among Filipino Adults")
    col1, col2, col3 = st.columns(3)

    col1.metric(
        label='% of male adults with accounts',
        value='73%'
    )
    col3.metric(
        label='% of female adults with accounts',
        value='64%'
    )

    st.image("./assets/age-EDA.png")
    st.markdown(
        """
        As observed from the graph, there is an apparent gender gap among Filipino adults with a 9.57 percentage point difference. This may be attributed to the general labor market participation of adult women. Usually, women are constrained by time-consuming domestic and care responsibilities. They also usually take up the role of a housewife which gives them a secondary role to economic activities. 
        """
    )

    # Education EDA
    st.subheader("Gender Gap Highest Among Filipinos Who Attained Secondary Education")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        label='% of male with accounts',
        value='61%'
    )
    col3.metric(
        label='% of female with accounts',
        value='53%'
    )

    st.image("./assets/educ-EDA.png")
    st.markdown(
        """
        Gender gap is highest among those who attained secondary education with a percentage point difference of 8.49. Women who attained secondary education may tend to work in the informal sectors - work that usually do not require formal documentations. We can tie this up to their obstacle of lack of documentation to create an account. 
        """
    )

    # Income EDA
    st.subheader("Gender Gap Highest Among Middle-Income and Poorest")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        label='% of poorest males with accounts',
        value='49%'
    )
    col3.metric(
        label='% of poorest females with accounts',
        value='35%'
    )

    st.image("./assets/income-EDA.png")
    st.markdown(
        """
        The gender gap is highest among middle class to the poorest. However, among the upper middle class and the richest, the gender gap is minimal. 

        Usually, upper middle and richest have the formal documentations to work and have the funds to open an account. Their financial states are generally stable, hence the gender gap in terms of financial inclusion may be minimal.

        Since poorer income households experience financially instability, they generally focus on survivability. They don't have bank accounts due to the  lack of funds and that it's too expensive. 
        """
    )

# Function that explores the reasons why some Filipinos do not have a formal financial account
# It provides visualizations of key findings and interprets the results
def viz_without_bank_reasons():
    st.title("Documentation: An Obstacle For Women")   
    st.image("./assets/doc.png")
    st.markdown(
        """
        The top two reasons for not having an account are the same for both genders which are:
        1. Lack of funds
        2. Too expensive
        
        What is specific to women is the lack of documentation which hinders them from opening an account.
        """
    )

    st.markdown(
        """
        Upon examining further, it was observed that 4 out 10 Filipino women lack the required documentation for opening accounts. 
        
        **Why this is documented more on women compared to men?**
        """
    )
    st.image("./assets/4outof10.png")
    st.markdown(
        """
        It may be perceived  that stay-at-home women don't need IDs. In addition, women who work in informal sectors such as cash-based small businesses like sari-sari stores, carinderia, palengke, among others, may not have the need to apply for IDs due to several requirements. 

        Lastly, it may also be assumed that men have gendered expectations to do formal work, and thus, the need for a bank account for payroll. 
        """
    )

# Function to identify profiles of women who are underserved and not financially included
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

# Function to define the summary and conlusion
def conclusion():
    st.title("Summary and Conclusion")

    # Conclusion 1
    st.subheader("How financially included are women in the Philippines?")
    st.markdown(
        """
        By using exploratory data analysis, it was observed that gender gap was high in terms of account ownership among:
        1. Filipino adults
        2. Filipinos whose highest educational attainment is secondary education
        3. Filipinos among the poor to middle class
        """
    )

    # Conclusion 2
    st.subheader("What are the profiles of women who are not financially included?")
    st.markdown(
        """
        Using K-modes clustering, it was observed that **2 out of 5 profiles** of women are underserved. These were
        women from the middle class who attained secondary education. One of the profiles was an adult while the other
        one was considered part of the youth age group (ages 15-30 years old).
        """
    )

    # Conclusion 3
    st.subheader("What can we do to bridge the gap?")
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

    st.image('./assets/message.png')

# Meet the team
def the_team():
    st.title("The Team")
    st.markdown(
        """
        We are the team **4loop**! We are a group of individuals from diverse backgrounds who came together as part of the Eskwelabs Data Science Cohort 11. In our first sprint, we collaborated to create a data-driven presentation on financial inclusion entitled **Bridging the Gender Gap Towards Financial Inclusion in the PH: A Data-Driven Approach**. We visualized and analyzed the data for a research project aimed at explaining the gender gap in financial inclusion in the Philippines. The project uses data from the 2021 Global Findex database, which is wrangled and analyzed using Python Pandas, exploratory data analysis, and unsupervised machine learning.
        """
    )
    st.header("Members")
    st.subheader("[Ben Estera](https://www.linkedin.com/in/benestera/)")
    st.markdown(
        """
        * Perfomed clustering analysis using an unsupervised machine learning algorithm, K-Modes clusterting, to identify clusters of financially excluded women in the Philippines
        * Created compelling visualizations to illustrate age versus gender gaps in financial inclusion
        * Led the charge in analyzing and presenting results, ensuring that our findings were clearly and persuasively communicated to our audience
        """
    )

    st.subheader("[Jox Latigar](https://www.linkedin.com/in/jokkaz-latigar-7bbb07190/)")
    st.markdown(
        """
        * Conducted comprehensive research on financial inclusion documentation to develop a solid foundation for the project
        * Adopted a clear and effective framework to guide the presentation, ensuring that the key points were effectively communicated and understood by the audience
        * Created a visualization that highlighted the gender gap in income to draw attention to the issue of financial exclusion
        """
    )

    st.subheader("[Denise Montecastro](https://www.linkedin.com/in/denise-montecastro-573b34a2/)")
    st.markdown(
        """
        * Contributed to the development of the project's web application, specifically the visualizations, summary, and conclusion.
        * Created compelling visualizations comparing gender disparities in Southeast Asia and the Philippines
        * Led the creation and design of an engaging slide presentation to effectively communicate our findings
        """
    )
    st.subheader("[Justin Louise Neypes](https://www.linkedin.com/in/jlrnrph/)")
    st.markdown(
        """
        * Took charge of designing and deploying the Sprint 1 project on Streamlit, an open-source app framework for data scientists and machine learning engineers
        * Produced informative data visualizations showcasing the relationship between gender gap and educational attainment, as well as the factors that determine whether men and women have bank accounts or not
        * Crafted distinct personas to aid in clustering, which helped identify patterns and insights from the data, thus providing a better understanding of the target audience and their financial behavior
        """
    )

    st.subheader("Mentor: Ron Flores")

# Define the main menu
list_of_pages = [
    "Introduction",
    "Exploring Demographic Variables",
    "Documentation: An Obstacle for Women",
    "Clustering",
    "Conclusion",
    "The Team"
]

st.sidebar.title(':scroll: Main Menu')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Introduction":
    introduction()

elif selection == "Exploring Demographic Variables":
    viz_variables()

elif selection == "Documentation: An Obstacle for Women":
    viz_without_bank_reasons()

elif selection == "Clustering":
    clustering()

elif selection == "Conclusion":
    conclusion()

elif selection == "The Team":
    the_team()
