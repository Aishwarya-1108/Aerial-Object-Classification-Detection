## Aerial Object Classification (Bird vs Drone)

## Project Overview
This project focuses on classifying aerial images into **Bird** or **Drone** using Deep Learning techniques. The system is designed for applications in surveillance, wildlife monitoring, and airspace safety.

---

 Objectives
- Build a **Custom CNN model**
- Apply **Transfer Learning using ResNet50**
- Compare model performance
- Deploy a **Streamlit web application**

---

##Dataset
The dataset contains RGB images divided into:
- Train set
- Validation set
- Test set

Classes:
- Bird
- Drone

---

Data Preprocessing
- Resized images to **224×224**
- Normalized pixel values to **[0,1]**

---

 Data Augmentation
- Rotation
- Horizontal Flip
- Zoom
- Brightness adjustment

---

Models Used

 Custom CNN
- Built from scratch
- Conv2D, MaxPooling, BatchNorm, Dropout

 ResNet50 (Transfer Learning)
- Pretrained on ImageNet
- Fine-tuned top layers

---

Training Details
- Optimizer: Adam
- Loss: Binary Crossentropy
- Batch Size: 32
- Callbacks:
  - EarlyStopping
  - ModelCheckpoint
  - ReduceLROnPlateau

---

 Model Evaluation

| Metric | CNN | ResNet50 |
|-------|------|----------|
| Accuracy | 87.4% | ~86–87% |
| Loss | 0.34 | 0.30 |
| Overfitting | Slight | Reduced |

---

Results
- CNN achieved slightly higher accuracy
- ResNet showed better generalization after fine-tuning

---

Conclusion
Both models performed well, but **ResNet50 is preferred for deployment** due to its robustness and generalization.

---

Streamlit App

Features:
- Upload image
- Predict Bird / Drone
- Display confidence score

