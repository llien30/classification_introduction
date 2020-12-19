import glob
import shutil

train_data_n = glob.glob("./chest_xray/train/NORMAL/*.jpeg")
train_data_a = glob.glob("./chest_xray/train/PNEUMONIA/*.jpeg")
print(len(train_data_n))
print(len(train_data_a))

test_data_n = glob.glob("./chest_xray/test/NORMAL/*.jpeg")
test_data_a = glob.glob("./chest_xray/test/PNEUMONIA/*.jpeg")
print(len(test_data_n))
print(len(test_data_a))

# normal = train_data_n + test_data_n
abnormal = train_data_a + test_data_a


# for path in normal[1000:1500]:
#     shutil.move(path, "./data/test/normal")


for path in abnormal[:1000]:
    shutil.move(path, "./data/train/pneumonia")

for path in abnormal[1000:1500]:
    shutil.move(path, "./data/test/pneumonia")
