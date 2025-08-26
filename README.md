# 🤖 AI Classifier Sample

[![Python 3.13+](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/badge/dependency%20manager-poetry-blue.svg)](https://python-poetry.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A clean, provider-agnostic message classification service using AI models. Built with modern Python practices, featuring robust configuration management and optimized performance through intelligent caching.

## ✨ Features

- **🤖 Dual Classification Modes**: Both single-turn and multi-turn conversational classification
- **💬 Context-Aware**: Tracks conversation state and intent transitions across multiple turns  
- **📊 Rich Output**: Detailed responses including intent, confidence, reasoning, and transitions
- **☁️ Provider Agnostic**: Currently supports AWS Bedrock Claude with extensible architecture
- **⚙️ Smart Configuration**: Pydantic Settings with environment variable support
- **🚀 High Performance**: LRU cached singleton settings for optimal performance
- **🔐 Secure Authentication**: Cloud provider profile support for secure access
- **📦 Modern Python**: Built with Python 3.13+ and Poetry dependency management

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/theakashrai/ai-classifier-sample.git
cd ai-classifier-sample

# Install with Poetry
poetry install

# Or install with pip
pip install ai-classifier-sample
```

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

## ⚙️ Configuration

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

## 🎯 Usage Examples

### Basic Classification

```python
import json
from ai_classifier_sample.service.classifier import MessageClassifier

# Initialize classifier (uses cached settings)
classifier = MessageClassifier()

# Single-turn classification
message = "Hello, how are you?"
result = classifier.classify(message)

# Parse JSON response
response_data = json.loads(result)
print(f"Message: {response_data['message']}")
print(f"Category: {response_data['category']}")
```

### Conversational Classification

```python
from ai_classifier_sample.service.classifier import MessageClassifier, ConversationState

# Initialize classifier and conversation state
classifier = MessageClassifier()
conversation_state = ConversationState()

# Multi-turn conversation
messages = [
    "Hi, I need help with my order",
    "I placed it last week but haven't received tracking info",
    "The order number is #12345"
]

for message in messages:
    response = classifier.classify_conversational(message, conversation_state)
    print(f"Intent: {response.intent}")
    print(f"Transition: {response.intent_transition}")
    print(f"Confidence: {response.confidence}")
```

### Settings Management

```python
from ai_classifier_sample.config.settings import get_settings

# Get cached settings instance
settings = get_settings()
print(f"☁️  Cloud Region: {settings.cloud_region}")
print(f"🤖 Model ARN: {settings.model_arn}")
print(f"🔧 Max Tokens: {settings.max_tokens}")
```

## 🧪 Testing

Run the tests using pytest:

```bash
# Run all tests
poetry run pytest

# Run tests with verbose output
poetry run pytest -v

# Run specific test file
poetry run pytest tests/test_settings.py

# Run with coverage
poetry run pytest --cov=ai_classifier_sample --cov-report=html

# Run legacy test script directly
poetry run python tests/test_settings.py
```

## 🏗️ Architecture

- **⚙️ Settings**: Pydantic Settings with LRU cache for singleton pattern
- **🤖 Classifier**: Message classification service using AI models  
- **🌍 Environment Variables**: Full support for configuration via environment variables
- **🔐 Cloud Provider Profile**: Automatic cloud provider profile setting when specified
- **📦 Modern Dependencies**: Poetry for dependency management and virtual environments

## 🔧 Development

### Setting up for Development

```bash
# Clone the repository
git clone https://github.com/theakashrai/ai-classifier-sample.git
cd ai-classifier-sample

# Install development dependencies
poetry install --with dev

# Install pre-commit hooks
poetry run pre-commit install
```

### Code Quality

```bash
# Format code
poetry run black .
poetry run isort .

# Remove unused imports
poetry run autoflake --remove-all-unused-imports --recursive --in-place .

# Run linting
poetry run flake8 .

# Type checking (if mypy is added)
# poetry run mypy src/
```

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=ai_classifier_sample --cov-report=html

# Run specific test categories
poetry run pytest -m unit
poetry run pytest -m integration
```

## 🛠️ Supported AI Providers

### AWS Bedrock

Currently supported with Claude models:

- **Claude 4**: Next-generation model with advanced capabilities
- **Claude 3.5 Sonnet**: Latest and most capable model with enhanced reasoning
- **Claude 3.5 Haiku**: Fast, cost-effective option with improved performance
- **Claude 3 Sonnet**: Balanced performance and speed
- **Claude 3 Haiku**: Ultra-fast and lightweight for simple tasks
- **Claude 3 Opus**: Maximum performance for complex reasoning tasks

### Adding New Providers

The architecture is designed to be extensible. To add a new provider:

1. Create a new provider class in `src/ai_classifier_sample/providers/`
2. Implement the required interface methods
3. Update the configuration settings
4. Add provider-specific tests

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Workflow

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes and add tests
4. Run the test suite (`poetry run pytest`)
5. Run code quality checks (`poetry run black . && poetry run flake8 .`)
6. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
7. Push to the branch (`git push origin feature/AmazingFeature`)
8. Open a Pull Request

### Code Standards

- Follow PEP 8 style guidelines
- Use type hints for all function signatures
- Write comprehensive tests for new features
- Document public APIs with docstrings
- Keep commits atomic and well-described

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔧 Dependencies

### Core Dependencies

- **boto3**: AWS SDK for Python
- **langchain-aws**: LangChain AWS integration
- **langgraph**: Graph-based AI workflows
- **langchain**: Framework for developing LLM applications
- **pydantic-settings**: Settings management with validation

### Development Dependencies

- **black**: Code formatting
- **flake8**: Linting and style checking
- **pytest**: Testing framework
- **pre-commit**: Git hooks for code quality
- **isort**: Import sorting
- **autoflake**: Unused import removal

## 🎯 Why This Tool?

### Clean Architecture

- ✅ Provider-agnostic design for future extensibility
- ✅ Separation of concerns with clear module boundaries
- ✅ Configuration management with validation
- ✅ Performance optimization through intelligent caching

### Developer Experience

- ✅ Modern Python 3.13+ with type hints
- ✅ Poetry for reliable dependency management
- ✅ Comprehensive testing with pytest
- ✅ Code quality tools integrated
- ✅ Clear documentation and examples

### Production Ready

- ✅ Environment-based configuration
- ✅ Secure cloud provider authentication
- ✅ Error handling and logging
- ✅ Extensible architecture for scaling

---

Built with ❤️ using modern Python practices
