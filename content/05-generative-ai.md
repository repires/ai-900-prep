# Domain 5: Generative AI Workloads on Azure (20-25%)

**Note**: This is the largest domain (20-25%) - study thoroughly!

---

## 📺 Official Microsoft Learn Video

> **Full Playlist:** <a href="https://www.youtube.com/playlist?list=PLahhVEj9XNTfFP-841X_gdJ0nmjfjfCQN" target="_blank">AI-900: Microsoft Azure AI Fundamentals</a>

### Episode 4: Fundamentals of Generative AI (36:44)

Covers generative AI fundamentals including Microsoft Copilot, Azure AI Studio, and responsible AI practices.

<a href="https://www.youtube.com/watch?v=w8dnKQ24vdk&list=PLahhVEj9XNTfFP-841X_gdJ0nmjfjfCQN&index=4" target="_blank">▶️ Watch Episode 4 on YouTube</a>

**Key Topics Covered:**
- Generative AI core concepts and principles
- Large Language Models (LLMs) and transformers
- Practical exploration of Microsoft Copilot
- Azure AI Studio platform introduction
- Responsible AI practices for generative AI

---

## Generative AI Fundamentals

### What is Generative AI?
- AI that creates new content
- Based on patterns learned from training data
- Can generate text, images, code, audio, video

### Large Language Models (LLMs)
- Trained on massive text datasets
- Understand and generate human-like text
- Examples: GPT-4, Claude, Gemini

### Transformer Architecture
- Foundation of modern LLMs
- Uses attention mechanisms
- Processes sequences in parallel
- Enables understanding of context

---

## Common Generative AI Scenarios

| Scenario | Description |
|----------|-------------|
| Text Generation | Creating articles, emails, stories |
| Code Generation | Writing and explaining code |
| Summarization | Condensing long content |
| Translation | Converting between languages |
| Q&A | Answering questions based on context |
| Chat/Conversation | Interactive dialogue |
| Image Generation | Creating images from descriptions |
| Content Editing | Rewriting, improving text |

---

## Responsible AI for Generative AI

### Key Considerations

1. **Harmful Content**
   - Prevent generation of violent, hateful, or illegal content
   - Content filtering systems
   - Safety classifiers

2. **Hallucinations**
   - AI generating false information
   - Grounding with verified sources
   - Retrieval-Augmented Generation (RAG)

3. **Bias**
   - Models may reflect biases in training data
   - Regular evaluation and mitigation
   - Diverse training datasets

4. **Intellectual Property**
   - Copyright concerns with generated content
   - Transparency about AI-generated content
   - Proper attribution

5. **Privacy**
   - Avoid exposing personal information
   - Data handling policies
   - User consent

---

## Azure AI Foundry (formerly Azure AI Studio)

### Overview
- Unified platform for building AI solutions
- Combines multiple Azure AI services
- End-to-end development experience

### Capabilities
| Feature | Description |
|---------|-------------|
| Model Catalog | Browse and deploy AI models |
| Playgrounds | Test models interactively |
| Prompt Flow | Design and test prompts |
| Evaluation | Assess model performance |
| Deployment | Deploy to production |
| Monitoring | Track usage and performance |

### Model Catalog
- Access to OpenAI models (GPT-4, DALL-E)
- Open-source models (Llama, Mistral)
- Microsoft models (Phi)
- Fine-tuned models

---

## Azure OpenAI Service

### Available Models

| Model Family | Use Cases |
|--------------|-----------|
| GPT-4 / GPT-4o | Complex reasoning, analysis, code |
| GPT-3.5 Turbo | General chat, simpler tasks |
| DALL-E | Image generation |
| Whisper | Speech-to-text |
| Embeddings | Text similarity, search |

### Key Features
- **Chat Completions**: Conversational AI
- **Completions**: Text generation
- **Embeddings**: Vector representations
- **Image Generation**: Create images from text

### Deployment Options
- **Standard**: Shared capacity, pay-per-use
- **Provisioned**: Dedicated capacity, predictable performance

