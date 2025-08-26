# AI Classifier Sample Examples

This directory contains example scripts demonstrating how to use the AI Classifier Sample package for both single-turn and multi-turn conversational message classification.

## Examples

### 1. Basic Usage (`basic_usage.py`)

Demonstrates single-turn message classification:

- Loading configuration settings
- Initializing the classifier
- Classifying customer support messages into categories
- Parsing JSON responses from the classifier
- Basic error handling

**Categories**: 'Support, Feedback, Complaint', 'Order Tracking', 'Refund/Exchange'

Run with:

```bash
poetry run python examples/basic_usage.py
```

### 2. Advanced Usage (`advanced_usage.py`)

Shows conversational classification and advanced features:

- Multi-turn conversational classification with context tracking
- Conversation state management
- Intent transitions (CONTINUE, NEW, CLARIFICATION)
- Comparison between single-turn vs conversational classification
- Settings management and caching
- Environment variable configuration

Run with:

```bash
poetry run python examples/advanced_usage.py
```

### 3. Complete Example (`complete_example.py`)

Replicates the exact functionality from `main.py` and demonstrates:

- Both single-turn and multi-turn classification
- Conversation state tracking across multiple turns
- Intent resolution and transition detection
- Realistic customer support conversation scenarios
- Comprehensive error handling and troubleshooting tips

Run with:

```bash
poetry run python examples/complete_example.py
```

## Prerequisites

Before running the examples, make sure you have:

1. **Installed dependencies**:

   ```bash
   poetry install
   ```

2. **AWS credentials configured** (for AWS Bedrock):
   - AWS CLI configured: `aws configure`
   - Or environment variables set
   - Or IAM role attached (for EC2/Lambda)

3. **Environment variables set** (optional):

   ```bash
   export CLOUD_REGION=us-east-1
   export CLOUD_PROFILE=your-profile
   export MODEL_ARN=your-model-arn
   ```

## Expected Output

The examples will show:

- ✅ Successful classifications with categories
- ❌ Error messages for invalid configurations
- 📋 Current configuration details
- 💡 Tips and recommendations

## Troubleshooting

Common issues and solutions:

1. **AWS Credentials Error**:
   - Ensure AWS credentials are properly configured
   - Check that your profile has access to Bedrock

2. **Model Not Found**:
   - Verify the MODEL_ARN is correct for your region
   - Ensure you have access to the specified model

3. **Region Issues**:
   - Make sure Bedrock is available in your specified region
   - Check that your model is available in that region

For more information, see the main [README](../README.md).
