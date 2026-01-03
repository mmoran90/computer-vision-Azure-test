
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

endpoint = "https://computer-vision-resource-test.cognitiveservices.azure.com/"
key = "xxx"

client = ComputerVisionClient(
    endpoint,
    CognitiveServicesCredentials(key)
)

image_path = "images/flower.jpg"

# Open image and analyze
with open(image_path, "rb") as image_stream:
    analysis = client.analyze_image_in_stream(
        image=image_stream,
        visual_features=["Description", "Tags"]
    )

# Show description caption
print("Caption:")
for caption in analysis.description.captions:
    print(f"  {caption.text} (Confidence: {caption.confidence:.2f})")

# Show tags
print("\nTags:")
for tag in analysis.tags:
    print(f"  {tag.name} (Confidence: {tag.confidence:.2f})")