### Content Filtering
- Built-in safety systems
- Filters for: hate, violence, sexual content, self-harm
- Configurable severity levels
- Block or flag content

---

## Prompt Engineering

### What is Prompting?
- Crafting inputs to get desired outputs
- Context + instructions = better results

### Prompt Techniques

| Technique | Description |
|-----------|-------------|
| Zero-shot | Direct question, no examples |
| Few-shot | Provide examples in prompt |
| Chain-of-thought | Ask model to explain reasoning |
| System messages | Set context and persona |

### Best Practices
1. Be specific and clear
2. Provide context
3. Give examples when helpful
4. Specify output format
5. Iterate and refine

---

## Retrieval-Augmented Generation (RAG)

### What is RAG?
- Combines LLM with external knowledge
- Retrieves relevant documents
- Grounds responses in facts
- Reduces hallucinations

### RAG Components
1. **Document Store**: Your knowledge base
2. **Retrieval**: Find relevant documents
3. **Generation**: LLM creates response using retrieved context

---

## Azure OpenAI Parameters

### Temperature
- Controls randomness/creativity
- **Range**: 0 to 2 (typically 0-1)
- **Low (0-0.3)**: Focused, deterministic, factual
- **High (0.7-1)**: Creative, diverse, varied
- **Use low for**: Code, facts, analysis
- **Use high for**: Creative writing, brainstorming

### Top_p (Nucleus Sampling)
- Alternative to temperature
- Controls token selection probability
- **Range**: 0 to 1
- Lower = more focused, higher = more diverse
- Usually adjust temperature OR top_p, not both

### Max Tokens
- Maximum length of response
- Limits output to prevent runaway generation
- Includes both prompt and completion tokens

### Presence/Frequency Penalty
- **Presence Penalty**: Reduces repetition of topics
- **Frequency Penalty**: Reduces repetition of words
- Range: -2 to 2 (0 = neutral)

---

## Tokens

### What are Tokens?
- Basic units LLMs process
- Can be words, parts of words, or punctuation
- English: ~1 token per 4 characters
- Pricing based on tokens (input + output)

### Token Limits
- Models have context length limits
- GPT-4: 8K-128K tokens depending on version
- Includes: system message + conversation history + prompt + response

---

## Embeddings

### What are Embeddings?
- Numeric vector representations of text
- Capture semantic meaning
- Similar meanings = similar vectors

### Use Cases
- Semantic search
- Recommendation systems
- Clustering similar documents
- RAG retrieval

---

## Copilots

### What is a Copilot?
- AI assistant embedded in applications
- Helps users complete tasks
- Uses natural language interaction

### Microsoft Copilots
- **Microsoft 365 Copilot**: Word, Excel, PowerPoint, Outlook
- **GitHub Copilot**: Code completion and generation
- **Power Platform Copilot**: App and automation building
- **Windows Copilot**: OS assistance

---

## Azure AI Search (for RAG)

### Role in RAG
- Indexes your documents
- Provides semantic search
- Retrieves relevant context for LLM

### Features
- Vector search (embeddings)
- Hybrid search (keyword + semantic)
- AI enrichment (skills pipeline)
- Data format: JSON

---

## Key Exam Tips

- **Azure AI Foundry** = unified platform for AI development
- **Azure OpenAI Service** = access to GPT, DALL-E, Whisper
- **Model Catalog** = browse and deploy models from various providers
- **Prompt engineering** = crafting effective inputs
- **RAG** = grounding AI with external knowledge to reduce hallucinations
- **Content filtering** = built-in safety for Azure OpenAI
- **Hallucinations** = AI generating false/fabricated information
- **Temperature** = controls randomness (low=focused, high=creative)
- **Tokens** = basic units of text LLMs process
- **Embeddings** = vector representations for similarity search
- **System message** = defines AI behavior and persona
- **Grounding** = providing context to improve accuracy
- **Copilot** = AI assistant integrated into applications
- Azure OpenAI advantage: enterprise security, compliance, private networking
- This domain is 20-25% of exam - largest section!
