import tkinter as tk
import os
import math
import cv2
import numpy as np
import shutil
from tkinter import filedialog
from PIL import Image
from tkinter import scrolledtext
import pandas as pd
import send2trash
Image.MAX_IMAGE_PIXELS = None


######function###############################
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
                        terminal_text.insert(tk.END, f"Error deleting {file_path}: {str(e)}\n")
    print(f"{picture_counter} pictures have been deleted")
    terminal_text.insert(tk.END, f"{picture_counter} pictures have been deleted\n")

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
                    terminal_text.insert(tk.END, f"命名->{new_name_3}\n")
                except Exception as e:
                    print(f"Error renaming {file_path}: {str(e)}")
                    terminal_text.insert(tk.END, f"Error renaming {file_path}: {str(e)}\n")

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

def rename_images_sort_only(folder_path, start_index=1):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.png'): 
            # 抓出圖片
            png_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.png')]
            
            # 照時間排序
            png_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
            
            count = start_index
            
            for png_file in png_files:
                file_path = os.path.join(folder_path, png_file)
                # 重新命名
                new_name = f"{count}.png"
                
                new_path = os.path.join(folder_path, new_name)
                os.rename(file_path, new_path)
                
                count += 1

def rename_images_sort_bp9999(folder_path, start_index=1,last_index=9999,size_threshold_bytes_mb=10):
    for root, dirs, files in os.walk(folder_path):
        for folder_name in dirs:
            folder_path = os.path.join(root, folder_name)
            
            # 抓出圖片
            png_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.png')]
            
            # 照時間排序
            png_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
            
            # 改上次名字 
            count_s = start_index
            count_l = last_index
            for png_file in png_files:
                file_path = os.path.join(folder_path, png_file)
                file_size = os.path.getsize(file_path)
                # 轉成mb
                file_size_mb=file_size/1024/1024
                # 比較大小
                if file_size_mb < size_threshold_bytes_mb:
                    # 重新命名
                    new_name = f"temp({count_s}).png"
                    count_s += 1
                else:
                    new_name = f"temp({count_l}).png"
                    count_l -= 1
                new_path = os.path.join(folder_path, new_name)
                os.rename(file_path, new_path)

            # 抓出圖片
            png_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.png')]
            
            # 照時間排序
            png_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
            
            # 正式改名
            count_s = start_index
            count_l = last_index
            for png_file in png_files:
                file_path = os.path.join(folder_path, png_file)
                file_size2 = os.path.getsize(file_path)
                # 轉成mb
                file_size_mb=file_size2/1024/1024
                # 比較大小
                if file_size_mb < size_threshold_bytes_mb:
                    # 重新命名
                    new_name = f"{count_s}.png"
                    count_s += 1
                else:
                    new_name = f"{count_l}.png"
                    count_l -= 1
                new_path = os.path.join(folder_path, new_name)
                os.rename(file_path, new_path)
            
def swap_filenames(folder_path,x,y):
    x=int(x)
    y=int(y)
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

def combine_big_2(folder_path, big_x, big_y):
    images = []
    big_x=int(big_x)
    big_y=int(big_y)
    for root, dirs, files in os.walk(folder_path):
        for folder_name in dirs:
            subfolder_path = os.path.join(root, folder_name)
            
            for i in range(1, big_x * big_y + 1):
                image_filename = os.path.join(subfolder_path, f'{i}.png')
                if os.path.exists(image_filename):
                    small_image = cv2.imread(image_filename)
                    images.append(small_image)

            # 将小图像组合成大图像
            if images:
                width, height = images[0].shape[1] * big_x, images[0].shape[0] * big_y
                big_image = np.zeros((height, width, 3), dtype=np.uint8)

                for i, img in enumerate(images):
                    if img is not None:
                        row = i // big_x
                        col = i % big_x
                        x = col * img.shape[1]
                        y = row * img.shape[0]
                        big_image[y:y+img.shape[0], x:x+img.shape[1]] = img

                output_filename = os.path.join(subfolder_path, f'{folder_name}.png')
                cv2.imwrite(output_filename, big_image)
                terminal_text.insert(tk.END, f"{folder_name}完成\n")
                terminal_text.update_idletasks()
                print(f"{folder_name}完成\n")
                images = []
    
