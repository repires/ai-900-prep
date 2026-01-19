# AI-900: Microsoft Azure AI Fundamentals - Exam Prep

**Live Site:** [ai900.raydev.ca](https://ai900.raydev.ca)

**Passing Score**: 700/1000 | **Duration**: 20 min check-in + 45 min test | **Questions**: ~45-50

## Features

- Practice Quiz with instant feedback
- Flashcards for key concepts
- Study notes organized by exam domain
- Official Microsoft Learn video course (8 episodes)

## Skills Measured

| Domain | Weight |
|--------|--------|
| 1. AI Workloads and Considerations | 15-20% |
| 2. Machine Learning Principles | 15-20% |
| 3. Computer Vision on Azure | 15-20% |
| 4. Natural Language Processing | 15-20% |
| 5. Generative AI Workloads | 20-25% |

## Folder Structure

```
ai-900-prep/
├── content/           # Study materials organized by domain
│   ├── 01-ai-workloads.md
│   ├── 02-machine-learning.md
│   ├── 03-computer-vision.md
│   ├── 04-nlp.md
│   └── 05-generative-ai.md
├── questions/         # Practice questions
│   └── questions.json
├── flashcards/        # Flashcard content
│   └── flashcards.json
├── app/               # Flask web application
│   ├── app.py
│   ├── templates/
│   └── static/
└── resources/         # Additional resources
```

## Run Locally

```bash
pip install flask
python app/app.py
```

Then open http://localhost:5000

## Official Resources

- [Microsoft Study Guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-900)
- [Learning Path](https://learn.microsoft.com/en-us/training/paths/introduction-to-ai-on-azure/)
- [Free Practice Assessment](https://aka.ms/examdemo)
- [Official Video Course](https://www.youtube.com/playlist?list=PLahhVEj9XNTfFP-841X_gdJ0nmjfjfCQN)

## Six Principles of Responsible AI

1. **Fairness** - AI systems should treat all people fairly
2. **Reliability & Safety** - AI systems should perform reliably and safely
3. **Privacy & Security** - AI systems should be secure and respect privacy
4. **Inclusiveness** - AI systems should empower everyone
5. **Transparency** - AI systems should be understandable
6. **Accountability** - People should be accountable for AI systems

---

Developed by Renato Pires

© 2026 Renato Pires. All rights reserved.

Licensed under the MIT License.
