import os
import numpy as np  # FIX: Import np correctamente
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import torch  # FIX: Añadir import de torch

# FIX: Importaciones con rutas absolutas
from src.Data.loader import load_and_prepare
from src.quantum.embedding import expand_to_angles
from src.quantum.expectations import expectations_for_angles, batch_quantum_computations
from src.ml.features import build_feature_matrix
from src.ml.models import train_rf, train_torch
from src.viz.plots import basic_boxplot

# O alternativa con rutas relativas:
# from ..data.loader import load_and_prepare
# from ..quantum.embedding import expand_to_angles
# from ..quantum.expectations import expectations_for_angles, batch_quantum_computations
# from .features import build_feature_matrix
# from .models import train_rf, train_torch
# from ..viz.plots import basic_boxplot