from langchain_aws import ChatBedrockConverse
from langchain_core.messages.base import BaseMessage
from langchain_core.prompt_values import ChatPromptValue
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from pydantic import BaseModel
from typing import Union, List, Optional

from ai_classifier_sample.config.settings import Settings, get_settings
from ai_classifier_sample.models import ConversationTurn, ConversationalClassifierOutput, ClassifierOutput


class ConversationState:
    def __init__(self):
        self.current_intent: Optional[str] = None
        self.conversation_history: List[ConversationTurn] = []
        self.resolved_intents: List[str] = []
    
    def add_turn(self, message: str, speaker: str, intent: Optional[str] = None):
        turn = ConversationTurn(message=message, speaker=speaker, intent=intent)
        self.conversation_history.append(turn)
    
    def get_recent_context(self, max_turns: int = 5) -> List[ConversationTurn]:
        return self.conversation_history[-max_turns:] if self.conversation_history else []
  
class MessageClassifier:
    def __init__(self):
        settings: Settings = get_settings()
            
        self.llm = ChatBedrockConverse(
            model=settings.model_arn,
            max_tokens=settings.max_tokens,
            provider=settings.provider,
            region_name=settings.cloud_region,
            temperature=0.0,
            credentials_profile_name=settings.cloud_profile
        )
    
    @staticmethod
    def _format_conversation_context(conversation_history: List[ConversationTurn]) -> str:
        if not conversation_history:
            return "No previous conversation"
        
        formatted = []
        for turn in conversation_history:
            formatted.append(f"{turn.speaker}: {turn.message}")
        return "\n".join(formatted)

    def classify_conversational(self, current_message: str, conversation_state: ConversationState) -> ConversationalClassifierOutput:
        """Classify a message within a conversational context"""
        recent_context = conversation_state.get_recent_context(max_turns=5)
        context_str = self._format_conversation_context(recent_context)
        
        prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(
                """You are a conversational customer support intent classifier. Analyze the current message in the context of an ongoing conversation.

Available intents: 'Support, Feedback, Complaint', 'Order Tracking', 'Refund/Exchange'

Determine:
1. Is this continuing the current active intent or introducing a new one?
2. What is the specific intent for this message?
3. How confident are you in this classification?

Intent Transitions:
- CONTINUE: Following up on the same intent
- NEW: Introducing a completely new intent  
- CLARIFICATION: Asking for clarification or providing additional details"""
            ),
            HumanMessagePromptTemplate.from_template(
                """<conversation_context>
Current Active Intent: {current_intent}
Recent Conversation:
{conversation_context}
</conversation_context>

<current_message>{current_message}</current_message>

Provide your analysis in the following format:
- Reasoning for your classification
- Intent transition type (CONTINUE/NEW/CLARIFICATION)
- The specific intent category
- Your confidence level (HIGH/MEDIUM/LOW)"""
            )
        ])
        
        formatted_prompt = prompt.format_prompt(
            current_intent=conversation_state.current_intent or "None",
            conversation_context=context_str,
            current_message=current_message
        )
        
        structured_llm = self.llm.with_structured_output(ConversationalClassifierOutput)
        raw_response = structured_llm.invoke(input=formatted_prompt.to_messages())
        
        if isinstance(raw_response, dict):
            _response = ConversationalClassifierOutput(**raw_response)
        else:
            _response: ConversationalClassifierOutput = raw_response  # type: ignore
            
        # Update conversation state
        conversation_state.add_turn(current_message, "user", _response.intent)
        
        if _response.intent_transition == "NEW":
            if conversation_state.current_intent:
                conversation_state.resolved_intents.append(conversation_state.current_intent)
            conversation_state.current_intent = _response.intent
        
        return _response

    def classify(self, message: str) -> str:
        """Original single-turn classification method"""
        prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(
                "You are a customer support message classifier. Classify the following message into one of the categories: 'Support, Feedback, Complaint', 'Order Tracking', 'Refund/Exchange'."
            ),
            HumanMessagePromptTemplate.from_template("Message: '{question}'\nCategory:")
        ])
  
        formatted_prompt: ChatPromptValue = prompt.format_prompt(question=message)
        
        structured_llm = self.llm.with_structured_output(ClassifierOutput)
        raw_response: Union[dict, BaseModel] = structured_llm.invoke(input=formatted_prompt.to_messages())
        
        # Convert response to ClassifierOutput if it's a dict
        if isinstance(raw_response, dict):
            response: ClassifierOutput = ClassifierOutput(**raw_response)
        else:
            response: ClassifierOutput = raw_response  # type: ignore
            
        return response.model_dump_json()

