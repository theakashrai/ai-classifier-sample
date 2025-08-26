#!/usr/bin/env python3
"""
Complete example replicating the main.py functionality.

This example shows exactly how the AI Classifier Sample works,
demonstrating both single-turn and multi-turn conversational classification
as implemented in the main application.
"""

import json
from ai_classifier_sample.service.classifier import MessageClassifier, ConversationState


def demo_single_turn_classification():
    """Demonstrate single-turn classification as in main.py"""
    print("=== Single-turn Classification ===")
    
    classifier = MessageClassifier()
    
    # Test the same message as in main.py
    message = "Hello, how are you?"
    response: str = classifier.classify(message=message)
    
    print(f"Input Message: {message}")
    print(f"Classified Response: {response}")
    
    # Parse and display the JSON response nicely
    try:
        response_data = json.loads(response)
        print(f"Category: {response_data.get('category', 'Unknown')}")
        print(f"Message: {response_data.get('message', 'Unknown')}")
    except json.JSONDecodeError:
        print("Note: Response is not valid JSON")
    
    print()


def demo_multi_turn_conversational():
    """Demonstrate multi-turn conversational classification as in main.py"""
    print("=== Multi-turn Conversational Classification ===")
    
    classifier = MessageClassifier()
    conversation_state = ConversationState()
    
    # Use the exact same conversation from main.py
    messages = [
        "Hi, I need help with my order",
        "I placed it last week but haven't received any tracking information",
        "The order number is #12345",
        "Actually, I also want to return another item I bought last month",
        "It doesn't fit properly"
    ]
    
    for i, msg in enumerate(messages, 1):
        print(f"\nTurn {i}: {msg}")
        
        try:
            conv_response = classifier.classify_conversational(msg, conversation_state)
            
            print(f"Intent: {conv_response.intent}")
            print(f"Transition: {conv_response.intent_transition}")
            print(f"Confidence: {conv_response.confidence}")
            print(f"Reasoning: {conv_response.reasoning}")
            print(f"Current State Intent: {conversation_state.current_intent}")
            print(f"Resolved Intents: {conversation_state.resolved_intents}")
            
        except Exception as e:
            print(f"Error processing turn {i}: {e}")
        
        print("-" * 50)


def demo_additional_scenarios():
    """Demonstrate additional realistic customer support scenarios"""
    print("\n=== Additional Customer Support Scenarios ===")
    
    classifier = MessageClassifier()
    
    # Test various single-turn classifications
    test_messages = [
        "I want to track my package",
        "This product broke after one day, I want a refund",
        "Great service, thank you!",
        "How do I cancel my subscription?",
        "The delivery was delayed and I'm very unhappy",
        "Can you exchange this for a different color?"
    ]
    
    print("\n--- Single-turn classifications ---")
    for msg in test_messages:
        try:
            result = classifier.classify(msg)
            result_data = json.loads(result)
            print(f"'{msg}' → {result_data['category']}")
        except Exception as e:
            print(f"'{msg}' → Error: {e}")
    
    # Test a complex multi-turn conversation
    print("\n--- Complex multi-turn conversation ---")
    conversation_state = ConversationState()
    
    complex_conversation = [
        "I have a problem with my recent purchase",
        "The item arrived damaged and I'd like to return it",
        "Also, I haven't received tracking for another order I placed",
        "That order was placed 2 weeks ago",
        "Thank you for helping me resolve these issues"
    ]
    
    for i, msg in enumerate(complex_conversation, 1):
        print(f"\nTurn {i}: {msg}")
        try:
            conv_response = classifier.classify_conversational(msg, conversation_state)
            print(f"  → Intent: {conv_response.intent} ({conv_response.intent_transition})")
            print(f"  → Confidence: {conv_response.confidence}")
        except Exception as e:
            print(f"  → Error: {e}")


def main():
    """Main function replicating and extending main.py functionality"""
    print("🤖 AI Classifier Sample - Complete Example\n")
    print("This example replicates the functionality demonstrated in main.py")
    print("and shows additional realistic customer support scenarios.\n")
    
    try:
        demo_single_turn_classification()
        demo_multi_turn_conversational()
        demo_additional_scenarios()
        
        print("\n✅ Example completed successfully!")
        print("\n💡 Tips:")
        print("  - Single-turn: Good for isolated customer messages")
        print("  - Multi-turn: Ideal for ongoing conversations with context")
        print("  - Available categories: 'Support, Feedback, Complaint', 'Order Tracking', 'Refund/Exchange'")
        
    except Exception as e:
        print(f"\n❌ Error running example: {e}")
        print("\n🔧 Troubleshooting:")
        print("  1. Ensure AWS credentials are configured")
        print("  2. Check that your MODEL_ARN is valid and accessible")
        print("  3. Verify your region supports the specified model")
        print("  4. Confirm you have the required permissions for AWS Bedrock")


if __name__ == "__main__":
    main()