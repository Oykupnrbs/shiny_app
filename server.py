import os
from shiny import render
from utils import extract_zip, process_h5ad

def server(input, output, session):

    @output
    @render.text
    def error_message():
        if not input.file_upload():
            return "Error: Please upload a ZIP file!"

        file_info = input.file_upload()[0]
        zip_path = file_info["datapath"]

        h5ad_path, error = extract_zip(zip_path)
        if error:
            return error

        _, error = process_h5ad(h5ad_path)
        if error:
            return error

        return None

    @output
    @render.plot
    def umap_plot():
        if not input.file_upload():
            return None

        file_info = input.file_upload()[0]
        zip_path = file_info["datapath"]

        h5ad_path, error = extract_zip(zip_path)
        if error:
            return None

        plot, error = process_h5ad(h5ad_path)
        if error:
            return None

        return plot
