import os
import random
import itertools

import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.image import imread
import seaborn as sns
import numpy as np
import pandas as pd


def page2_data_visualization():

    st.write('### Data Visualization')
    st.info(
        f' The client is interested in how we can visually differentiate'
        f' between healthy cherry leaves and those affected by powdery'
        f' mildew'
    )

    version = 'v1'
    if st.checkbox('Difference between average and variability image'):
        avg_healthy = plt.imread(f'outputs/{version}/avg_var_healthy.png')
        avg_mildew = plt.imread(f'outputs/{version}/avg_var_powdery_mildew.png')

        st.success(
            f'* We notice the average and variability images show a noticeable'
            f' difference, which admits visual discrimination.'
        )

        st.image(avg_healthy, caption='Healthy leaf - average and variability')
        st.image(avg_mildew, caption="Diseased Leaf - average and variability")
        st.write('---')

    if st.checkbox('Difference between average healthy leaf and average diseased leaf'):
        diff_image = plt.imread(f'outputs/{version}/avg_diff.png')
        st.warning(
            f'* We notice that the study didn\'t show patterns that we'
            f' count intuitively differentiate from one another'
        )
        st.image(diff_image, caption="Difference between average images")

    if st.checkbox('Image Montage'):
        my_data_dir = 'inputs/cherry-leaves-dataset/cherry-leaves'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(label="Select label", options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(dir_path=my_data_dir + '/validation',
                          label_to_display=label_to_display,
                          nrows=5, ncols=3, figsize=(10, 25))
            st.write('---')

def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
  sns.set_style("white")
  labels = os.listdir(dir_path)

  # subset the class you are interested to display
  if label_to_display in labels:

    # checks if your montage space is greater than subset size
    # how many images in that folder
    images_list = os.listdir(dir_path+'/'+ label_to_display)
    if nrows * ncols < len(images_list):
      img_idx = random.sample(images_list, nrows * ncols)
    else:
      print(
          f"Decrease nrows or ncols to create your montage. \n"
          f"There are {len(images_list)} in your subset. "
          f"You requested a montage with {nrows * ncols} spaces")
      return
    

    # create list of axes indices based on nrows and ncols
    list_rows= range(0,nrows)
    list_cols= range(0,ncols)
    plot_idx = list(itertools.product(list_rows,list_cols))


    # create a Figure and display images
    fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
    for x in range(0,nrows*ncols):
      img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
      img_shape = img.shape
      axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
      axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
      axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
      axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
    plt.tight_layout()
    
    st.pyplot(fig=fig)
    # plt.show()