import os
from typing import Dict, List, Any
from langchain_google_vertexai import VertexAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, SystemMessage
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CustomerInsightAgent:
    def __init__(self):
        """
        Initialize the Vertex AI Agent with Gemini Pro credentials.
        """
        self.llm = VertexAI(
            model_name="gemini-pro",
            max_output_tokens=1024,
            temperature=0.2,
            location="us-central1"
        )
        logger.info("Vertex AI Agent initialized successfully.")

    def analyze_sentiment(self, ticket_text: str) -> Dict[str, Any]:
        """
        Analyzes the sentiment of an incoming support ticket using Gemini.
        Returns a dictionary with sentiment score and urgency flag.
        """
        prompt = f"""
        You are a Customer Experience AI. Analyze the sentiment of the following support ticket.
        Classify it as Positive, Neutral, or Negative.
        Determine if it requires 'Urgent' intervention (Yes/No).
        
        Ticket: "{ticket_text}"
        
        Output format: JSON {{ "sentiment": "...", "urgency": "..." }}
        """
        
        try:
            response = self.llm.invoke(prompt)
            # In a real scenario, we would parse the JSON string here
            logger.info(f"Sentiment analysis complete for ticket: {ticket_text[:30]}...")
            return response
        except Exception as e:
            logger.error(f"Error in sentiment analysis: {str(e)}")
            return {"error": "Analysis failed"}

    def generate_retention_offer(self, customer_segment: str, sentiment: str) -> str:
        """
        Drafts a personalized email response based on customer value and sentiment.
        """
        template = """
        Context: Customer segment is {segment} and current sentiment is {sentiment}.
        Task: Draft a short, empathetic email response.
        Offer: If sentiment is Negative and Segment is High-Value, offer a 20% discount.
        Otherwise, offer a personalized apology and priority support.
        """
        
        prompt = PromptTemplate(
            input_variables=["segment", "sentiment"],
            template=template
        )
        
        final_prompt = prompt.format(segment=customer_segment, sentiment=sentiment)
        return self.llm.invoke(final_prompt)

# Example Usage (Mock Execution)
if __name__ == "__main__":
    # Simulating a run
    agent = CustomerInsightAgent()
    
    sample_ticket = "I have been waiting for my refund for 2 weeks! This is unacceptable."
    sentiment_result = agent.analyze_sentiment(sample_ticket)
    
    print(f"Analysis Result: {sentiment_result}")
    
    response_draft = agent.generate_retention_offer("High-Value", "Negative")
    print(f"Drafted Response: \n{response_draft}")
