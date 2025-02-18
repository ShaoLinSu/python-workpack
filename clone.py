import os
import shutil

def clone_all(folder_path):
    # 要複製到的目的地
    destination_directory = os.path.join(folder_path, 'clone')

    # 檢查是存在clone資料夾
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # 抓所有png
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.png'):
                source_file_path = os.path.join(root, file)
                destination_file_path = os.path.join(destination_directory, file)

                # 複製png
                shutil.copy(source_file_path, destination_file_path)
                print(f"複製文件：-> {destination_file_path}")

    print("複製完成")

# 此資料夾
folder_path = os.getcwd()
clone_all(folder_path)