def rename_images_sort_bp9999_only(folder_path, start_index=1,last_index=9999,size_threshold_bytes_mb=10):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.png'): 
            # 抓出圖片
            png_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.png')]
            
            # 照時間排序
            png_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
            
            # 改上次名字 
            count_s = start_index
            count_l = last_index
            for png_file in png_files:
                file_path = os.path.join(folder_path, png_file)
                file_size = os.path.getsize(file_path)
                # 轉成mb
                file_size_mb=file_size/1024/1024
                # 比較大小
                if file_size_mb < size_threshold_bytes_mb:
                    # 重新命名
                    new_name = f"temp({count_s}).png"
                    count_s += 1
                else:
                    new_name = f"temp({count_l}).png"
                    count_l -= 1
                new_path = os.path.join(folder_path, new_name)
                os.rename(file_path, new_path)

            # 抓出圖片
            png_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.png')]
            
            # 照時間排序
            png_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
            
            # 正式改名
            count_s = start_index
            count_l = last_index
            for png_file in png_files:
                file_path = os.path.join(folder_path, png_file)
                file_size2 = os.path.getsize(file_path)
                # 轉成mb
                file_size_mb=file_size2/1024/1024
                # 比較大小
                if file_size_mb < size_threshold_bytes_mb:
                    # 重新命名
                    new_name = f"{count_s}.png"
                    count_s += 1
                else:
                    new_name = f"{count_l}.png"
                    count_l -= 1
                new_path = os.path.join(folder_path, new_name)
                os.rename(file_path, new_path)
        break
 
def swap_filenames_only(folder_path,x,y):
    x=int(x)
    y=int(y)
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.png'):
            for j in range(0, x * y, 2 * x):
                for i in range(x // 2):
                    idx1 = j + i
                    idx2 = j + x - i - 1
                    name1=f"{idx1+1}.png"
                    name2=f"{idx2+1}.png"
                    # 構建檔名
                    file1_path = os.path.join(folder_path, name1)
                    file2_path = os.path.join(folder_path, name2)
                    # 交換檔名
                    if os.path.exists(file1_path) and os.path.exists(file2_path):
                        os.rename(file1_path, os.path.join(folder_path, "temp.png"))
                        os.rename(file2_path, file1_path)
                        os.rename(os.path.join(folder_path, "temp.png"), file2_path)
        break

def combine_only(folder_path,big_x,big_y):
    images = []
    big_x=int(big_x)
    big_y=int(big_y)
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.png'):
            
            for i in range(1, big_x * big_y + 1):
                image_filename = os.path.join(folder_path, f'{i}.png')
                if os.path.exists(image_filename):
                    small_image = cv2.imread(image_filename)
                    images.append(small_image)

            # 将小图像组合成大图像
            if images:
                width, height = images[0].shape[1] * big_x, images[0].shape[0] * big_y
                big_image = np.zeros((height, width, 3), dtype=np.uint8)

                for i, img in enumerate(images):
                    if img is not None:
                        row = i // big_x
                        col = i % big_x
                        x = col * img.shape[1]
                        y = row * img.shape[0]
                        big_image[y:y+img.shape[0], x:x+img.shape[1]] = img
                current_folder_name = os.path.basename(folder_path)
                output_filename = os.path.join(folder_path, f'{current_folder_name}.png')
                cv2.imwrite(output_filename, big_image)
                terminal_text.insert(tk.END, f"{current_folder_name}完成\n")
                terminal_text.update_idletasks()
                print(f"{current_folder_name}完成\n")
                images = []
                break

def clone_image(gamma_folder,clone_folder):
    # 創造一個資料夾放複製圖片
    if not os.path.exists(clone_folder):
        os.makedirs(clone_folder)

    # 遍歷folder_path所有圖片
    for root, dirs, files in os.walk(gamma_folder):
        for file in files:
            if file.lower().endswith('.png'):
                source_file_path = os.path.join(root, file)
                destination_file_path = os.path.join(clone_folder, file)

                # 複製png到指定資料夾
                shutil.copy(source_file_path, destination_file_path)
                print(f"複製文件：{file}")
                terminal_text.insert(tk.END, f"複製文件：{file}\n")

    print("複製完成")

def catch_big_circle(img1):
    # 網路上抓的範例
    img = cv2.imread(img1,cv2.IMREAD_GRAYSCALE)
    mask = img.copy()
    _,binaryzation = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

    contours,_=cv2.findContours(binaryzation, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    aera = []

    for i in range(len(contours)):
        aera.append(cv2.contourArea(contours[i]))
    max_idx = np.argmax(np.array(aera))

    mask = cv2.drawContours(mask,contours,max_idx,0,cv2.FILLED)
    _,inv_mask= cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY_INV)
    return inv_mask

def img_xnor(img1,img2):
    img1 = cv2.imread(img1)
    img2 = cv2.imread(img2)
    output = cv2.bitwise_xor(img1, img2)  # 使用 bitwise_xor
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return output

def convert_to_black_and_white(clone_folder, bwp_folder,folder_path):
    # 創建資料夾
    if not os.path.exists(bwp_folder):
        os.makedirs(bwp_folder)

    # 篩選圖片
    files = os.listdir(clone_folder)
    image_files = [file for file in files if file.lower().endswith(('.png'))]

    # 處理圖片
    for image_file in image_files:
        # 輸入路徑
        input_path = os.path.join(clone_folder, image_file)
        # 輸出路徑
        new_name = image_file.replace(".png","")
        new_name2 = f"bwp_{new_name}.png"
        output_path = os.path.join(bwp_folder, new_name2)
        try:
            img = np.array(Image.open(input_path))
            # 轉換前，都先將圖片轉換成灰階色彩
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY); 
            # 如果大於 127 就等於 255，反之等於 0
            _, output1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)  
            temp1_image = Image.fromarray(output1)
            temp1_image.save(os.path.join(folder_path, 'temp1.png'))
            img1='temp1.png'
            mask=catch_big_circle(img1)
            temp2_image= Image.fromarray(mask)
            temp2_image.save(os.path.join(folder_path, 'temp2.png'))
            
            img2='temp2.png'
            bw_partical=img_xnor(img1,img2)
            pil_image= Image.fromarray(bw_partical)
            pil_image.save(output_path)
            print(f"二值圖: {new_name2}")
            terminal_text.insert(tk.END, f"二值圖: {new_name2}\n")

        except Exception as e:
            print(f"Error processing {input_path}: {str(e)}")
            terminal_text.insert(tk.END, f"Error processing {input_path}: {str(e)}\n")

