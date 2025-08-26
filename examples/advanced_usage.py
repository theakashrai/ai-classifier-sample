#!/usr/bin/env python3
"""
Advanced usage example for AI Classifier Sample.

This example demonstrates the conversational classification features,
showing how the classifier can track context across multiple turns
in a customer support conversation.
"""

import os
import json
from ai_classifier_sample.config.settings import get_settings
from ai_classifier_sample.service.classifier import MessageClassifier, ConversationState


def demo_conversational_classification():
    """Demonstrate multi-turn conversational classification."""
    print("💬 Conversational Classification Demo\n")
    
    classifier = MessageClassifier()
    conversation_state = ConversationState()
    
    # Simulate a realistic customer support conversation
    conversation_turns = [
        "Hi, I need help with my recent order",
        "I placed it last week but haven't received any tracking information",
        "The order number is #12345",
        "Actually, I also want to return another item I bought last month",
        "It doesn't fit properly and I'd like to exchange it for a larger size",
        "Thank you for your help, the support team has been very responsive"
    ]
    
    print("� Starting conversation simulation...\n")
    
    for turn_num, message in enumerate(conversation_turns, 1):
        print(f"Turn {turn_num}: {message}")
        
        try:
            # Classify within conversational context
            conv_response = classifier.classify_conversational(message, conversation_state)
            
            print(f"   🎯 Intent: {conv_response.intent}")
            print(f"   🔄 Transition: {conv_response.intent_transition}")
            print(f"   🎚️  Confidence: {conv_response.confidence}")
            print(f"   🧠 Reasoning: {conv_response.reasoning}")
            print(f"   📊 Current State Intent: {conversation_state.current_intent}")
            print(f"   ✅ Resolved Intents: {conversation_state.resolved_intents}")
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        print("-" * 60)
        print()
    
    print(f"🏁 Conversation completed!")
    print(f"   Final Intent: {conversation_state.current_intent}")
    print(f"   Total Resolved Intents: {conversation_state.resolved_intents}")
    print(f"   Total Turns: {len(conversation_state.conversation_history)}")


def demo_single_vs_conversational():
    """Compare single-turn vs conversational classification."""
    print("⚖️ Single-turn vs Conversational Comparison\n")
    
    classifier = MessageClassifier()
    
    # Test message that could be ambiguous without context
    test_message = "Can you help me with the return process?"
    
    print(f"Test message: '{test_message}'\n")
    
    # Single-turn classification
    print("📝 Single-turn classification:")
    try:
        single_result = classifier.classify(test_message)
        single_data = json.loads(single_result)
        print(f"   Category: {single_data['category']}")
    except Exception as e:
        print(f"   Error: {e}")
    
    print()
    
    # Conversational classification with context
    print("💬 Conversational classification with context:")
    conversation_state = ConversationState()
    
    # Add some context first
    context_messages = [
        "I received my order yesterday",
        "The quality is not what I expected"
    ]
    
    print("   Setting up context:")
    for msg in context_messages:
        print(f"      '{msg}'")
        try:
            classifier.classify_conversational(msg, conversation_state)
        except Exception as e:
            print(f"      Error: {e}")
    
    print(f"\n   Now classifying: '{test_message}'")
    try:
        conv_result = classifier.classify_conversational(test_message, conversation_state)
        print(f"   Intent: {conv_result.intent}")
        print(f"   Transition: {conv_result.intent_transition}")
        print(f"   Reasoning: {conv_result.reasoning}")
    except Exception as e:
        print(f"   Error: {e}")


def demo_settings_management():
    """Demonstrate settings management features."""
    print("⚙️ Settings Management Demo\n")
    
    # Get the singleton settings instance
    settings = get_settings()
    
    print("📋 Current Settings:")
    print(f"   Cloud Region: {settings.cloud_region}")
    print(f"   Cloud Profile: {settings.cloud_profile}")
    print(f"   Model ARN: {settings.model_arn}")
    print(f"   Max Tokens: {settings.max_tokens}")
    print(f"   Provider: {settings.provider}")
    print()
    
    # Settings are cached - getting them again returns the same instance
    settings2 = get_settings()
    print(f"✅ Settings are cached: {settings is settings2}")
    print()


def demo_environment_variables():
    """Show how environment variables affect configuration."""
    print("🌍 Environment Variables Demo\n")
    
    print("Current environment variables:")
    env_vars = [
        "CLOUD_REGION",
        "CLOUD_PROFILE", 
        "MODEL_ARN",
        "MAX_TOKENS",
        "PROVIDER"
    ]
    
    for var in env_vars:
        value = os.getenv(var, "Not set")
        print(f"   {var}: {value}")
    
    print()
    print("💡 Tip: Set these environment variables or create a .env file")
    print("   to customize the classifier behavior.")
    print()


def main():
    """Run advanced examples."""
    print("🤖 AI Classifier Sample - Advanced Usage Example\n")
    
    try:
        demo_settings_management()
        demo_environment_variables()
        demo_conversational_classification()
        demo_single_vs_conversational()
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("💡 Make sure you have proper AWS credentials configured.")
        print("💡 Ensure your MODEL_ARN is valid and accessible in your region.")


if __name__ == "__main__":
    main()