import os
import subprocess

# Folder paths
test_indices_folder = "mafft_samples/"  # Folder containing test_indices_fold_*.txt files
result_model_folder = "mafft_samples/result_model/"  # Folder containing the saved models
test_result_folder = "mafft_samples/test_result/"  # Folder to save the command output data
ranklib_jar_path = "RankLib-2.16.jar"  # Path to the RankLib JAR file

# Ensure the output folder exists
os.makedirs(test_result_folder, exist_ok=True)

# Iterate over test_indices_fold_*.txt files
for file_name in os.listdir(test_indices_folder):
    if file_name.startswith("test_indices_fold_") and file_name.endswith(".txt"):
        test_file_path = os.path.join(test_indices_folder, file_name)
        model_file_name = file_name.replace("test_indices_fold_", "KIBA_model_train_indices_fold_")
        model_file_path = os.path.join(result_model_folder, model_file_name)

        # Build the output file path
        rank_output_path = os.path.join(test_result_folder, f"KIBA_test_sam_rank_{file_name.replace('.txt', '')}.txt")

        # Build the command
        command = [
            "java", "-jar", ranklib_jar_path,
            "-load", model_file_path,
            "-rank", test_file_path,
            "-indri", rank_output_path
        ]

        # Execute the command and save output to file
        try:
            subprocess.run(command, check=True)
            print(f"Command executed successfully, results saved to {rank_output_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
