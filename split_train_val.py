import json
import random

data_dir = "databricks-dolly-15k"
input_file = f"{data_dir}/databricks-dolly-15k-output.jsonl"
training_output_file = f"{data_dir}/training.jsonl"
validation_output_file = f"{data_dir}/validation.jsonl"
test_output_file = f"{data_dir}/test.jsonl"

# Specify the proportion of data for training and validation
train_proportion = 0.80
validation_proportion = 0.15
test_proportion = 0.05

# Read the JSONL file and shuffle the JSON objects
with open(input_file, "r") as f:
    lines = f.readlines()
    random.shuffle(lines)

# Calculate split indices
total_lines = len(lines)
train_index = int(total_lines * train_proportion)
val_index = int(total_lines * validation_proportion)

# Distribute JSON objects into training and validation sets
train_data = lines[:train_index]
validation_data = lines[train_index:train_index+val_index]
test_data = lines[train_index+val_index:]

# Write JSON objects to training file
with open(training_output_file, "w") as f:
    for line in train_data:
        f.write(line.strip() + "\n")

# Write JSON objects to validation file
with open(validation_output_file, "w") as f:
    for line in validation_data:
        f.write(line.strip() + "\n")

# Write JSON objects to training file
with open(test_output_file, "w") as f:
    for line in test_data:
        f.write(line.strip() + "\n")
