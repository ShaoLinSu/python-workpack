import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
###############################################################################################
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
                        # #     # terminal_text.insert(tk.END, f"Error deleting {file_path}: {str(e)}\n")
    print(f"{picture_counter} pictures have been deleted")
    # #     # terminal_text.insert(tk.END, f"{picture_counter} pictures have been deleted\n")

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
                    #     # terminal_text.insert(tk.END, f"命名->{new_name_3}\n")
                except Exception as e:
                    print(f"Error renaming {file_path}: {str(e)}")
                    #     # terminal_text.insert(tk.END, f"Error renaming {file_path}: {str(e)}\n")

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

def rename_images_sort_bp1048575(folder_path, start_index=1,last_index=1048575,size_threshold_bytes_mb=0.004):
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
                    # 建構檔名
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
                #     # terminal_text.insert(tk.END, f"{folder_name}完成\n")
                #     # terminal_text.update_idletasks()
                print(f"{folder_name}完成\n")
                images = []
    
def rename_images_sort_bp1048575_only(folder_path, start_index=1,last_index=1048575,size_threshold_bytes_mb=10):
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
                    # 建構檔名
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

            # 將小圖和成大圖
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
                #     # terminal_text.insert(tk.END, f"{current_folder_name}完成\n")
                #     # terminal_text.update_idletasks()
                print(f"{current_folder_name}完成\n")
                images = []
                break

def split_image(folder_path ,resolution_x,resolution_y):
    files = os.listdir(folder_path)
    for file in files:
        if file.lower().endswith(".png") and "1048575" in file:
            current_filepath = os.path.join(folder_path, file)
    # 讀取原始圖片
    original_image = cv2.imread(current_filepath, cv2.IMREAD_UNCHANGED)
    x = int(resolution_x)
    y = int(resolution_y)
    # 取得圖片的寬度和高度
    height, width, _ = original_image.shape

    # 計算每張切割圖片的寬度和高度
    pieces_width = width // x
    pieces_height = height // y
    print(f"{pieces_width} x {pieces_height}")
    # 迭代切割並保存每張圖片
    
    for i in range(y):
        for j in range(x):
            left = i * pieces_height
            top = j * pieces_width
            right = (i + 1) * pieces_height
            bottom = (j + 1) * pieces_width

            # 切割圖片
            piece = original_image[left:right, top:bottom]

            # 檢查小塊的大小是否大於零
            if piece.size > 0:
                # 設定輸出檔名
                output_filename = f"{folder_path}/piece_{i+1}_{j+1}.png"

                # 儲存切割後的圖片
                cv2.imwrite(output_filename, piece)
    
def display_image(img_path):
    image = Image.open(img_path)
    image.thumbnail((250, 250))  
    tk_image = ImageTk.PhotoImage(image)

    img_dis_before.config(image=tk_image)
    img_dis_before.image = tk_image  

def gray_remove(img_path,entry_rb_1,entry_rb_2):
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)  # 開啟圖片
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)         # 因為是 jpg，要轉換顏色為 BGRA
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        # 新增 gray 變數為轉換成灰階的圖片
    h = img.shape[0]     # 取得圖片高度
    w = img.shape[1]     # 取得圖片寬度

    # 依序取出圖片中每個像素
    for x in range(w):
        for y in range(h):
            if gray[y, x]>128:
                img[y, x, 3] = 255 - gray[y, x]
                # 如果該像素的灰階度大於 200，調整該像素的透明度
                # 使用 255 - gray[y, x] 可以將一些邊緣的像素變成半透明，避免太過鋸齒的邊緣
    
    pil_img = Image.fromarray(img)
    pil_img.thumbnail((250, 250))
    tk_image = ImageTk.PhotoImage(pil_img)
    img_dis_after.config(image=tk_image)
    img_dis_after.image = tk_image  

def has_subdirectories(path):
    # 取得指定路徑下的所有檔案和資料夾
    items = os.listdir(path)

    # 檢查每個項目是否為資料夾
    for item in items:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            return True  # 如果找到一個資料夾，就回傳 True

    return False  # 如果沒有找到資料夾，回傳 False


###############################################################################################
# 按鈕
def browse_now_path():
    folder_selected = filedialog.askdirectory()
    entry_now_path.delete(0, tk.END)
    entry_now_path.insert(tk.END, folder_selected)


def delete_small_rename():
        # terminal_text.delete("1.0", "end")
        # terminal_text.insert(tk.END, ">>>\n")
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
        # terminal_text.insert(tk.END, ">>>\n")

def sort_combine():
        # terminal_text.delete("1.0", "end")
        # terminal_text.insert(tk.END, ">>>\n")
    folder_path = entry_now_path.get()
    x=entry_sc_x.get()
    y=entry_sc_y.get()
    if os.path.exists(folder_path):
        has_sub=has_subdirectories(folder_path)
        if has_sub:
            rename_images_sort_bp1048575(folder_path)
            # swap_filenames(folder_path,x,y)
            combine_big_2(folder_path,x,y)
            tk.messagebox.showinfo("complete", "complete")
        else:
            rename_images_sort_bp1048575_only(folder_path)
            # swap_filenames_only(folder_path,x,y)
            combine_only(folder_path,x,y)
            tk.messagebox.showinfo("complete", "complete")
    else:
        tk.messagebox.showerror("Error", "Invalid path. Please select a valid directory.")
        # terminal_text.insert(tk.END, ">>>\n")
    
