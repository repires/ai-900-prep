# Domain 4: Natural Language Processing on Azure (15-20%)

---

## 📺 Official Microsoft Learn Video

> **Full Playlist:** <a href="https://www.youtube.com/playlist?list=PLahhVEj9XNTfFP-841X_gdJ0nmjfjfCQN" target="_blank">AI-900: Microsoft Azure AI Fundamentals</a>

### Episode 5: Fundamentals of Natural Language Processing (31:05)

Covers NLP fundamentals and Azure capabilities including text analysis, question answering, conversational language understanding with Language Studio, and Speech Studio features.

<a href="https://www.youtube.com/watch?v=0Xl-Q161RIA&list=PLahhVEj9XNTfFP-841X_gdJ0nmjfjfCQN&index=5" target="_blank">▶️ Watch Episode 5 on YouTube</a>

**Key Topics:**
- Text analysis using Azure AI Language
- Question answering model implementation
- Conversational Language Understanding with Language Studio
- Speech Studio features and capabilities

---

## NLP Workload Scenarios

### Key Phrase Extraction
- Identifies main concepts in text
- Extracts important terms and phrases
- **Example**: "The food was delicious and the staff was friendly" → "food", "staff"

### Entity Recognition (NER)
- Identifies and categorizes named entities
- **Categories**: Person, Location, Organization, Date, Quantity, etc.
- **Example**: "Microsoft was founded by Bill Gates in Seattle" → Microsoft (Org), Bill Gates (Person), Seattle (Location)

### Sentiment Analysis
- Determines emotional tone of text
- **Output**: Positive, Negative, Neutral (with confidence scores)
- **Use cases**: Customer reviews, social media monitoring, feedback analysis

### Language Detection
- Identifies the language of text
- Returns language code and confidence score
- Supports 100+ languages

### Language Modeling
- Understanding and generating language
- Predicting next words
- Foundation for chatbots and assistants

### Speech Recognition
- Converts spoken audio to text (Speech-to-Text)
- Real-time or batch processing
- Custom speech models available

### Speech Synthesis
- Converts text to spoken audio (Text-to-Speech)
- Multiple voices and languages
- Neural voices for natural sound

### Translation
- **Text Translation**: Convert text between languages
- **Document Translation**: Translate entire documents
- **Speech Translation**: Real-time speech translation

---

## Azure AI Language Service

### Core Features

| Feature | Description |
|---------|-------------|
| Sentiment Analysis | Positive/negative/neutral with scores |
| Key Phrase Extraction | Main concepts from text |
| Named Entity Recognition | People, places, organizations, etc. |
| Entity Linking | Links entities to Wikipedia |
| Language Detection | Identify text language |
| PII Detection | Find personal information |
| Text Summarization | Generate concise summaries |

### Custom Features
- **Custom Text Classification**: Train custom categorizers
- **Custom NER**: Train custom entity extractors
- **Conversational Language Understanding (CLU)**: Build custom intent/entity models

### Question Answering
- Build FAQ bots from existing content
- Import from URLs, documents, or manual entry
- Multi-turn conversations
- Active learning for improvement

---

## Azure AI Speech Service

### Speech-to-Text
- Real-time transcription
- Batch transcription for files
- Custom speech models
- Speaker diarization (who said what)

### Text-to-Speech
- Neural voices (natural sounding)
- Standard voices
- Custom voice creation
- SSML for fine control

### Speech Translation
- Real-time translation
- Multiple target languages
- Audio-to-audio translation

### Key Features
| Feature | Use Case |
|---------|----------|
| Real-time STT | Live captioning |
| Batch STT | Transcribe recordings |
| Custom Speech | Domain-specific vocabulary |
| Neural TTS | Natural voice assistants |
| Speaker Recognition | Identify who is speaking |

---

## Azure AI Translator

### Text Translation
- 100+ languages supported
- Auto language detection
- Dictionary lookups
- Transliteration

### Document Translation
- Preserve document formatting
- Batch processing
- Supported formats: PDF, DOCX, PPTX, etc.

### Custom Translator
- Train custom translation models
- Domain-specific terminology
- Use your parallel data

---

## Conversational Language Understanding (CLU)

### Core Concepts

#### Intents
- What the user wants to do
- **Examples**: GetWeather, BookFlight, OrderPizza
- Each app has a "None" intent for unrecognized requests

#### Entities
- Key information extracted from utterances
- **Examples**: City, Date, ProductName
- Types: Prebuilt, List, Machine-learned

#### Utterances
- Example phrases users might say
- Used to train the model
- Label intents and entities in utterances

### Example
**Intent**: GetTime
**Entity**: city
**Utterances**:
- "What time is it in **London**?"
- "Tell me the time in **Tokyo**"
- "Current time **New York**"

### Workflow
1. Create Language resource
2. Define intents and entities
3. Add and label utterances
4. Train the model
5. Test and iterate
6. Publish for prediction
7. Use prediction endpoint + key in your app

---

## Question Answering

### Knowledge Base Creation
- Import from URLs (FAQ pages)
- Import from files (PDF, Word, Excel)
- Manual entry of Q&A pairs
- Add chitchat personality

### Features
- Multi-turn conversations
- Synonyms and alternatives
- Active learning suggestions
- Metadata filtering

---

## Key Exam Tips

- **Sentiment Analysis** = positive/negative/neutral tone (highest confidence wins)
- **Key Phrase Extraction** = main concepts/topics
- **Named Entity Recognition** = people, places, organizations
- **Language Detection** = identify which language (NaN if ambiguous)
- **Azure AI Language** service handles text analysis
- **Azure AI Speech** service handles audio
- **Speech-to-Text** = recognition
- **Text-to-Speech** = synthesis
- **CLU Intent** = what user wants to do
- **CLU Entity** = key information to extract
- After publishing CLU: need **prediction endpoint + key**
- Question Answering can import FAQs directly
- NLP is used for: sentiment analysis, topic detection, language detection, key phrase extraction, document categorization
