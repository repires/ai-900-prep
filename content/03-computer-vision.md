# Domain 3: Computer Vision on Azure (15-20%)

---

## 📺 Official Microsoft Learn Video

> **Full Playlist:** <a href="https://www.youtube.com/playlist?list=PLahhVEj9XNTfFP-841X_gdJ0nmjfjfCQN" target="_blank">AI-900: Microsoft Azure AI Fundamentals</a>

### Episode 6: Fundamentals of Computer Vision (22:02)

Covers computer vision concepts, image analysis, face detection, and text recognition (OCR) capabilities in Azure.

<a href="https://www.youtube.com/watch?v=0Xl-Q161RIA&list=PLahhVEj9XNTfFP-841X_gdJ0nmjfjfCQN&index=6" target="_blank">▶️ Watch Episode 6 on YouTube</a>

---

## Computer Vision Solutions

### Image Classification
- Assigns a single label to an entire image
- "What is in this image?"
- **Example**: Is this a cat or a dog?

### Object Detection
- Identifies and locates multiple objects in an image
- Returns bounding boxes with coordinates
- **Example**: Find all cars and pedestrians in a street photo

### Optical Character Recognition (OCR)
- Extracts printed or handwritten text from images
- Supports multiple languages
- **Use cases**: Digitizing documents, reading signs, processing forms

### Facial Detection and Analysis
- **Detection**: Locates faces in images
- **Analysis**: Determines attributes (age, emotion, glasses, makeup)
- **Verification**: Confirms if two faces are the same person
- **Identification**: Matches a face to a known person

---

## Azure AI Vision Service

### Capabilities
- **Analyze Image**: Tags, categories, descriptions, objects, faces
- **Read (OCR)**: Extract text from images and PDFs
- **Image Generation**: Create images from descriptions
- **Spatial Analysis**: Analyze movement in video streams

### Image Analysis Features
| Feature | Description |
|---------|-------------|
| Tags | Keywords describing image content |
| Caption | Human-readable description |
| Objects | Detected objects with bounding boxes |
| Brands | Recognized commercial logos |
| Categories | High-level image categorization |
| Color | Dominant colors and accent colors |
| Faces | Face locations (basic detection) |
| Adult | Adult/racy/gory content flags |
| Smart Crop | Suggested crop regions |

### Custom Vision
- Train custom image classifiers
- Create custom object detectors
- No ML expertise required
- Export models to edge devices

---

## Azure AI Face Service

### Operations

#### Detect
- Locate faces in an image
- Return face rectangles
- Optionally return attributes:
  - Age, emotion, glasses, hair
  - Head pose, makeup, blur
  - Exposure, noise, occlusion

**Key**: Use **Detect** to find faces and analyze attributes like sunglasses

#### Verify
- Compare two faces
- Determine if they are the same person
- Returns confidence score
- 1-to-1 matching

#### Identify
- Match a face against a person group
- 1-to-many matching
- Requires pre-registered faces

#### Find Similar
- Find faces similar to a given face
- Search within a face list
- Returns ranked matches

#### Group
- Organize faces into groups
- Based on visual similarity
- Unsupervised clustering

---

## Key Scenarios

| Scenario | Service/Operation |
|----------|-------------------|
| Check if person wearing sunglasses | Face - Detect |
| Verify employee identity | Face - Verify |
| Find all product logos | Vision - Analyze (brands) |
| Read text from document | Vision - Read (OCR) |
| Detect objects in image | Vision - Analyze (objects) |
| Count people in store | Spatial Analysis |

---

## Azure AI Document Intelligence (Form Recognizer)

### Overview
- Extract text, key-value pairs, and tables from documents
- Prebuilt models for common document types
- Custom models for specific forms

### Prebuilt Models
| Model | Use Case |
|-------|----------|
| Invoice | Extract invoice data (vendor, amounts, line items) |
| Receipt | Extract receipt data (merchant, total, items) |
| ID Document | Extract ID card/passport/driver's license data |
| Business Card | Extract contact information |
| Tax Forms | W-2, 1099, etc. |
| Health Insurance | Insurance card data |

### Extracted Information
- **Text**: Raw text from document
- **Key-Value Pairs**: Field labels and their values
- **Tables**: Structured tabular data
- **Selection Marks**: Checkboxes, radio buttons

### Custom Models
- Train with your own labeled documents
- Minimum 5 sample documents recommended
- Supports structured and unstructured forms

---

## Semantic Segmentation

- Classifies every pixel in an image
- Creates pixel-level masks
- **Use cases**: Medical imaging, autonomous vehicles, satellite imagery
- Different from object detection (bounding boxes vs. pixel masks)

---

## Key Exam Tips

- **Object Detection** returns bounding boxes with coordinates
- **Image Classification** returns a single label for entire image
- **Semantic Segmentation** classifies every pixel
- **Face Detect** operation to check for attributes (sunglasses, emotions)
- **Face Verify** for 1-to-1 comparison (two faces)
- **Face Identify** for 1-to-many matching (against person group)
- **OCR/Read API** for extracting text from images
- **Document Intelligence** extracts key-value pairs and tables
- Read API returns results organized as: Pages → Lines → Words
- Extreme angles can impair face detection
- Computer Vision ≠ Face service (different services)
