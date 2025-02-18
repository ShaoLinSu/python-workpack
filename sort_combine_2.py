import os
from PIL import Image
import math
Image.MAX_IMAGE_PIXELS = None
# 照時間順序重新命名
def rename_images_sort(folder_path, start_index=1):
    for root, dirs, files in os.walk(folder_path):
        for folder_name in dirs:
            folder_path = os.path.join(root, folder_name)
            
            # 抓出圖片
            png_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.png')]
            
            # 照時間排序
            png_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
            
            count = start_index
            for png_file in png_files:
                file_path = os.path.join(folder_path, png_file)
                
                # 重新命名
                new_name = f"temp({count}).png"
                
                new_path = os.path.join(folder_path, new_name)
                os.rename(file_path, new_path)
                
                count += 1
            count=start_index
            png_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.png')]
            
            # 照時間排序
            png_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))

            for png_file in png_files:
                file_path = os.path.join(folder_path, png_file)
                
                # 重新命名
                new_name = f"{count}.png"
                
                new_path = os.path.join(folder_path, new_name)
                os.rename(file_path, new_path)
                
                count += 1

# 交換檔案
#[ 5  4  3  2  1             [ 1  2  3  4  5
#  6  7  8  9 10               6  7  8  9 10
# 15 14 13 12 11              11 12 13 14 15
# 16 17 18 19 20              16 17 18 19 20
# 25 24 23 22 21     ===>     21 22 23 24 25
# 26 27 28 29 30              26 27 28 29 30
# 35 34 33 32 31              31 32 33 34 35
# 36 37 38 39 40]             36 37 38 39 40]
def swap_filenames(folder_path,x,y):
    for root, dirs, files in os.walk(folder_path):
        for dir_name in dirs:
            for j in range(0, x * y, 2 * x):
                for i in range(x // 2):
                    idx1 = j + i
                    idx2 = j + x - i - 1
                    name1=f"{idx1+1}.png"
                    name2=f"{idx2+1}.png"
                    dir_path = os.path.join(root, dir_name)
                    # 構建檔名
                    file1_path = os.path.join(dir_path, name1)
                    file2_path = os.path.join(dir_path, name2)
                    # 交換檔名
                    if os.path.exists(file1_path) and os.path.exists(file2_path):
                        os.rename(file1_path, os.path.join(dir_path, "temp.png"))
                        os.rename(file2_path, file1_path)
                        os.rename(os.path.join(dir_path, "temp.png"), file2_path)
                        print(f"已交换文件名：{os.path.basename(file1_path)} <-> {os.path.basename(file2_path)}")

def combine_big_2(folder_path,big_x,big_y):
    
    width, height = big_x * 1920, big_y * 1200
    big_image = Image.new('RGB', (width, height))
    for root, dirs, files in os.walk(folder_path):
        for folder_name in dirs:
            subfolder_path=os.path.join(root, folder_name)
            
            print(subfolder_path)
            for i in range(1, big_x*big_y+1):
                image_filename = os.path.join(subfolder_path, f'{i}.png')
                if os.path.exists(image_filename):
                    small_image = Image.open(image_filename)
                    row = (i - 1) // big_x
                    col = (i - 1) % big_x
                    x = col * 1920
                    y = row * 1200
                    big_image.paste(small_image, (x, y))

            output_filename = os.path.join(subfolder_path, f'{folder_name}.png')
            big_image.save(output_filename)
            big_image = Image.new('RGB', (width, height))
    big_image.close()

folder_path = r"D:\dark_field\2023.12.12_cp\gamma_0.25"
x=4
y=8
rename_images_sort(folder_path)
swap_filenames(folder_path,x,y)
combine_big_2(folder_path,x,y)