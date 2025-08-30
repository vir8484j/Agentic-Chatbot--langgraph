import os
from src.langgraph_components.state.state import State
class BasicChatbotNode:
    """
    Basic Chatbot node implementation
    """
    
    def __init__(self,model):
        self.llm=model
        
    def process(self,state:State)->dict:
        """
        Represent the input state and generates a chatbot response.
        """ 
        
        return {"messages":self.llm.invoke(state["messages"])}