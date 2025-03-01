import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    plot_predictions_probabilities
                                                    )


def page3_predictor():
    st.info(
        f'* Detecting the presence or absence of disease in a leaf image'
    )

    st.write(
        f"* You can download a set of parasitised and uninfected cells for live prediction. "
        )

    st.write("---")

    images_buffer = st.file_uploader('Upload leaf image samples. You may select more than one.',
                                        type='png',accept_multiple_files=True)

    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f'Leaf image: **{image.name}**')
            img_array = np.array(img_pil)
            st.image(img_pil, caption=f'Image Size: {img_array.shape[1]}px width x {img_array.shape[0]} px height')
            version = 'v1'

            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(resized_img, version=version)

            df_report = df_report.append(
                {
                    "Name": image.name,
                    "Result": pred_class
                },
                ignore_index=True
            )
            if not df_report.empty:
                st.success("Analysis Report")
                st.table(df_report)
                st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)