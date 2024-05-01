import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page1_project_summary import page1_project_summary
from app_pages.page2_data_visualization import page2_data_visualization

app = MultiPage(app_name="Cherry Leaves Mildew Study")

app.add_page('Project Summary', page1_project_summary)
app.add_page('Data Visualization', page2_data_visualization)

app.run()