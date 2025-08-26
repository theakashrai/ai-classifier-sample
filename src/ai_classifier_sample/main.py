"""
Main entry point for the AI Classifier Sample project.
This demonstrates both single-turn and multi-turn conversational classification.
"""

from ai_classifier_sample.service.classifier import MessageClassifier, ConversationState


def main():
    classifier = MessageClassifier()
    
    # Single-turn classification (original functionality)
    print("=== Single-turn Classification ===")
    message = "Hello, how are you?"
    response: str = classifier.classify(message=message)
    print(f"Classified Response: {response}")
    
    print("\n=== Multi-turn Conversational Classification ===")
    # Multi-turn conversational classification
    conversation_state = ConversationState()
    
    # Simulate a conversation
    messages = [
        "Hi, I need help with my order",
        "I placed it last week but haven't received any tracking information",
        "The order number is #12345",
        "Actually, I also want to return another item I bought last month",
        "It doesn't fit properly"
    ]
    
    for i, msg in enumerate(messages, 1):
        print(f"\nTurn {i}: {msg}")
        conv_response = classifier.classify_conversational(msg, conversation_state)
        print(f"Intent: {conv_response.intent}")
        print(f"Transition: {conv_response.intent_transition}")
        print(f"Confidence: {conv_response.confidence}")
        print(f"Reasoning: {conv_response.reasoning}")
        print(f"Current State Intent: {conversation_state.current_intent}")
        print(f"Resolved Intents: {conversation_state.resolved_intents}")
        print("-" * 50)


if __name__ == "__main__":
    main()