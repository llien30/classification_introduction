import glob

train_n_dataset = glob.glob("./data/train/normal/*.jpeg")
train_a_dataset = glob.glob("./data/train/pneumonia/*.jpeg")
test_n_dataset = glob.glob("./data/test/normal/*.jpeg")
test_a_dataset = glob.glob("./data/test/pneumonia/*.jpeg")
print("train")
print(f"normal : {len(train_n_dataset)}")
print(f"pneumonia : {len(train_a_dataset)}")
print("test")
print(f"normal : {len(test_n_dataset)}")
print(f"pneumonia : {len(test_a_dataset)}")
