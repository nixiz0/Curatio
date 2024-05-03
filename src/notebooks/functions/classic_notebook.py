import nbformat


def create_notebook(file_path):
    # Create a new empty notebook
    notebook = nbformat.v4.new_notebook()
    
    # Add a title cell
    title_cell = nbformat.v4.new_markdown_cell("# **Title Notebook**\nLorem ipsum ipsum ipsum ipsum")
    notebook.cells.append(title_cell)

    # Add Markdown text cell with table of contents
    toc_cell = nbformat.v4.new_markdown_cell("\
* [I. Lorem](#i-lorem)\n\
    - [A. Lorem](#a-lorem)\n\
        * [1- Lorem](#1-lorem)\n\
        * [2- Lorem](#2-lorem)\n\
        * [3- Lorem](#3-lorem)\n\
    - [B. Lorem](#b-lorem)\n\
        * [1- Lorem](#1-lorem)\n\
        * [2- Lorem](#2-lorem)\n\
        * [3- Lorem](#3-lorem)\n\
    - [C. Lorem](#c-lorem)\n\
        * [1- Lorem](#1-lorem)\n\
        * [2- Lorem](#2-lorem)\n\
        * [3- Lorem](#3-lorem)\n\
* [II. Lorem](#ii-lorem)\n\
    - [A. Lorem](#a-lorem)\n\
        * [1- Lorem](#1-lorem)\n\
        * [2- Lorem](#2-lorem)\n\
        * [3- Lorem](#3-lorem)\n\
    - [B. Lorem](#b-lorem)\n\
        * [1- Lorem](#1-lorem)\n\
        * [2- Lorem](#2-lorem)\n\
        * [3- Lorem](#3-lorem)\n\
    - [C. Lorem](#c-lorem)\n\
        * [1- Lorem](#1-lorem)\n\
        * [2- Lorem](#2-lorem)\n\
        * [3- Lorem](#3-lorem)\
    ")
    notebook.cells.append(toc_cell)

    # Add import cell with common libraries
    import_cells = [
        nbformat.v4.new_code_cell("\
import numpy as np\n\
import pandas as pd\n\
import matplotlib.pyplot as plt\n\
import seaborn as sns\n\
import warnings\n\
import re\n\
import tensorflow_hub as hub\n\
import tensorflow as tf\n\
import time\n\
import os\n\
import warnings\n\
import collections\n\
import string\n\
import scipy\n\
from sklearn.cluster import KMeans\n\
from sklearn.manifold import TSNE\n\
from sklearn.preprocessing import LabelEncoder\n\
from sklearn import cluster, metrics\n\
from sklearn.decomposition import PCA\n\
from sklearn import manifold, decomposition\n\
from sklearn.metrics import adjusted_rand_score, confusion_matrix\n\
from sklearn.metrics.cluster import adjusted_rand_score\n\
from sklearn.model_selection import train_test_split\n\
from tensorflow.keras.models import Model\n\
from tensorflow.keras.layers import Dense, Dropout, concatenate, Input\n\
from tensorflow.keras.preprocessing.image import load_img, img_to_array\n\
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint\n\
from scipy.optimize import linear_sum_assignment\
    "),
    ]
    notebook.cells.extend(import_cells)

    # Add a cell to display the version of the libraries used
    version_cell = nbformat.v4.new_code_cell("\
# Version of the libraries used\n\
print('\\n'.join(f'{m.__name__} - {m.__version__}' \n\
                for m in globals().values() \n\
                if getattr(m, '__version__', None)))\
    ")
    notebook.cells.append(version_cell)
    
    # Added a separator
    title_cell = nbformat.v4.new_markdown_cell("---\n")
    notebook.cells.append(title_cell)
    
    # Add cell to read CSV file
    read_csv_cell = nbformat.v4.new_code_cell("\
# Read CSV file\n\
df = pd.read_csv('your_dataset.csv')\
")
    notebook.cells.append(read_csv_cell)

    # Add a cell to display the first rows of the dataframe
    head_cell = nbformat.v4.new_code_cell("\
# Show first rows of dataframe\n\
df.head()\
")
    notebook.cells.append(head_cell)

    # Add a cell to display dataframe information
    info_cell = nbformat.v4.new_code_cell("\
# Show dataframe information\n\
df.info()\
")
    notebook.cells.append(info_cell)

    # Add a cell to display the first and last rows of the dataframe
    display_cell = nbformat.v4.new_code_cell("\
# Show first and last rows of dataframe\n\
display(df.head(3), df.tail(3))\
")
    notebook.cells.append(display_cell)

    # Add title I
    title_cell = nbformat.v4.new_markdown_cell("\
---\n\
<a id='i-lorem'></a>\n\
# **I. Lorem**\n\
Lorem ipsum ipsum ipsum.\
")
    notebook.cells.append(title_cell)

    # Added code cell
    version_cell = nbformat.v4.new_code_cell("")
    notebook.cells.append(version_cell)

    # Add Subcategories for I. Lorem
    subcategories_i = ['A', 'B', 'C']

    for subcategory in subcategories_i:
        title_cell = nbformat.v4.new_markdown_cell(f"\
---\n\
<a id='{subcategory.lower()}-lorem'></a>\n\
### **{subcategory}. Lorem**\n\
Lorem ipsum ipsum.\n\n\
<a id='1-lorem'></a>\n\
**1- Lorem**\
    ")
        notebook.cells.append(title_cell)

        # Added code cell
        version_cell = nbformat.v4.new_code_cell("")
        notebook.cells.append(version_cell)

        # Ajout de la sous-section 2
        title_cell = nbformat.v4.new_markdown_cell("\
<a id='2-lorem'></a>\n\
**2- Lorem**\
    ")
        notebook.cells.append(title_cell)

        # Added code cell
        version_cell = nbformat.v4.new_code_cell("")
        notebook.cells.append(version_cell)

        # Added subsection 3
        title_cell = nbformat.v4.new_markdown_cell("\
<a id='3-lorem'></a>\n\
**3- Lorem**\
    ")
        notebook.cells.append(title_cell)

        # Added code cell
        version_cell = nbformat.v4.new_code_cell("")
        notebook.cells.append(version_cell)

    # Add title II
    title_cell = nbformat.v4.new_markdown_cell("\
---\n\
<a id='ii-lorem'></a>\n\
# **II. Lorem**\n\
Lorem ipsum ipsum ipsum.\
")
    notebook.cells.append(title_cell)

    # Added code cell
    version_cell = nbformat.v4.new_code_cell("")
    notebook.cells.append(version_cell)

    # Add Subcategories for II. Lorem
    subcategories_ii = ['A', 'B', 'C']

    for subcategory in subcategories_ii:
        title_cell = nbformat.v4.new_markdown_cell(f"\
---\n\
<a id='{subcategory.lower()}-lorem'></a>\n\
### **{subcategory}. Lorem**\n\
Lorem ipsum ipsum.\n\n\
<a id='1-lorem'></a>\n\
**1- Lorem**\
    ")
        notebook.cells.append(title_cell)

        # Added code cell
        version_cell = nbformat.v4.new_code_cell("")
        notebook.cells.append(version_cell)

        # Added subsection 2
        title_cell = nbformat.v4.new_markdown_cell("\
<a id='2-lorem'></a>\n\
**2- Lorem**\
    ")
        notebook.cells.append(title_cell)

        # Added code cell
        version_cell = nbformat.v4.new_code_cell("")
        notebook.cells.append(version_cell)

        # Added subsection 3
        title_cell = nbformat.v4.new_markdown_cell("\
<a id='3-lorem'></a>\n\
**3- Lorem**\
    ")
        notebook.cells.append(title_cell)

        # Added code cell
        version_cell = nbformat.v4.new_code_cell("")
        notebook.cells.append(version_cell)
        
    # Added a separator
    title_cell = nbformat.v4.new_markdown_cell("---\n---")
    notebook.cells.append(title_cell)
    
    # Addition of the results title
    title_cell = nbformat.v4.new_markdown_cell("## **Results**\n")
    notebook.cells.append(title_cell)
    
    # Added markdown to explain the conclusion
    title_cell = nbformat.v4.new_markdown_cell("")
    notebook.cells.append(title_cell)

    # Save the notebook to a file
    with open(file_path, 'w') as f:
        nbformat.write(notebook, f)

    print(f"The notebook was successfully created at location: {file_path}")