def process_images_in_folder(bwp_folder,folder_path):
    result_data = {'File Name': [], 'Black Area': []}

    # 遍歷所有png
    for filename in os.listdir(bwp_folder):
        if filename.endswith(".png"):
            # 建立圖片
            image_path = os.path.join(bwp_folder, filename)
            image = Image.open(image_path)

            # 轉黑白
            bw_image = image.convert('1')

            # 取向素
            pixels = bw_image.load()

            # 計算黑色pixel
            black_pixels = 0
            for y in range(bw_image.size[1]):
                for x in range(bw_image.size[0]):
                    if pixels[x, y] == 0:  # 黑色像素的值为0
                        black_pixels += 1
                        
            result_data['File Name'].append(filename)
            result_data['Black Area'].append(black_pixels)
            terminal_text.insert(tk.END, f"計算: {filename}\n")

    # 建立DataFrame
    df = pd.DataFrame(result_data)

    # 保存excel
    folder_name=os.path.basename(folder_path)
    df.to_excel(f"{folder_name}_analyze.xlsx", index=False)

def has_subdirectories(path):
    # 取得指定路徑下的所有檔案和資料夾
    items = os.listdir(path)

    # 檢查每個項目是否為資料夾
    for item in items:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            return True  # 如果找到一個資料夾，就回傳 True

    return False  # 如果沒有找到資料夾，回傳 False

###############################################



#####按按鈕###################################
def delete_small_rename():
    terminal_text.delete("1.0", "end")
    terminal_text.insert(tk.END, ">>>\n")
    folder_path = entry_now_path.get()
    if os.path.exists(folder_path):
        delete_small_png_files(folder_path)
        has_sub=has_subdirectories(folder_path)
        if has_sub:
            rename_images_sort(folder_path)
        else:
            rename_images_sort_only(folder_path)
        rename_images_with_folders(folder_path)
        tk.messagebox.showinfo("complete", "complete")
        
    else:
        tk.messagebox.showerror("Error", "Invalid path. Please select a valid directory.")
    terminal_text.insert(tk.END, ">>>\n")

def browse_now_path():
    folder_selected = filedialog.askdirectory()
    entry_now_path.delete(0, tk.END)
    entry_now_path.insert(tk.END, folder_selected)

def sort_combine():
    terminal_text.delete("1.0", "end")
    terminal_text.insert(tk.END, ">>>\n")
    folder_path = entry_now_path.get()
    x=entry_img_x.get()
    y=entry_img_y.get()
    if os.path.exists(folder_path):
        has_sub=has_subdirectories(folder_path)
        if has_sub:
            rename_images_sort_bp9999(folder_path)
            swap_filenames(folder_path,x,y)
            combine_big_2(folder_path,x,y)
            tk.messagebox.showinfo("complete", "complete")
        else:
            rename_images_sort_bp9999_only(folder_path)
            swap_filenames_only(folder_path,x,y)
            combine_only(folder_path,x,y)
            tk.messagebox.showinfo("complete", "complete")
    else:
        tk.messagebox.showerror("Error", "Invalid path. Please select a valid directory.")
    terminal_text.insert(tk.END, ">>>\n")
    
