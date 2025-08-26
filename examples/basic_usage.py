#!/usr/bin/env python3
"""
Basic usage example for AI Classifier Sample.

This example demonstrates how to use the single-turn message classifier
with different types of customer support messages.
"""

import json
from ai_classifier_sample.config.settings import get_settings
from ai_classifier_sample.service.classifier import MessageClassifier


def main():
    """Run basic single-turn classification examples."""
    print("🤖 AI Classifier Sample - Basic Usage Example\n")
    
    # Display current settings
    settings = get_settings()
    print("📋 Current Configuration:")
    print(f"   Cloud Region: {settings.cloud_region}")
    print(f"   Provider: {settings.provider}")
    print(f"   Max Tokens: {settings.max_tokens}")
    print(f"   Model ARN: {settings.model_arn}")
    print()
    
    # Initialize classifier
    print("🔧 Initializing classifier...")
    classifier = MessageClassifier()
    print("✅ Classifier ready!\n")
    
    # Example messages for classification
    # Categories: 'Support, Feedback, Complaint', 'Order Tracking', 'Refund/Exchange'
    messages = [
        "Hello, I need help with my account login issues",
        "Thank you so much for the excellent customer service!",
        "When will my order #12345 be delivered?",
        "I would like to return this item I bought last week",
        "Can you help me understand how to use this feature?",
        "This product is terrible, it stopped working after one day",
        "I'm having technical difficulties with the app",
        "Where is my package? I ordered it 5 days ago",
        "I want to exchange this for a different size",
        "The customer support team was very helpful today"
    ]
    
    print("🚀 Classifying messages...\n")
    
    for i, message in enumerate(messages, 1):
        print(f"Message {i}:")
        print(f"📝 Text: {message}")
        
        try:
            # Classify the message (returns JSON string)
            category_json = classifier.classify(message)
            
            # Parse the JSON response
            category_data = json.loads(category_json)
            
            print(f"🏷️  Category: {category_data['category']}")
            print(f"📄 Full Response: {category_data}")
            
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print("-" * 60)
        print()


if __name__ == "__main__":
    main()