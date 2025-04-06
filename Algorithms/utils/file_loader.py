import pickle
from pathlib import Path

def load_or_initialize_item_dict(filepath):
    filepath = Path(filepath)
    if not filepath.exists() or filepath.stat().st_size == 0:
        item_dict = {}
        with open(filepath, "wb") as file:
            pickle.dump(item_dict, file)
        #print(f"[INFO] Created new file at: {filepath}")
    else:
        with open(filepath, "rb") as file:
            try:
                item_dict = pickle.load(file)
                #print(f"[INFO] Loaded item data from: {filepath}")
            except EOFError:
                #print(f"[WARN] File corrupted or empty. Resetting: {filepath}")
                item_dict = {}
                with open(filepath, "wb") as f:
                    pickle.dump(item_dict, f)
    return item_dict

def load_or_initialize_container_dict(filepath):
    filepath = Path(filepath)
    if not filepath.exists() or filepath.stat().st_size == 0:
        container_dict = {}
        with open(filepath, "wb") as file:
            pickle.dump(container_dict, file)
        #print(f"[INFO] Created new container file at: {filepath}")
    else:
        with open(filepath, "rb") as file:
            try:
                container_dict = pickle.load(file)
                #print(f"[INFO] Loaded container data from: {filepath}")
            except EOFError:
                #print(f"[WARN] Container file corrupted or empty. Resetting: {filepath}")
                container_dict = {}
                with open(filepath, "wb") as f:
                    pickle.dump(container_dict, f)
    return container_dict

def load_or_initialize_waste_dict(filepath):
    filepath = Path(filepath)
    if not filepath.exists() or filepath.stat().st_size == 0:
        waste_dict = {}
        with open(filepath, "wb") as file:
            pickle.dump(waste_dict, file)
        #print(f"[INFO] Created new container file at: {filepath}")
    else:
        with open(filepath, "rb") as file:
            try:
                waste_dict = pickle.load(file)
                #print(f"[INFO] Loaded container data from: {filepath}")
            except EOFError:
                #print(f"[WARN] Container file corrupted or empty. Resetting: {filepath}")
                waste_dict = {}
                with open(filepath, "wb") as f:
                    pickle.dump(waste_dict, f)
    return waste_dict

def load_or_initialize_log_file(filepath):
    filepath = Path(filepath)
    if not filepath.exists() or filepath.stat().st_size == 0:
        logging_dict = {}
        with open(filepath, "wb") as file:
            pickle.dump(logging_dict, file)
        #print(f"[INFO] Created new container file at: {filepath}")
    else:
        with open(filepath, "rb") as file:
            try:
                logging_dict = pickle.load(file)
                #print(f"[INFO] Loaded container data from: {filepath}")
            except EOFError:
                #print(f"[WARN] Container file corrupted or empty. Resetting: {filepath}")
                logging_dict = {}
                with open(filepath, "wb") as f:
                    pickle.dump(logging_dict, f)
    return logging_dict

def save_dict_to_file(data, filepath):
    filepath = Path(filepath)
    with open(filepath, "wb") as file:
        pickle.dump(data, file)
    #print(f"[INFO] Saved data to: {filepath}")

#item_dict = load_or_initialize_item_dict(ITEM_DATA_PATH)
#container_dict = load_or_initialize_container_dict(CONTAINER_DATA_PATH)

#save_dict_to_file(item_dict, ITEM_DATA_PATH)
#save_dict_to_file(container_dict, CONTAINER_DATA_PATH)