def cal_particle():
    terminal_text.delete("1.0", "end")
    terminal_text.insert(tk.END, ">>>\n")
    folder_path = entry_now_path.get()
    gamma_folder = os.path.join(folder_path, 'gamma_0.25')
    clone_folder = os.path.join(folder_path, 'clone')
    bwp_folder = os.path.join(folder_path, 'bwp')
    if os.path.exists(folder_path):
        clone_image(gamma_folder,clone_folder)
        convert_to_black_and_white(clone_folder, bwp_folder,folder_path)
        process_images_in_folder(bwp_folder,folder_path)
        os.remove(os.path.join(bwp_folder,'temp1.png'))
        os.remove(os.path.join(bwp_folder,'temp2.png'))
        tk.messagebox.showinfo("complete", "complete")
        
    else:
        tk.messagebox.showerror("Error", "Invalid path. Please select a valid directory.")
    terminal_text.insert(tk.END, ">>>\n")
######################################################################

root = tk.Tk()
root.title("Program Executor")

#col 0
# 路径文字框
label_path = tk.Label(root, text="Select Path:")
label_path.grid(row=0, column=0, pady=10, padx=10,sticky="e")

entry_now_path = tk.Entry(root, width=40)
entry_now_path.grid(row=0, column=1, columnspan=4,pady=10, padx=10,sticky="ew")

# 瀏覽
button_browse_now_path = tk.Button(root, text="Browse", command=browse_now_path)
button_browse_now_path.grid(row=0, column=5, pady=10, padx=5)

label_terminal_title = tk.Label(root, text="Terminal")
label_terminal_title.grid(row=0, column=6, columnspan=4,pady=10, padx=10)

###############################################################################################
#sc
# 告訴路徑
label_sc_desc=tk.Label(root, text="說明：\n把資料夾所有圖片排序(ex:1~40)，再合成。\n可一次合多個資料夾，選到日期就可以了\n《注意》資料夾不要用中文命名",justify="left")
label_sc_desc.grid(row=1, column=1,columnspan=5,pady=10, padx=10,sticky="ws")

button_sc = tk.Button(root, text="排序、合成圖片",bg="lightgray", command=sort_combine)
button_sc.grid(row=1, column=0,rowspan=3, pady=5, padx=10,sticky="news")

label_img_xy= tk.Label(root, text="張數")
label_img_xy.grid(row=2, column=1,pady=10, padx=10,sticky="nw")

label_img_x= tk.Label(root, text="x  :             ")
label_img_x.grid(row=2, column=1,pady=10, padx=10,sticky="n")

entry_img_x = tk.Entry(root, width=2)
entry_img_x.grid(row=2, column=1,pady=10, padx=10,sticky="n")
entry_img_x.insert(0,"13")
x=entry_img_x.get()

label_img_y= tk.Label(root, text="y：     ")
label_img_y.grid(row=2, column=1,pady=10, padx=10,sticky="ne")

entry_img_y = tk.Entry(root, width=2)
entry_img_y.grid(row=2, column=1,pady=10, padx=10,sticky="ne")
entry_img_y.insert(0,"20")
y=entry_img_y.get()

#############################################################################################
#terminal

terminal_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="white", fg="black", font=("Courier", 12),width=30,height=10)
terminal_text.grid(row=1, column=6, rowspan=8, columnspan=4, sticky="nsew")
terminal_text.insert(tk.END, ">>>\n")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

############################################################################################
# 執行dsr
button_delete_rename = tk.Button(root, text="刪除、命名圖片",bg="lightgray", command=delete_small_rename,)
button_delete_rename.grid(row=4, column=0,   pady=10, padx=10, sticky="news")

label_dsr_desc=tk.Label(root, text="說明：\n刪除多餘的png，把完整大圖重新命名\n《注意》先確定圖片有合成過了，不然刪掉的小圖回不來的",justify="left")
label_dsr_desc.grid(row=4, column=1,columnspan=5,pady=10, padx=10,sticky="wn")
############################################################################################
# cp
button_cal_particle = tk.Button(root, text="計算顆粒",bg="lightgray", command=cal_particle)
button_cal_particle.grid(row=6, column=0,   pady=10, padx=10, sticky="news")

label_cp_desc=tk.Label(root, text="說明：\n二質化計算顆粒\n(已廢棄 不建議使用)",justify="left")
label_cp_desc.grid(row=6, column=1,columnspan=5,pady=10, padx=10,sticky="wn")
button_cal_particle.config(state=tk.DISABLED)
############################################################################################

root.mainloop()