from shiny import ui

def app_ui(request):
    return ui.page_fluid(
        ui.h2("Interactive Single-Cell UMAP Viewer"),
        ui.input_file("file_upload", "Upload ZIP File", multiple=False, accept=[".zip"]),
        ui.output_plot("umap_plot"),
        ui.output_text("error_message")
    )
