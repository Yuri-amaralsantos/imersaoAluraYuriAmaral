# 🧠 Redação IA: Um sistema de agentes inteligentes para ensino de redação

**Redação IA** é um sistema interativo de agentes desenvolvidos com **Python** e **Gemini (Google AI)**, que simula a experiência de um professor de redação. O projeto combina **geração de temas**, **criação de redações exemplo** e **avaliação automática** com feedback detalhado, como em uma aula real.

---

## 🚀 O que o sistema faz?

Este projeto reúne **três agentes principais** que trabalham juntos para melhorar sua escrita:

| Agente | Função |
|-------|--------|
| 🧑‍🏫 `agente_tutor` | Gera temas de redação dissertativa-argumentativa com contextualização |
| ✍️ `agente_aluno` | Produz uma redação exemplo a partir do tema |
| 🖊️ `agente_corretor` | Avalia qualquer redação com base no tema, destacando pontos fortes e fracos |

---

## 💡 Exemplos de uso

Ao executar o sistema, você pode:

- Receber um **tema atual e contextualizado** para praticar
- Solicitar uma **redação modelo gerada pela IA**
- Escrever seu próprio texto e receber uma **correção detalhada**
- Solicitar **novos temas** a qualquer momento

---

## 🛠️ Tecnologias utilizadas

- 🐍 **Python 3.10+**
- 🌐 [Gemini API (Google Generative AI)](https://ai.google.dev/)
- 🧪 `google.adk` (AI Development Kit)
- 📦 `dotenv` para gerenciamento seguro da chave da API

---

## 📂 Estrutura dos agentes

Cada agente é criado com instruções específicas que definem seu comportamento e tom:

agente_tutor = Agent(name="agente_tutor", instruction="Você é um professor de redação...")
agente_aluno = Agent(name="agente_aluno", instruction="Você é um aluno que escreve redações...")
agente_corretor = Agent(name="agente_corretor", instruction="Você é um corretor de redações...")



## 🧠 Exemplo de execução
📚 Bem-vindo ao Professor de Redação Interativo com IA!

Etapa 1: Gerando tema...
📖 Tema proposto:
Tema: Os impactos das redes sociais no comportamento social
[texto de contextualização]

> Digite sua redação ou escolha: 'exemplo', 'mudar tema', 'sair':

## 📌 Possíveis aplicações
- Plataformas educacionais e EAD

- Assistentes virtuais de correção de texto

- Bots para prática de escrita para ENEM ou concursos

- Ferramentas para professores e corretores automatizados

