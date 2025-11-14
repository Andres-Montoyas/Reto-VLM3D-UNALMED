import shutil
import pandas as pd
from huggingface_hub import hf_hub_download
from tqdm import tqdm
import os

repo_id = 'ibrahimhamamci/CT-RATE'
hf_token = input("Ingresa tu token de Hugging Face: ")


train_csv = "train_names.csv"
val_csv = "val_names.csv"

val_csv = input("Ingresa el path del archivo csv de validación: ")
train_csv = input("Ingresa el path del archivo csv de entrenamiento: ")

df_train = pd.read_csv(train_csv)
df_val = pd.read_csv(val_csv)

def descargar(data, split_name):
    directory_name = f"dataset/{split_name}/"

    print(f"\nDescargando {len(data)} volúmenes para el split '{split_name}'...\n")

    for name in tqdm(data["VolumeName"]):
        parts = name.split("_")
        folder = f"{parts[0]}_{parts[1]}"
        subfolder = f"{folder}_{parts[2]}"
        full_subfolder = f"{directory_name}{folder}/{subfolder}"

        os.makedirs(f"data_volumes", exist_ok=True)

        try:
            hf_hub_download(
                repo_id=repo_id,
                repo_type='dataset',
                token=hf_token,
                subfolder=f"{folder}/{subfolder}",
                filename=name,
                cache_dir='./',
                local_dir=f"data_volumes/{split_name}",
                local_dir_use_symlinks=False,
                resume_download=True
            )
        except Exception as e:
            print(f"Error al descargar {name}: {e}")


descargar(df_train, "train")
descargar(df_val, "val")

print("\nDescarga completa.")
print("Los datos se guardaron en:")
print("  data_volumes/train/")
print("  data_volumes/val/\n")
