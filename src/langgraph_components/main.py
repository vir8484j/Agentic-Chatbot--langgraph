import streamlit as st
from src.langgraph_components.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph_components.LLMs.groqllm import GroqLLM
from src.langgraph_components.graph.graph_builder import GraphBuilder
from src.langgraph_components.ui.streamlitui.display_result import DisplayResultStreamlit
def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while implementing exception handling for robustness.
    
    """
    
    #Load UI
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()
    
    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    # Input for user_message
    if st.session_state.IsFetchButtonClicked:
        user_message=st.session_state.timeframe
    else:    
        user_message=st.chat_input("Enter your message:")
    
    if user_message:
        try:
            #Config the LLm's
            obj_llm__config=GroqLLM(user_controls_input=user_input)
            model=obj_llm__config.get_llm_model()
            
            if not model:
                st.error("Error: LLM model could not be initialized")
                return
            #Initialize and set up the graph based on use case
            usecase=user_input.get("selected_usecase")
            
            if not usecase:
                st.error("Error: No use case selected")
                return
            
            #Graph builder
            graph_builder=GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error graph setup failed {e}")
                return
                
        except Exception as e:    
            st.error(f"Error: Graph set up failed {e}")
            return