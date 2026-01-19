# Domain 1: AI Workloads and Considerations (15-20%)

---

## 📺 Official Microsoft Learn Videos

> **Full Playlist:** <a href="https://www.youtube.com/playlist?list=PLahhVEj9XNTfFP-841X_gdJ0nmjfjfCQN" target="_blank">AI-900: Microsoft Azure AI Fundamentals</a>

### Episode 1: Course Intro (4:31)

Introduction to the AI-900 certification course and what you'll learn.

<a href="https://www.youtube.com/watch?v=0Xl-Q161RIA&list=PLahhVEj9XNTfFP-841X_gdJ0nmjfjfCQN&index=1" target="_blank">▶️ Watch Episode 1 on YouTube</a>

---

### Episode 2: AI Overview (9:39)

Overview of artificial intelligence concepts, workloads, and considerations.

<a href="https://www.youtube.com/watch?v=vQW4WtFMa1I&list=PLahhVEj9XNTfFP-841X_gdJ0nmjfjfCQN&index=2" target="_blank">▶️ Watch Episode 2 on YouTube</a>

---

### Episode 7: Fundamentals of Information Extraction (29:02)

Covers Azure AI Document Intelligence and Knowledge Mining with Azure AI Search.

<a href="https://www.youtube.com/watch?v=0Xl-Q161RIA&list=PLahhVEj9XNTfFP-841X_gdJ0nmjfjfCQN&index=7" target="_blank">▶️ Watch Episode 7 on YouTube</a>

---

### Episode 8: Course Conclusion (3:31)

Summary and next steps for the AI-900 certification exam.

<a href="https://www.youtube.com/watch?v=0Xl-Q161RIA&list=PLahhVEj9XNTfFP-841X_gdJ0nmjfjfCQN&index=8" target="_blank">▶️ Watch Episode 8 on YouTube</a>

---

## Common AI Workloads

### Computer Vision Workloads
- **Image Classification**: Categorizing images into predefined classes
- **Object Detection**: Identifying and locating objects within images
- **Facial Detection/Analysis**: Detecting faces and analyzing attributes
- **Optical Character Recognition (OCR)**: Extracting text from images

### Natural Language Processing Workloads
- **Text Analysis**: Extracting insights from text
- **Sentiment Analysis**: Determining positive/negative/neutral sentiment
- **Language Translation**: Converting text between languages
- **Speech Recognition/Synthesis**: Converting speech to text and vice versa

### Document Processing Workloads
- **Form Recognition**: Extracting data from forms and documents
- **Invoice Processing**: Automated invoice data extraction
- **Receipt Processing**: Extracting data from receipts

### Generative AI Workloads
- **Text Generation**: Creating human-like text content
- **Code Generation**: Generating programming code
- **Image Generation**: Creating images from descriptions
- **Content Summarization**: Condensing long content

---

## Six Principles of Responsible AI

### 1. Fairness
- AI systems should treat all people fairly
- Avoid bias based on gender, race, religion, or other factors
- Use diverse training data
- Regular bias auditing

**Example**: A loan approval AI should not discriminate based on gender or race

### 2. Reliability and Safety
- Systems should perform consistently and safely
- Handle unexpected situations gracefully
- Resist manipulation
- Continuous monitoring and testing

**Example**: An autonomous vehicle AI must respond safely to unexpected road conditions

### 3. Privacy and Security
- Protect personal data
- Comply with privacy regulations
- Secure data storage and transmission
- Transparent data collection practices

**Example**: A health AI must protect patient medical records

### 4. Inclusiveness
- AI should empower everyone
- Consider people with disabilities
- Design for diverse human experiences
- Use accessible technologies (speech-to-text, text-to-speech)

**Example**: Voice recognition should work for people with different accents

### 5. Transparency
- AI systems should be understandable
- Explain how decisions are made
- Document algorithms and data used
- Enable model interpretability

**Example**: A credit scoring AI should explain why an application was denied

### 6. Accountability
- People should be accountable for AI systems
- Establish governance frameworks
- Define clear roles and responsibilities
- Maintain audit trails

**Example**: Organizations must have processes to address AI system failures

---

## Azure AI Resource Types

### Multi-Service Resource (Azure AI Services)
- Single resource for multiple AI services
- One endpoint and key for all services
- Simplified management
- **Use when**: Need multiple services with convenience

### Single-Service Resource
- Dedicated resource per service
- Separate billing and tracking
- Independent scaling
- **Use when**: Need individual cost visibility

### Common Resources
| Resource Type | Services Included |
|--------------|-------------------|
| Azure AI Services | Vision, Language, Speech, etc. |
| Azure OpenAI | GPT, DALL-E, Whisper |
| Azure AI Search | Search and indexing |
| Azure Machine Learning | ML training and deployment |

---

## Knowledge Mining

### What is Knowledge Mining?
- Extract insights from unstructured data
- Documents, images, audio, video
- Make data searchable and actionable

### Azure AI Search
- Core service for knowledge mining
- Indexes content from various sources
- AI enrichment pipeline (skillsets)
- Supports: JSON, Cosmos DB, SQL, Blob Storage

### AI Enrichment Skills
- OCR for images
- Entity recognition
- Key phrase extraction
- Language detection
- Sentiment analysis
- Custom skills

---

## Anomaly Detection

### Use Cases
- Fraud detection in transactions
- Network intrusion detection
- Equipment failure prediction
- Unusual patterns in time-series data

### Azure Anomaly Detector
- Detects anomalies in time-series data
- Batch and real-time detection
- No ML expertise required

---

## Key Exam Tips

- **Webchat bots** reduce workload for customer service agents
- **Anomaly detection** identifies fraudulent transactions, network intrusions, abnormal patterns
- **Knowledge mining** extracts insights from unstructured data
- **Azure AI services resource** = multi-service, one key/endpoint
- **Single-service resource** = individual cost tracking
- When asked about "empowering everyone including people with disabilities" = **Inclusiveness**
- When asked about "explainable decisions" = **Transparency**
- When asked about "consistent performance under unexpected conditions" = **Reliability and Safety**
- When asked about "avoiding bias" = **Fairness**
- When asked about "protecting personal data" = **Privacy and Security**
- When asked about "humans responsible for AI" = **Accountability**
