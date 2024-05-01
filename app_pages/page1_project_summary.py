import streamlit as st


def page1_project_summary():

    st.write('### Quick Project Summary')

    st.info(
        f'**General Information**  \n'
        f'The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.'
    )

    st.info(
        f'**Project Dataset**  \n'
        f'The available dataset contains 4208 labelled images of cherry leaves, divided evenly (2104 each) between healthy leaves and leaves affected by mildew.'
    )

    st.info(
        f'**Business Requirements**  \n'
        f'- The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.'
        f'- The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew'
    )
