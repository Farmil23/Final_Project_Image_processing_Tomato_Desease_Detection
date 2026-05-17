import os
import cv2
import random

DATASET_PATH = "dataset/train"
VALID_EXTENSIONS = (".jpg", ".jpeg", ".png")

def load_images(dataset_path=DATASET_PATH):
    """
    Membaca semua gambar dari folder dataset
    """
    images = []
    labels = []
    total_images = 0
    
    for class_name in os.listdir(dataset_path):
        class_path = os.path.join(dataset_path, class_name)
        if not os.path.isdir(class_path):
            continue
        print(f"\nMembaca kelas: {class_name}")
        
        count = 0
        
        for file_name in os.listdir(class_path):
            if not file_name.lower().endswith(VALID_EXTENSIONS):
                continue
            img_path = os.path.join(class_path, file_name)
            image = cv2.imread(img_path)

            if image is None:
                print(f"[ERROR] Gambar rusak: {img_path}")
                continue

            images.append(image)
            labels.append(class_name)

            count += 1
            total_images += 1

        print(f"Jumlah gambar kelas {class_name}: {count}")

    print(f"\nTotal gambar berhasil dibaca: {total_images}")
    return images, labels

def show_random_dimensions(images):
    """
    Menampilkan ukuran gambar random
    """
    
    print("\nContoh dimensi gambar:")
    sample_images = random.sample(
        images,
        min(5, len(images))
    )
    for i, img in enumerate(sample_images):
        print(f"Gambar {i+1}: {img.shape}")

if __name__ == "__main__":
    images, labels = load_images()
    show_random_dimensions(images)