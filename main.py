import os
from dotenv import load_dotenv
from google import genai

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types  # Para criar conteúdos (Content e Part)
from datetime import date
import requests
import warnings

warnings.filterwarnings("ignore")

# Carrega a API KEY do arquivo .env
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

client = genai.Client()

MODEL_ID = "gemini-2.0-flash"

# Função auxiliar que envia uma mensagem para um agente via Runner e retorna a resposta final
def call_agent(agent: Agent, message_text: str) -> str:
    session_service = InMemorySessionService()
    session = session_service.create_session(app_name=agent.name, user_id="user1", session_id="session1")
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    content = types.Content(role="user", parts=[types.Part(text=message_text)])

    final_response = ""
    for event in runner.run(user_id="user1", session_id="session1", new_message=content):
        if event.is_final_response():
            for part in event.content.parts:
                if part.text is not None:
                    final_response += part.text + "\n"
    return final_response

#agentes
def criar_agente_tutor() -> Agent:
    return Agent(
        name="agente_tutor",
        model=MODEL_ID,
        instruction="""
Você é um professor de redação que propõe temas atuais e relevantes nos últimos anos.

Sua tarefa é:
- Escolher um tema pertinente e plausível para provas atuais;
- Informar que o tipo de texto é dissertativo-argumentativo;
- Escrever um pequeno texto introdutório, como se fosse uma explicação ou contextualização sobre o tema — sem listar estrutura (introdução, desenvolvimento ou conclusão).

Esse texto deve servir como inspiração para que o aluno compreenda o tema e desenvolva a redação a partir disso, como nos melhores modelos de orientação de professores de redação.

Evite roteiros. Escreva com tom motivador e natural, como se estivesse falando com um estudante brasileiro se preparando para o ENEM ou um concurso público.
"""
    )

def criar_agente_aluno() -> Agent:
    return Agent(
        name="agente_aluno",
        model=MODEL_ID,
        instruction="""
Você é um aluno simulando uma redação baseada em um tema proposto.
Sua tarefa é escrever um texto dissertativo com introdução, desenvolvimento e conclusão, com até 300 palavras.
Evite repetir ideias e mantenha coesão textual.
"""
    )

def criar_agente_corretor() -> Agent:
    return Agent(
        name="agente_corretor",
        model=MODEL_ID,
        instruction="""
Você é um corretor de redações. Avalie o texto do aluno considerando:
1. Gramática
2. Coesão e coerência
3. Argumentação e clareza
4. Pertinência em relação ao tema proposto

Dê um parecer completo, com elogios e sugestões, como um professor faria. Seja direto, mas respeitoso, apontando como o aluno pode melhorar.
"""
    )

# Execução principal
def executar_chatbot():
    print("📚 Professor de Redação Interativo")

    agente_tutor = criar_agente_tutor()
    agente_aluno = criar_agente_aluno()
    agente_corretor = criar_agente_corretor()

    print("Etapa 1: Gerando tema...\n")
    tema = call_agent(agente_tutor, f"Hoje é {date.today().strftime('%d/%m/%Y')}")
    print("📖 Tema proposto:")
    print(tema)
    print("\n")

    ultima_redacao = ""  # Para armazenar a última redação, se o usuário quiser corrigir

    while True:
        print("Digite sua redação ou escolha uma opção: 'exemplo', 'mudar tema', 'sair':")
        entrada = input("> ").strip()

        if entrada.lower() == "sair":
            print("Encerrando o programa.")
            break

        elif entrada.lower() == "exemplo":
            print("Gerando redação exemplo...\n")
            exemplo = call_agent(agente_aluno, tema)
            print("✍️ Redação modelo gerada:")
            print(exemplo)
            ultima_redacao = exemplo  # Armazena como última redação
            print("\n")

            print("Avaliando redação exemplo...\n")
            mensagem_correcao = f"""
                Avalie a seguinte redação com base no tema proposto abaixo.

                📌 Tema: {tema}

                📝 Redação:
                {ultima_redacao}
                """

            avaliacao = call_agent(agente_corretor, mensagem_correcao)
            print("🖊️ Avaliação do corretor:")
            print(avaliacao)
            print("\n")

        elif entrada.lower() == "mudar tema":
            print("Gerando novo tema...\n")
            tema = call_agent(agente_tutor, f"Hoje é {date.today().strftime('%d/%m/%Y')}")
            print("📖 Novo tema proposto:")
            print(tema)
            print("\n")

        else:
            # Qualquer outra entrada é considerada uma redação
            ultima_redacao = entrada
            print("\nRedação registrada. Enviando para correção...\n")

            mensagem_correcao = f"""
            Avalie a seguinte redação com base no tema proposto abaixo.

            📌 Tema: {tema}

            📝 Redação:
            {ultima_redacao}
            """

            avaliacao = call_agent(agente_corretor, mensagem_correcao)
            print("🖊️ Avaliação do corretor:")
            print(avaliacao)
            print("\n")
        

        
if __name__ == "__main__":
    executar_chatbot()
