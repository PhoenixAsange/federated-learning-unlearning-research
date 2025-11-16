# Simple package test
print("Testing packages...")

try:
    import numpy as np
    print(f"OK - NumPy {np.__version__}")
except ImportError:
    print("FAIL - NumPy")

try:
    import pandas as pd
    print(f"OK - Pandas {pd.__version__}")
except ImportError:
    print("FAIL - Pandas")

try:
    import matplotlib.pyplot as plt
    print("OK - Matplotlib")
except ImportError:
    print("FAIL - Matplotlib")

try:
    import torch
    print(f"OK - PyTorch {torch.__version__}")
except ImportError:
    print("FAIL - PyTorch")

try:
    import torchvision
    print(f"OK - TorchVision {torchvision.__version__}")
except ImportError:
    print("FAIL - TorchVision")

try:
    import notebook
    print("OK - Jupyter")
except ImportError:
    print("FAIL - Jupyter")

print("Test completed.")