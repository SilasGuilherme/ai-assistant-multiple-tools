from langchain_community.chat_models import ChatOllama
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from app.core.config import OLLAMA_MODEL
from app.agents.tools import tools


def create_agent():
    # Inicializa o LLM
    llm = ChatOllama(model=OLLAMA_MODEL, temperature=0)

        # Prompt compatível com create_react_agent
    prompt = PromptTemplate.from_template(
        """
    Você é um assistente inteligente que pode responder perguntas e usar ferramentas quando necessário.

    Regras importantes para a Calculadora:
    - Sempre forneça expressões no formato Python.
    - Exemplos: "2 + 2", "sqrt(144)", "(10 / 2) ** 3".
    - Nunca escreva em linguagem natural, apenas expressões matemáticas válidas.

    Ferramentas disponíveis:
    {tools}

    Nomes das ferramentas: {tool_names}

    Use o formato:
    Thought: descreva seu raciocínio
    Action: o nome da ferramenta a usar (se necessário)
    Action Input: a entrada para a ferramenta
    Observation: resultado da ferramenta
    Thought: análise do resultado
    Final Answer: resposta final para o usuário

    A resposta final deve ser dada sempre em português brasileiro.
    Pergunta: {input}
    {agent_scratchpad}
        """
    )

        # Cria o agente ReAct
    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt,
    )

        # Executor do agente
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
    )

    return agent_executor
