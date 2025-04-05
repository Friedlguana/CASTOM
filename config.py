from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ITEM_DATA_PATH = (BASE_DIR / "Algorithms/data/item_data.bin").resolve()
CONTAINER_DATA_PATH = (BASE_DIR / "Algorithms/data/container_data.bin").resolve()
WASTE_DATA_PATH = (BASE_DIR / "Algorithms/data/waste_data.bin").resolve()