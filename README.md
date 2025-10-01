# Reto VLM3D - UNALMED

**Materia:** Tópicos de Geometría y Visualización Médica  
**Participantes:**  
- Jerónimo Hoyos Botero  
- Andrés Esteban Montoya Suárez  
- Jose Miguel García Vélez
---

## Introducción

Este repositorio corresponde al trabajo realizado en el marco de la materia **Tópicos de Geometría y Visualización Médica** de la Universidad Nacional de Colombia (sede Medellín).  

El **Reto VLM3D** busca impulsar el desarrollo de modelos de inteligencia artificial para la **interpretación de imágenes médicas en 3D**, con un enfoque especial en tomografías computarizadas de tórax (**CT**).  

El reto se fundamenta en el **conjunto de datos abierto CT-RATE**, que reúne más de **50,000 volúmenes 3D** acompañados de reportes radiológicos y anotaciones de **18 anomalías clínicas relevantes**. Este recurso proporciona una base sólida para explorar tareas como:

- Generación automática de reportes radiológicos.  
- Clasificación de anomalías en CT.  
- Localización auto-supervisada de hallazgos clínicos.  
- Generación de volúmenes 3D condicionada por texto.  

---
## Estructura del Proyecto

```
Reto-VLM3D-UNALMED/
├── datos/                     # Carpeta para scripts de acceso a datos
│   └── README.md              # Instrucciones para obtener el dataset desde Hugging Face / Zenodo
│
├── src/                       # Código fuente del proyecto
│
├── notebooks/                 # Jupyter notebooks de experimentación
│   └── enfermedades.ipynb
|   ├── otros_labels.ipynb
│
├── .gitignore                 
├── LICENSE                    # Licencia MIT del código
└── README.md                  # Documentación principal del proyecto

```

## Instalación y Configuración  

### Requisitos
- Python 3.10+  
- Carpeta datos/ subidos según el README.md mostrado en la misma
### Pasos para la instalación
```bash
# Clonar repositorio
git clone https://github.com/JeroHoyos/Reto-VLM3D-UNALMED

# Entrar al directorio del notebooks
cd Reto-VLM3D-UNALMED/notebooks

# Crear entorno virtual (Python)
py -m venv .venv
source venv/bin/activate  # Linux/Mac
.venv\Scripts\activate    # Windows

# Instalar dependencias
pip install -r requirements.txt

#Para desactivar entorno
deactivate
```

## Recursos

- [Información oficial del reto (Zenodo)](https://zenodo.org/records/15052708)  
- [Dataset CT-RATE en Hugging Face](https://huggingface.co/datasets/ibrahimhamamci/CT-RATE)  
- [Implementación base en GitHub (CT-CLIP)](https://github.com/ibrahimethemhamamci/CT-CLIP)  

---

## Citación

Si utilizas CT-RATE, CT-CLIP o las tareas del reto en tu investigación, por favor cita las siguientes publicaciones:

1. Hamamci, I. E., Er, S., Almas, F., Simsek, A. G., Esirgun, S. N., Dogan, I., Dasdelen, M. F., Durugol, O. F., Wittmann, B., Amiranashvili, T., Simsar, E., Simsar, M., Erdemir, E. B., Alanbay, A., Sekuboyina, A., Lafci, B., Bluethgen, C., Ozdemir, M. K., & Menze, B. (2024).  
   *Developing Generalist Foundation Models from a Multimodal Dataset for 3D Computed Tomography*.  
   [arXiv:2403.17834](https://arxiv.org/abs/2403.17834).  

2. Hamamci, I. E., Er, S., Sekuboyina, A., Simsar, E., Tezcan, A., Simsek, A. G., Esirgun, S. N., Almas, F., Dogan, I., Dasdelen, M. F., et al. (2024).  
   *GenerateCT: Text-conditional generation of 3D chest CT volumes*.  
   In *European Conference on Computer Vision* (pp. 126–143). Springer.  

3. Hamamci, I. E., Er, S., & Menze, B. (2024).  
   *CT2Rep: Automated radiology report generation for 3D medical imaging*.  
   In *International Conference on Medical Image Computing and Computer-Assisted Intervention* (pp. 476–486). Springer.  

---

## Licencia

El **código** de este repositorio se distribuye bajo la licencia **MIT**.  

```text
MIT License

Copyright (c) 2025 Jerónimo Hoyos Botero & Andrés Esteban Montoya Suárez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
