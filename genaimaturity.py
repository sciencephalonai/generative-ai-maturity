import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.image('website_logo.png', width=400)

"""
SciEncephalon AI is a leader in AI innovation, offering cloud-agnostic, cutting-edge AI solutions. 
With a team of Ivy League graduates, we focus on ethical AI development and strategic partnerships. 
Our Generative AI Maturity Chart helps organizations assess their AI capabilities, guiding them 
from basic adoption to advanced integration. This tool enables companies to benchmark progress, 
allocate resources effectively, and drive continuous innovation in the rapidly evolving AI landscape.
https://www.linkedin.com/company/sciencephalon

"""
# st.markdown("[![Click me](website_logo.png)](https://www.sciencephalon.com)")
st.title("Generative AI Maturity")
st.subheader("Is Your Company on Track with Gen AI?")

# Define the survey questions and options
questions = {
    "Belief": ["AI is a toy, AI is all hype", "AI is a tool, AI helps me be more efficient", "AI is a system, AI is a shift in how we work"],
    "Policy on AI usage": ["Bans all versions and forms of generative AI", "Allows only a few AI tools but with a clear AI policy around it", "Multi-tiered AI tool usage approach"],
    "Tool Choice": ["No adoption of AI tools", "Selective adoption of proven AI tools", "Broad adoption of various AI tools"],
    "Internal Training": ["No AI-related training for employees", "AI training programs for select teams", "Extensive AI training programs available to all employees"],
    "Budget": ["Tests AI without clear costs or KPIs", "Allocates an experimental budget to AI", "Comprehensive budget across both tech and change management"],
    "Use Case Progress": ["No use cases in flight", "Limited to a few specific LOB use cases", "Sees AI as revenue opportunity"],
    "Privacy and Security": ["Lack dedicated privacy POC", "Has basic data policies", "Dedicated privacy team"],
    "Talent": ["No changes made in hiring or recruiting", "Hiring a few DS or MLEs", "Reallocated headcount across company for AI talent"]
}

# Initialize response dictionary
responses = {}

# Create two columns for the layout
col1, col2 = st.columns([4,3])

# Survey Form on the left column
with col1:
    st.header("Survey")
    with st.form("survey_form"):
        st.write("Please fill out the survey")
        for question, options in questions.items():
            response = st.radio(question, options)
            responses[question] = options.index(response) + 1  # Index + 1 to map to Behind (1), On Track (2), Ahead (3)
        submit = st.form_submit_button("Submit")


# To run the Streamlit app, save this code to a file (e.g., app.py) and run:
# streamlit run app.py

# Results and Visualization on the right column
with col2:
    if submit:
        st.header("Survey Results")
        st.write("Here is how your company's generative AI maturity looks:")

        # Create a DataFrame
        df = pd.DataFrame(list(responses.items()), columns=["Category", "Maturity Level"])
        df['Maturity Level'] = df['Maturity Level'].map({1: 'Behind', 2: 'On Track', 3: 'Ahead'})

        st.table(df)

        # Visualization
        maturity_counts = df['Maturity Level'].value_counts().reindex(['Behind', 'On Track', 'Ahead'], fill_value=0)
        
        # Optional: Detailed visualization using matplotlib with Viridis color palette
        fig, ax = plt.subplots()
        bars = ax.bar(maturity_counts.index, maturity_counts.values, color=sns.color_palette("viridis", len(maturity_counts)))
        ax.set_title("Generative AI Maturity Levels")
        ax.set_xlabel("Maturity Level", fontweight='bold')
        ax.set_ylabel("Count", fontweight='bold')
        ax.set_xticks(range(len(maturity_counts.index)))
        ax.set_xticklabels(maturity_counts.index, fontweight='bold')
        
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')  # Label each bar with its value
        
        st.pyplot(fig)
