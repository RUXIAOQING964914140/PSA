import os
import subprocess

# Folder paths
train_indices_folder = "mafft_samples/"  # Folder containing train_indices_fold_*.txt files
result_model_folder = "mafft_samples/result_model/"  # Folder to save the trained models
train_result_folder = "mafft_samples/train_result/"  # Folder to save the command output logs
ranklib_jar_path = "RankLib-2.16.jar"  # Path to the RankLib JAR file

# Ensure output folders exist
os.makedirs(result_model_folder, exist_ok=True)
os.makedirs(train_result_folder, exist_ok=True)

# RankLib parameters
ranker = 0
metric2t = "NDCG@50"
tree = 500
leaf = 300
shrinkage = 0.03
mls = 5

# Iterate over train_indices_fold_*.txt files
for file_name in os.listdir(train_indices_folder):
    if file_name.startswith("train_indices_fold_") and file_name.endswith(".txt"):
        train_file_path = os.path.join(train_indices_folder, file_name)
        model_output_path = os.path.join(result_model_folder, f"KIBA_model_{file_name.replace('.txt', '')}.txt")
        result_output_path = os.path.join(train_result_folder, f"train_result_{file_name.replace('.txt', '')}.txt")

        # Build the command
        command = [
            "java", "-jar", ranklib_jar_path,
            "-train", train_file_path,
            "-ranker", str(ranker),
            "-metric2t", metric2t,
            "-tree", str(tree),
            "-leaf", str(leaf),
            "-shrinkage", str(shrinkage),
            "-mls", str(mls),
            "-save", model_output_path
        ]

        # Execute the command and save output to file
        try:
            with open(result_output_path, "w") as output_file:
                subprocess.run(command, check=True, stdout=output_file, stderr=subprocess.STDOUT)
            print(f"Command executed successfully, model saved to {model_output_path}, results saved to {result_output_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
