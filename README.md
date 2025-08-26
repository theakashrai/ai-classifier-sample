# AI Classifier Sample

A message classification service using AI models with provider-agnostic configuration.

## Features

- Message classification using AI models (currently supports AWS Bedrock Claude)
- Configuration management with Pydantic Settings
- Environment variable support
- LRU cached singleton settings for optimal performance
- Cloud provider profile support

## Configuration

The application uses environment variables for configuration. You can set these in your environment or create a `.env` file:

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `CLOUD_REGION` | Cloud provider region for AI service | `us-east-1` |
| `CLOUD_PROFILE` | Cloud provider profile to use for authentication | `None` |
| `MODEL_ARN` | AI model ARN or identifier | `arn:aws:bedrock:us-east-1:123456789:inference-profile/us.anthropic.claude-sonnet-4-20250514-v1:0` |
| `MAX_TOKENS` | Maximum tokens for AI model responses | `5000` |
| `PROVIDER` | AI service provider type | `aws` |

### Example `.env` file

```bash
# Cloud Provider Configuration
CLOUD_REGION=us-west-1
CLOUD_PROFILE=my-cloud-profile

# AI Model Configuration
MODEL_ARN=arn:aws:bedrock:us-east-1:123456789:inference-profile/us.anthropic.claude-sonnet-4-20250514-v1:0
MAX_TOKENS=5000
PROVIDER=aws
```

## Installation

1. Install dependencies:

```bash
poetry install
```

## Usage

### Basic Usage

```python
from ai_classifier_sample.service.classifier import MessageClassifier

# Initialize classifier (uses cached settings)
classifier = MessageClassifier()

# Classify a message
message = "Hello, how are you?"
category = classifier.classify(message)
print(f"Message: {message}\nCategory: {category}")
```

### Settings Management

```python
from ai_classifier_sample.config.settings import get_settings

# Get cached settings instance
settings = get_settings()
print(f"Cloud Region: {settings.cloud_region}")
print(f"Model ARN: {settings.model_arn}")
```

## Testing

Run the tests using pytest:

```bash
# Run all tests
poetry run pytest

# Run tests with verbose output
poetry run pytest -v

# Run specific test file
poetry run pytest tests/test_settings.py

# Run legacy test script directly
poetry run python tests/test_settings.py
```

## Architecture

- **Settings**: Pydantic Settings with LRU cache for singleton pattern
- **Classifier**: Message classification service using AI models
- **Environment Variables**: Full support for configuration via environment variables
- **Cloud Provider Profile**: Automatic cloud provider profile setting when specified
