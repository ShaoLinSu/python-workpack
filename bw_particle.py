from PIL import Image
import os
import cv2
import numpy as np
folder_path = os.getcwd()
Image.MAX_IMAGE_PIXELS = None

def catch_big_circle(img1):
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


def convert_to_black_and_white(input_folder, output_folder):
    # 創建資料夾
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 篩選圖片
    files = os.listdir(input_folder)
    image_files = [file for file in files if file.lower().endswith(('.png'))]

    # 處理圖片
    for image_file in image_files:
        # 輸入路徑
        input_path = os.path.join(input_folder, image_file)
        # 輸出路徑
        new_name = image_file.replace(".png","")
        new_name2 = f"bwp_{new_name}.png"
        output_path = os.path.join(output_folder, new_name2)
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
            print(f"Converted and saved: {new_name2}")

        except Exception as e:
            print(f"Error processing {input_path}: {str(e)}")

# 設定路徑資料夾
input_folder = os.path.join(folder_path, 'clone')
output_folder = os.path.join(folder_path, 'bwp')

# 執行
convert_to_black_and_white(input_folder, output_folder)
os.remove(os.path.join(folder_path,'temp1.png'))
os.remove(os.path.join(folder_path,'temp2.png'))