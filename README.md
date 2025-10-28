# 🚨 AI-Powered Shoplifting Detection and Comparative Video Analysis

## 🌟 Project Overview: Smart Retail Security

This repository presents a robust, state-of-the-art solution for **real-time shoplifting detection** using computer vision. Leveraging the power of **YOLOv8** (You Only Look Once) and the **Ultralytics** framework, this project provides a clear, comparative analysis of video footage to highlight anomalous behavior.

The core deliverable is a highly detailed Jupyter Notebook (`Shoplifting_Detection_Analysis.ipynb`) designed to be immediately runnable and visually astounding, perfect for demonstrating advanced AI capabilities to stakeholders or potential employers.

---

## ✨ Key Features

*   **High-Performance Detection:** Utilizes the cutting-edge YOLOv8 model for fast and accurate object detection.
*   **Comparative Analysis:** Demonstrates the model's performance on **two distinct video scenarios**:
    1.  `video_normal.mp4`: Control test with regular customer behavior.
    2.  `video_shoplifting.mp4`: Anomaly test simulating a potential shoplifting event.
*   **Astounding Visualization:** The notebook includes embedded video playback of the annotated results and a comparative **metrics chart** to instantly visualize the difference in detection counts between the two scenarios.
*   **Modular & Clean Code:** The notebook is structured into logical sections for easy understanding, modification, and extension.

## 🚀 Getting Started

Follow these simple steps to set up the environment and run the analysis.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Setup Environment

It is highly recommended to use a Python virtual environment.

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the Analysis

Open the Jupyter Notebook and execute the cells sequentially:

```bash
jupyter notebook Shoplifting_Detection_Analysis.ipynb
```

The notebook will automatically:
1.  Load the YOLOv8 model (using `yolov8n.pt` by default).
2.  Run detection on both videos in the `data/` folder.
3.  Save the annotated videos to the `runs/detect` directory.
4.  Display the annotated videos and a comparative bar chart of the results.

## 📁 Repository Structure

```
.
├── data/
│   ├── video_normal.mp4          # Control video (Placeholder)
│   └── video_shoplifting.mp4     # Anomaly video (Placeholder)
├── runs/
│   └── detect/                   # Output directory for annotated videos
├── Shoplifting_Detection_Analysis.ipynb  # The main analysis notebook
└── requirements.txt              # Project dependencies
└── README.md                     # This file
```

## 💡 Future Enhancements

This project is a powerful foundation. Consider these next steps to take it to the next level:

*   **Tracking Integration:** Implement **DeepSORT** or **ByteTrack** to track individual objects and analyze their movement patterns over time.
*   **Custom Training:** Train the model on a custom dataset with specific "Shoplifting" action classes for more granular anomaly detection.
*   **Real-Time Dashboard:** Develop a simple web interface (e.g., using Flask/Streamlit) to stream the detection and display real-time metrics.
*   **Alert System:** Integrate an event-based system to trigger notifications when a high-confidence shoplifting event is detected.

---
*Project maintained by [Your Name/GitHub Handle]*
