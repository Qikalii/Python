import os
import numpy as np

base_folder = "F:\AppData\Git\Repository\Python\Data\-0.2-0"

for i in np.arange(-2, 0.04, 0.04):

    folder_name = str(f"{i:.2f}")
    os.makedirs(folder_name, exist_ok=True)
