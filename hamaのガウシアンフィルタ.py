import cv2
img = cv2.imread("hama.jpg") # フィルタを適用

img2 = cv2.Canny(img, 30, 200) # ネガポジ反転

img2 = 256 - img2 # ファイルに保存

cv2.imwrite("hama-canny.jpg", img2)
