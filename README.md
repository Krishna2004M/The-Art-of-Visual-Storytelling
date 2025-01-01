# Object Detection and Story Generation Project

This project combines AI-powered object detection with creative story generation. It uses object detection to identify items in images and generates cohesive narratives based on these detections. The resulting stories highlight imaginative interactions between the detected objects in a unified storyline.

---

## Features
- **Object Detection**: Identifies objects in images using the DETR (DEtection TRansformer) model.
- **Bounding Boxes**: Draws bounding boxes on detected objects in the images.
- **Story Generation**: Creates descriptive stories for each image based on the detected objects.
- **Cohesive Story**: Combines individual stories into one grand narrative using the `wizard-vicuna-uncensored:7b` model.

---

## Project Objective
To explore how AI can creatively transform object detection data into compelling and imaginative narratives.

---

## Prerequisites
Ensure you have the following installed:
- **Python 3.x**
- Required Python libraries listed in `requirements.txt`:
  - `transformers`
  - `Pillow`
  - `python-dotenv`
- **Ollama CLI**: For running the `wizard-vicuna-uncensored:7b` model.
- Compatible GPU for object detection and story generation tasks.

---

## Installation
1. Clone the repository:
    ```bash
    git clone https://https://github.com/Krishna2004M
    cd project-name
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the `Ollama` CLI:
    - Ensure the `wizard-vicuna-uncensored:7b` model is downloaded:
      ```bash
      ollama pull wizard-vicuna-uncensored:7b
      ```

---

## Usage
1. **Prepare Images**:
   - Place your images in a folder (e.g., `input_images`).
   - Update the `image_paths` variable in the script with the paths to your images.

2. **Run the Script**:
    ```bash
    python main.py
    ```

3. **View Outputs**:
   - The script will display images with bounding boxes.
   - Generated stories will be printed in the console.
   - The final cohesive story will also be displayed.

---

## Example
### Input
- Images: Detected objects from:
  - `img4.webp`
  - `pic1.jpg`
  - `ts1.png`

### Output
1. **Object Detection**:
   - Detected objects with bounding boxes displayed on input images.
2. **Generated Stories**:
   - Individual stories for each image based on detected objects.
3. **Cohesive Story**:
   - A unified narrative that connects elements from all images.

---

## Technologies Used
- **Python**
- **Pillow**: For image processing.
- **Transformers**: For DETR model and pipeline.
- **Ollama CLI**: For running `wizard-vicuna-uncensored:7b` model.

---

## File Structure
```plaintext
project-name/
├── README.md
├── requirements.txt
├── main.py
├── input_images/
│   ├── img4.webp
│   ├── pic1.jpg
│   ├── ts1.png
