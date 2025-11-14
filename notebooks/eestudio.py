import pandas as pd

# === CONFIGURAR EL ARCHIVO A LEER ===
df = pd.read_csv("seleccion_final.csv")

print("\n===== INFORMACIÓN GENERAL =====\n")
print(f"Total de estudios seleccionados: {len(df)}")

# Etiqueta (asumimos columna 'label' donde 1 = nódulo, 0 = no nódulo)
if "Lung nodule" in df.columns:
    print("\n--- Distribución de etiquetas (positivos/negativos) ---")
    print(df["Lung nodule"].value_counts().rename(index={0:"Negativos", 1:"Positivos"}))
else:
    print("\n[ADVERTENCIA] No se encontró la columna 'label'.\n")

# Género (columna PatientSex)
if "PatientSex" in df.columns:
    print("\n--- Distribución por sexo ---")
    print(df["PatientSex"].value_counts())
else:
    print("\n[ADVERTENCIA] No se encontró la columna 'PatientSex'.\n")

# Grupo de edad (columna AgeGroup)
if "AgeGroup" in df.columns:
    print("\n--- Distribución por grupos de edad ---")
    print(df["AgeGroup"].value_counts().sort_index())
else:
    print("\n[ADVERTENCIA] No se encontró la columna 'AgeGroup'.\n")

# Grupo de grosor de corte (columna SliceGroup)
if "SliceGroup" in df.columns:
    print("\n--- Distribución por grupos de grosor de corte (SliceGroup) ---")
    print(df["SliceGroup"].value_counts().sort_index())
else:
    print("\n[ADVERTENCIA] No se encontró la columna 'SliceGroup'.\n")

# Distribución cruzada: Edad vs Sexo
if "AgeGroup" in df.columns and "PatientSex" in df.columns:
    print("\n--- Tabla cruzada: Edad vs Sexo ---")
    print(pd.crosstab(df["AgeGroup"], df["PatientSex"]))

# Distribución cruzada: Etiqueta vs SliceGroup
if "label" in df.columns and "SliceGroup" in df.columns:
    print("\n--- Tabla cruzada: Positivos/Negativos vs SliceGroup ---")
    print(pd.crosstab(df["label"], df["SliceGroup"]).rename(index={0:"Neg",1:"Pos"}))

# Distribución combinada completa (estratos)
print("\n--- Distribución combinada de estratos ---")
if all(col in df.columns for col in ["label", "PatientSex", "AgeGroup", "SliceGroup"]):
    print(df.groupby(["label", "PatientSex", "AgeGroup", "SliceGroup"]).size())
else:
    print("[ADVERTENCIA] Una o más columnas de estratos no están disponibles.")

print("\n===== FIN DEL REPORTE =====\n")
