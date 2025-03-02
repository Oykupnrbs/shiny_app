**# Interactive Single Cell UMAP Viewer**

With this web application, you can visualize single-cell RNA-seq data stored in .h5ad format within a zip file.

**## Requirements**

**shiny** for creating the web application.

**scanpy** for loading .h5ad files and UMAP plotting.

**matplotlib** for generating visualizations.

**zipfile** for unzipping files.

**os** for handling file paths and directories.

Python 3.8 or higher.

*Install required packages using: 
      
      'pip install shiny scanpy matplotlib'
**## Why do you use this app?**

This application makes complex cell data more meaningful to you and presents you with a visual. With this app, you can see different types of cells and how they related to each other.

**## How can you use this app?**

**Run the App:** 

**Upload Your File:** When you open this app, you will see File Upload Button. You should upload a zipfile which contains .h5ad file.

**UMAP visualization:** After you upload the file, this app will unzip your file and process it. Finally, you will see UMAP map. Also, you can see that the file contains which cell groups.
