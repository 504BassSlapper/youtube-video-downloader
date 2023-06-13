import os
import shutil


def move_files_to_subdirectory(src_dir, dest_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    files = os.listdir(src_dir)
    for file in files:
        if file.endswith(".mp4"):
            new_file_name = os.path.splitext(file)[0] + ".mp3"

            # get source and destination file path before mv
            src_file_path = os.path.join(src_dir, file)
            dest_file_path = os.path.join(dest_dir, new_file_name)
            # performing mv
            try:
                shutil.move(src_file_path, dest_file_path)
                print(
                    f"The file '{src_file_path}' have been renamed and mooved successfully"
                )
            except:
                print(f"could not transfert '{src_file_path}' to '{dest_file_path}'")


move_files_to_subdirectory(".", "mp3")
