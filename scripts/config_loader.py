import json

def load_config(file_path):
    """
    Load a JSON configuration file.
    
    :param file_path: Path to the JSON file.
    :return: Parsed JSON data as a dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found: {file_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON file: {file_path}. Error: {e}")
