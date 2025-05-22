import os
import json
import random

def create_train_val_split(data_dir, output_file, train_ratio=0.95):
    """
    Splits files in a directory into training and validation sets and saves the split to a JSON file.

    Args:
        data_dir (str): The directory containing the data files.
        output_file (str): The path to the output JSON file.
        train_ratio (float): The proportion of data to be used for training.
    """
    try:
        filenames = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]
    except FileNotFoundError:
        print(f"Error: Directory not found at {data_dir}")
        return
    except Exception as e:
        print(f"An error occurred while listing files: {e}")
        return

    if not filenames:
        print(f"No files found in {data_dir}")
        return

    # Extract UUIDs (filenames without the .py extension)
    uuids = [os.path.splitext(filename)[0] for filename in filenames]

    # Shuffle the UUIDs
    random.shuffle(uuids)

    # Calculate the split index
    split_index = int(len(uuids) * train_ratio)

    # Split the UUIDs
    train_uuids = uuids[:split_index]
    validation_uuids = uuids[split_index:]

    # Create the dictionary for the JSON output
    split_data = {
        "train": train_uuids,
        "validation": validation_uuids
    }

    # Write the JSON output file
    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w') as f:
            json.dump(split_data, f, indent=4)
        print(f"Successfully created train/validation split at {output_file}")
        print(f"Total files: {len(uuids)}")
        print(f"Training files: {len(train_uuids)}")
        print(f"Validation files: {len(validation_uuids)}")
    except IOError:
        print(f"Error: Could not write to output file {output_file}")
    except Exception as e:
        print(f"An unexpected error occurred while writing the JSON file: {e}")

if __name__ == '__main__':
    data_directory = "/home/user2/wns/cad-recode/dpo_data/ground_truth"
    output_json_file = "/home/user2/wns/cad-recode/dpo_data/train_val.json"
    
    create_train_val_split(data_directory, output_json_file)