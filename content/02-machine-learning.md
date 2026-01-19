# Domain 2: Machine Learning Principles on Azure (15-20%)

---

## 📺 Official Microsoft Learn Video

> **Full Playlist:** <a href="https://www.youtube.com/playlist?list=PLahhVEj9XNTfFP-841X_gdJ0nmjfjfCQN" target="_blank">AI-900: Microsoft Azure AI Fundamentals</a>

### Episode 3: Fundamentals of Machine Learning (32:58)

Comprehensive coverage of machine learning principles, techniques, and Azure Machine Learning capabilities.

<a href="https://www.youtube.com/watch?v=9XwjX1FQ7p4&list=PLahhVEj9XNTfFP-841X_gdJ0nmjfjfCQN&index=3" target="_blank">▶️ Watch Episode 3 on YouTube</a>

---

## Machine Learning Techniques

### Regression
- **Purpose**: Predict continuous numeric values
- **Output**: A number (price, temperature, quantity)
- **Examples**:
  - Predicting house prices
  - Forecasting sales revenue
  - Estimating delivery times

### Classification
- **Purpose**: Predict categorical labels
- **Output**: A category/class
- **Types**:
  - **Binary**: Two classes (yes/no, spam/not spam)
  - **Multi-class**: Multiple classes (animal type, product category)
- **Examples**:
  - Email spam detection
  - Disease diagnosis
  - Customer churn prediction

### Clustering
- **Purpose**: Group similar data points
- **Output**: Groups/clusters (unsupervised - no labels)
- **Examples**:
  - Customer segmentation
  - Document grouping
  - Anomaly detection

---

## Core ML Concepts

### Features and Labels
- **Features**: Input variables used to make predictions (X)
- **Labels**: Output variable being predicted (Y)

**Example**: Predicting house price
- Features: Size, bedrooms, location, age
- Label: Price

### Training and Validation Datasets
- **Training Data**: Used to train the model (typically 70-80%)
- **Validation/Test Data**: Used to evaluate model performance (typically 20-30%)
- **Split**: Random split of rows, NOT columns

### Confusion Matrix
```
                    Predicted
                    Positive    Negative
Actual  Positive      TP          FN
        Negative      FP          TN
```
- **TP (True Positive)**: Correctly predicted positive
- **TN (True Negative)**: Correctly predicted negative
- **FP (False Positive)**: Incorrectly predicted positive (Type I error)
- **FN (False Negative)**: Incorrectly predicted negative (Type II error)

---

## Deep Learning

### Neural Networks
- Inspired by biological neurons
- Multiple layers of interconnected nodes
- Can learn complex patterns
- Requires large amounts of data

### Transformer Architecture
- Foundation for modern LLMs
- Uses attention mechanisms
- Processes sequences in parallel
- Powers GPT, BERT, and similar models

---

## Azure Machine Learning Capabilities

### Automated ML (AutoML)
- Automatically selects algorithms
- Tunes hyperparameters
- Compares model performance
- Reduces time to develop models

**Key Feature**: "Explain best model" enables transparency principle

### Azure ML Compute
- **Compute Instances**: Development VMs
- **Compute Clusters**: Scalable training compute
- **Inference Clusters**: Model deployment
- **Attached Compute**: Link external resources

### Model Management
- **Model Registry**: Version and track models
- **Datasets**: Manage training data
- **Pipelines**: Automate ML workflows
- **Endpoints**: Deploy models as services

---

## ML Pipeline Steps (In Order)

1. **Prepare Data**: Clean and transform data
2. **Train Model**: Fit model to training data
3. **Evaluate Model**: Assess model performance
4. **Deploy Model**: Make model available as a service

---

## Evaluation Metrics

### Regression Metrics
| Metric | Description | Goal |
|--------|-------------|------|
| R² (R-squared) | Proportion of variance explained | Higher (0-1) |
| RMSE | Root Mean Squared Error | Lower |
| MAE | Mean Absolute Error | Lower |
| MSE | Mean Squared Error | Lower |

### Classification Metrics
| Metric | Formula | Description |
|--------|---------|-------------|
| Accuracy | (TP+TN) / Total | Overall correctness |
| Precision | TP / (TP+FP) | Of predicted positive, how many correct? |
| Recall | TP / (TP+FN) | Of actual positive, how many found? |
| F1 Score | 2×(P×R)/(P+R) | Balance of precision and recall |
| AUC | Area under ROC | Model discrimination ability (0.5-1) |

### Clustering Metrics
- **Silhouette Score**: Measures cluster cohesion (-1 to 1, higher is better)
- **Inertia**: Within-cluster sum of squares (lower is better)

---

## Azure ML Designer

### Key Components
- **Datasets**: Data sources you drag onto canvas
- **Modules**: Processing steps (transform, train, evaluate)
- **Pipelines**: Connected workflows of modules

### Common Modules
| Module | Purpose |
|--------|---------|
| Split Data | Divide into training/test sets |
| Train Model | Fit model to training data |
| Score Model | Generate predictions |
| Evaluate Model | Calculate metrics |
| Select Columns | Choose specific columns |
| Clean Missing Data | Handle null values |
| Normalize Data | Scale features |

### Languages Supported
- Python (Execute Python Script module)
- R (Execute R Script module)

### Deployment
- Published pipelines provide **REST endpoint** + **Authentication key**
- Real-time inference requires Azure Kubernetes Service (AKS)
- Batch inference uses compute clusters

---

## Key Exam Tips

- Data should be split into **rows** for training/evaluation, NOT columns
- **Features** = inputs, **Labels** = outputs
- **Regression** = numeric output (R², RMSE, MAE)
- **Classification** = categorical output (Precision, Recall, F1, AUC)
- **Clustering** = grouping with no labels (Silhouette score)
- AutoML's "Explain best model" = **Transparency principle**
- Precision/Recall/F1/AUC = Classification metrics
- R²/RMSE/MAE = Regression metrics
- To access published pipeline: REST endpoint + Primary Key
