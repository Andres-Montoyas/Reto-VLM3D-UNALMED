

import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import streamlit as st
import time


st.set_page_config(layout="wide", page_title="Visualizador NIfTI - Tomografía de Pecho")


@st.cache_data
def cargar_nifti(ruta_nifti: str):
    try:
        img = nib.load(ruta_nifti)
        data = img.get_fdata()
        return np.array(data, dtype=np.float32)
    except Exception as e:
        st.error(f"⚠️ Error al cargar el archivo NIfTI: {e}")
        return None


st.title("🩻 Visualizador de Tomografías de Pecho (NIfTI)")

archivo_nifti = st.file_uploader("📂 Sube un archivo NIfTI (.nii o .nii.gz)", type=["nii", "nii.gz"])

if archivo_nifti is not None:
    with open("temp_file.nii.gz", "wb") as f:
        f.write(archivo_nifti.getvalue())
    volumen = cargar_nifti("temp_file.nii.gz")

    if volumen is not None:
        st.success("✅ Tomografía cargada correctamente")

 
        col_img, col_ctrl = st.columns([2, 1])

        with col_ctrl:
            st.markdown("<h2 style='text-align:center;'>⚙️ Controles</h2>", unsafe_allow_html=True)


            corte = st.radio("🩻 Tipo de plano", ["Plano 1", "Plano 2", "Plano 3"])

            cortes_anatomicos = {
                "Plano 1": volumen,                      
                "Plano 2": volumen.transpose(1, 0, 2),   
                "Plano 3": volumen.transpose(2, 0, 1)    
            }
            vol = cortes_anatomicos[corte]


            modo_auto = st.checkbox("▶ Reproducción automática")

            if not modo_auto:
           
                index = st.slider(f"Corte en {corte}", 0, vol.shape[0] - 1, vol.shape[0] // 2)
            else:

                velocidad = st.slider("⏱ Velocidad (segundos por corte)", 0.05, 1.0, 0.2, step=0.05)

    
            grados_rotacion = st.slider("↪ Rotar imagen (grados)", 0, 270, 0, 90)
            k = grados_rotacion // 90

        with col_img:
            st.markdown("<div style='display:flex; justify-content:center;'>", unsafe_allow_html=True)

    
            img_placeholder = st.empty()

            if modo_auto:

                for i in range(vol.shape[0]):
                    fig, ax = plt.subplots(figsize=(3, 3))
                    slice_mostrar = np.rot90(vol[i], k=k)
                    ax.imshow(slice_mostrar, cmap="gray")
                    ax.axis("off")
                    img_placeholder.pyplot(fig, use_container_width=False)
                    plt.close(fig)
                    time.sleep(velocidad)
            else:

                fig, ax = plt.subplots(figsize=(3, 3))
                slice_mostrar = np.rot90(vol[index], k=k)
                ax.imshow(slice_mostrar, cmap="gray")
                ax.axis("off")
                img_placeholder.pyplot(fig, use_container_width=False)
                plt.close(fig)

            st.markdown("</div>", unsafe_allow_html=True)

else:
    st.info("📌 Por favor, sube un archivo NIfTI de tomografía de pecho para visualizarlo.")
