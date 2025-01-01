import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
from PIL import Image, ImageDraw
from dotenv import load_dotenv  # type: ignore
from transformers import pipeline
from collections import defaultdict
import subprocess

load_dotenv()

def draw_bounding_boxes(image_paths):
    all_object_counts = []

    for image_path in image_paths:
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        # Perform object detection using DETR model
        detector = pipeline(task="object-detection", model="facebook/detr-resnet-50")
        outputs = detector(image_path)

        # Count objects
        object_counts = defaultdict(int)
        for output in outputs:
            label = output['label']
            object_counts[label] += 1

        all_object_counts.append(object_counts)

        # Draw bounding boxes
        for output in outputs:
            box = output['box']
            label = output['label']
            draw.rectangle([(box['xmin'], box['ymin']), (box['xmax'], box['ymax'])], outline="red", width=2)
            draw.text((box['xmin'], box['ymin'] - 10), label, fill="red")

        image.show()

    return all_object_counts

def generate_story(object_counts):
    stories = []
    for i, counts in enumerate(object_counts, start=1):
        # Construct story for each image
        story = "In a world where"
        for label, count in counts.items():
            story += f" {count} {label}s,"
        story += " emerged into existence. They embarked on a journey full of adventure and mystery, exploring the depths of imagination and creativity."
        stories.append((f"Image {i} Story:\n" + story))
    return stories

if __name__ == "__main__":
    # Example usage with three image paths
    image_paths = [
        r"C:\Users\LENOVO\OneDrive\Desktop\Art Of Visual Storytelling\input_images\img1.webp",
        r"C:\Users\LENOVO\OneDrive\Desktop\Art Of Visual Storytelling\input_images\img2.jpg",
        r"C:\Users\LENOVO\OneDrive\Desktop\Art Of Visual Storytelling\input_images\img3.png"
    ]
    
    # Draw bounding boxes and generate initial object stories
    all_object_counts = draw_bounding_boxes(image_paths)
    image_stories = generate_story(all_object_counts)

    # Print the generated stories
    print("\nGenerated Stories:")
    for story in image_stories:
        print(story)

    # Combine the three stories into one prompt for the wizard-vicuna-uncensored:7b model
    combined_stories = "\n\n".join(image_stories)
    final_prompt = (
        "Below are three separate story seeds generated from object detections:\n\n"
        f"{combined_stories}\n\n"
        "Now please create a single, cohesive story that unites the elements and characters from all three "
        "stories into one grand narrative. Emphasize the interactions, the diverse items, and the sense of "
        "adventure that spans across this combined world."
    )

    # Run the Ollama model with the combined prompt
    try:
        result = subprocess.run(
            ["ollama", "run", "wizard-vicuna-uncensored:7b"],
            input=final_prompt,
            capture_output=True,
            text=True,
            check=True,
            encoding='utf-8',     # Use UTF-8 encoding
            errors='replace'      # Replace un-decodable characters
        )

        final_story = result.stdout.strip()

        print("\nFinal Combined Story:\n")
        print(final_story)

    except subprocess.CalledProcessError as e:
        print("An error occurred while running the model:")
        print(e.stderr)
