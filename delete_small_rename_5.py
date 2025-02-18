#刪除小圖並改名

import os
def delete_small_png_files(folder_path, size_threshold_bytes_mb=10):
    picture_counter=0
    # 檢查所有資料夾
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # 檢查png
            if file.lower().endswith('.png'):
                # 獲得檔案大小
                file_size = os.path.getsize(file_path)
                # 轉成mb
                file_size_mb=file_size/1024/1024
                # 比較大小
                if file_size_mb < size_threshold_bytes_mb:
                    try:
                        # 刪除圖片
                        os.remove(file_path)
                        picture_counter+=1
                    except Exception as e:
                        print(f"Error deleting {file_path}: {str(e)}")
    print(f"{picture_counter} pictures have been deleted")

def rename_images_with_folders(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # 檢查是否為圖片
            if file.lower().endswith(('.png')):
                # 獲得上層資料夾名稱
                parent_folder_name = os.path.basename(os.path.dirname(root))
                
                # 獲得當前資料夾名稱
                current_folder_name = os.path.basename(root)
                
                # 構建新檔名
                new_name = f"{current_folder_name}-{file}-{parent_folder_name}"
                new_name_2 = new_name.replace(".png","")
                new_name_3 = f"{new_name_2}.png"
                
                # 構建新路徑
                new_path = os.path.join(root, new_name_3)
                
                try:
                    # 重新命名
                    os.rename(file_path, new_path)
                    print(f"Renamed -> {new_name_3}")
                except Exception as e:
                    print(f"Error renaming {file_path}: {str(e)}")

def rename_images_sort(folder_path, start_index=1):
    for root, dirs, files in os.walk(folder_path):
        for folder_name in dirs:
            smallest_folder_name = os.path.join(root, folder_name)
            
            # 抓出圖片
            png_files = [file for file in os.listdir(smallest_folder_name) if file.lower().endswith('.png')]
            
            # 照時間排序
            png_files.sort(key=lambda x: os.path.getmtime(os.path.join(smallest_folder_name, x)))
            
            count = start_index
            
            for png_file in png_files:
                file_path = os.path.join(smallest_folder_name, png_file)
                # 重新命名
                new_name = f"{count}.png"
                
                new_path = os.path.join(smallest_folder_name, new_name)
                os.rename(file_path, new_path)
                
                count += 1

folder_path = os.getcwd()

#執行
delete_small_png_files(folder_path)
rename_images_sort(folder_path)
rename_images_with_folders(folder_path)
