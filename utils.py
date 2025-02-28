import os
import zipfile
import scanpy as sc
import matplotlib.pyplot as plt

def extract_zip(zip_path, extract_dir="extracted_files"):
    """ZIP dosyasını çıkarır ve içindeki .h5ad dosyasını döndürür."""
    os.makedirs(extract_dir, exist_ok=True)

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            if not zip_ref.namelist():
                return None, "ZIP file is empty. Please upload a valid ZIP file."
            zip_ref.extractall(extract_dir)
    except zipfile.BadZipFile:
        return None, "Invalid ZIP file. Please upload a valid .zip file."

    h5ad_files = [f for f in os.listdir(extract_dir) if f.endswith(".h5ad")]
    if not h5ad_files:
        return None, "No .h5ad file found in the ZIP."

    return os.path.join(extract_dir, h5ad_files[0]), None

def process_h5ad(h5ad_path):
    """H5AD dosyasını okur, PCA, UMAP ve Leiden işlemlerini yapar, ardından UMAP grafiğini çizer."""
    adata = sc.read_h5ad(h5ad_path)

    if "Cell type" not in adata.obs.columns:
        return None, "No 'Cell type' column found in the dataset."

    sc.pp.pca(adata)
    sc.pp.neighbors(adata, use_rep="X_pca")
    sc.tl.umap(adata)
    sc.tl.leiden(adata)

    plt.figure(figsize=(6, 4))
    sc.pl.umap(adata, color="Cell type", cmap="tab10", alpha=0.5, show=False)

    return plt.gcf(), None