def split_1048575(): # 沒用has_sub
    folder_path = entry_now_path.get()
    x=entry_sc_x.get()
    y=entry_sc_y.get()
    if os.path.exists(folder_path):
        rename_images_sort_bp1048575_only(folder_path)
        split_image(folder_path ,x ,y)
        tk.messagebox.showinfo("complete", "complete")
    else:
        tk.messagebox.showerror("Error", "Invalid path. Please select a valid directory.")

def browse_img():
    img_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])

    entry_now_img.delete(0, tk.END)
    entry_now_img.insert(tk.END, img_path)
    if img_path:
        display_image(img_path)

def remove_background():
    img_path = entry_now_img.get()
    if img_path:
        gray_remove(img_path,entry_rb_1,entry_rb_2)

        
    else:
        tk.messagebox.showerror("Error", "Invalid path. Please select a valid directory.")


###############################################################################################
root = tk.Tk()
root.geometry("1200x600")
root.title("Image Processing")
###############################################################################################
# 選擇路徑
label_path = tk.Label(root, text="    選擇路徑:")
label_path.place(x=10, y=20)

entry_now_path = tk.Entry(root, width=40)
entry_now_path.place(x=100, y=20)

# 瀏覽
button_browse_now_path = tk.Button(root, text="Browse", command=browse_now_path)
button_browse_now_path.place(x=470, y=15)
###############################################################################################
#sc
# 告訴路徑
label_sc_desc=tk.Label(root, text="《注意》資料夾不要用中文命名",justify="left")
label_sc_desc.place(x=130, y=70)

button_sc = tk.Button(root, text="合成圖片",bg="lightgray", command=sort_combine)
button_sc.place(x=10, y=70, height=45, width=120)

button_sp = tk.Button(root, text="分開圖片",bg="lightgray", command=split_1048575)
button_sp.place(x=10, y=130, height=45, width=120)

label_sc_xy= tk.Label(root, text="張數")
label_sc_xy.place(x=130, y=120)

label_sc_x= tk.Label(root, text="x：")
label_sc_x.place(x=170, y=120)

entry_sc_x = tk.Entry(root, width=3)
entry_sc_x.place(x=200, y=120)
entry_sc_x.insert(0,"13")
x=entry_sc_x.get()

label_sc_y= tk.Label(root, text="y：")
label_sc_y.place(x=240, y=120)

entry_sc_y = tk.Entry(root, width=3)
entry_sc_y.place(x=270, y=120)
entry_sc_y.insert(0,"20")
y=entry_sc_y.get()

############################################################################################
# 執行dsr
button_delete_rename = tk.Button(root, text="刪除、命名圖片",bg="lightgray", command=delete_small_rename)
button_delete_rename.place(x=10, y=200, height=100, width=120)

label_dsr_desc=tk.Label(root, text="說明：\n刪除多餘的png，把完整大圖重新命名\n《注意》先確定圖片有合成過了，不然刪掉的小圖回不來的",justify="left")
label_dsr_desc.place(x=130, y=200)

label_dsr_mb= tk.Label(root, text="   小於        mb就刪除")
label_dsr_mb.place(x=130, y=270)

entry_dsr_mb = tk.Entry(root, width=2)
entry_dsr_mb.place(x=180, y=270)
entry_dsr_mb.insert(0,"10")
entry_dsr_mb_input=entry_dsr_mb.get()
#############################################################################################
# 去背
button_rb = tk.Button(root, text="簡易去背",bg="lightgray", command=remove_background)
button_rb.place(x=10, y=400, height=80, width=120)

label_rb_desc = tk.Label(root,text="說明：\n只是指定一個灰階顏色去除",justify="left")
label_rb_desc.place(x=130, y=400)

entry_rb_1 = tk.Entry(root, width=4)
entry_rb_1.place(x=150, y=450)
entry_rb_1.insert(0,"215")
entry_rb_1=entry_rb_1.get()

label_rb_y= tk.Label(root, text=" < 去除的部分 <")
label_rb_y.place(x=190, y=450)

entry_rb_2 = tk.Entry(root, width=4)
entry_rb_2.place(x=310, y=450)
entry_rb_2.insert(0,"226")
entry_rb_2=entry_rb_2.get()
#############################################################################################
# gif轉png
button_gtp = tk.Button(root, text="gif轉png",bg="lightgray", command="")
button_gtp.place(x=10, y=500, height=80, width=120)

label_gtp_desc = tk.Label(root,text="說明：\n把gif每一幀變成png存在gif旁",justify="left")
label_gtp_desc.place(x=130, y=500)
###############################################################################################
# 選擇路徑
label_img = tk.Label(root, text="    選擇圖片:")
label_img.place(x=10, y=355)

entry_now_img = tk.Entry(root, width=40)
entry_now_img.place(x=100, y=355)

# 瀏覽
button_browse_now_img = tk.Button(root, text="瀏覽", command=browse_img)
button_browse_now_img.place(x=470, y=350,width=60)
###############################################################################################
vertical_separator = ttk.Separator(root, orient="vertical")
vertical_separator.pack(fill="y", padx=600)
###############################################################################################
#顯示圖片
img_dis_before = tk.Label(root)
img_dis_before.place(x=600,y=100)

img_dis_after = tk.Label(root)
img_dis_after.place(x=900,y=100)



root.mainloop()
# pyinstaller -F tk_5.py --noconsole
