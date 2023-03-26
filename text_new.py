import glob
#
#       要把classes檔刪掉，才不會卡BUG
#       建議要先把檔案備份一次，以免操作失誤
# 
# 設定要讀取的檔案路徑和檔案類型
file_path = "C:\\Users\\cchhi\\Desktop\\5_copy\\*.txt" #檔案位置需加\\，用\會讀不到，"C:\\Users\\cchhi\\Desktop\\4_copy\\是自己的路徑
# 使用glob模塊查找符合條件的檔案路徑
file_list = glob.glob(file_path)
print(file_list)
# 使用for迴圈讀取每個檔案
for file_name in file_list:
    with open(file_name, "r") as file:
        # 讀取檔案內容
        content = file.read()
        content_list=content.split()
        print(content_list,"\n")
        # 處理檔案內容
        content_list[0]=5 #改成自己負責的數字
        print(content_list)
    with open(file_name, "w") as file:
            for content_li in content_list:
                file.write(str(content_li))
                file.write(" ")


