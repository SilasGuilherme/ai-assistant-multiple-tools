🤖 AI Assistant com LangChain + Ollama + FastAPI

Este projeto implementa um assistente de IA que pode usar ferramentas externas (como calculadora, busca, etc.) através do LangChain.
Ele utiliza o Ollama como LLM local, expõe um endpoint em FastAPI (/ask) e segue boas práticas de modularidade e segurança (configuração via .env).

⚡️ Requisitos

Python 3.12+

Poetry
 ou venv para gerenciar dependências

Ollama
 instalado e rodando localmente

Modelos do Ollama (exemplo: mistral, llama3 ou outro de sua preferência)

📦 Instalação

Clone o repositório:
git clone https://github.com/SilasGuilherme/ai-assistant-multiple-tools.git
cd ai-assistant

Crie e ative um ambiente virtual:
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows

Instale as dependências:
pip install -r requirements.txt

⚙️ Configuração

O projeto utiliza variáveis de ambiente apenas para as integrações externas (APIs opcionais).

A porta **não é configurada no código nem no `.env`**.  
Por padrão, ao rodar com Uvicorn, a aplicação sobe em `http://127.0.0.1:8000`.  

Se quiser usar outra porta, especifique no comando de execução:
uvicorn app.main:app --reload --port 9000

O modelo do Ollama está definido no código, em:
app/core/config.py

Por padrão usamos o modelo `mistral`.  
Se quiser trocar (ex.: para `llama2`), basta alterar esse arquivo.

## APIs Externas

O projeto possui integração opcional com APIs de **Clima** e **Notícias**.  
Essas funcionalidades só funcionam se você configurar as chaves de API corretamente.

### 1. Clima
Usamos a API [OpenWeatherMap](https://openweathermap.org/api).  
Crie uma conta gratuita e obtenha sua chave.  

No arquivo .env, adicione:
OPENWEATHER_API_KEY=sua_chave_aqui

### 2. Notícias
Usamos a API [NewsAPI](https://newsapi.org/).  
Crie uma conta gratuita e copie a chave.

No arquivo .env, adicione:
NEWS_API_KEY=sua_chave_aqui

### Uso sem chaves
Se você não configurar as chaves, o projeto **continua funcionando** com o modelo Mistral no Ollama, mas os comandos de clima e notícias retornarão uma mensagem de erro informando que a API não está configurada.


▶️ Como executar

Certifique-se que o Ollama está rodando:
ollama run mistral

Inicie a API:
uvicorn app.main:app --reload

Envie uma requisição para o endpoint /ask:
curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Qual é a raiz quadrada de 144?"}'

Você receberá a resposta processada pelo agente. 🎉

🧩 Estrutura do Projeto

app/
├── agents/
│ ├── router.py # Configuração do agente e prompt
│ ├── tools.py # Registro e definição das ferramentas
│
├── core/
│ └── config.py # Configuração principal do LLM (modelo Ollama)
│ └── logger.py # Configuração de logs
│
├── services/
│ ├── math_service.py # Serviço para cálculos matemáticos
│ ├── news_service.py # Serviço para integração com NewsAPI
│ └── weather_service.py # Serviço para integração com OpenWeatherMap
│
├── tests/
│ ├── test_math.py # Testes do serviço de cálculos
│ ├── test_news.py # Testes do serviço de notícias
│ └── test_weather.py # Testes do serviço de clima
│
└── main.py # Ponto de entrada da aplicação FastAPI

.env     # Variáveis de ambiente (não versionado)
.env.example     # Exemplo de configuração de variáveis de ambiente
requirements.txt     # Dependências do projeto
README.md     # Este arquivo


🚀 Exemplo de Uso

POST /ask
{
  "question": "Me diga quanto é (25 * 4) / 2"
}

Resposta:
{
  "answer": "O resultado é 50."
}

## 🧪 Testes

Este projeto utiliza **pytest** para rodar os testes unitários.

### Executar todos os testes
pytest -v

### Executar testes de um arquivo específico
pytest app/tests/test_math.py -v
pytest app/tests/test_news.py -v
pytest app/tests/test_weather.py -v

### Estrutura dos testes
test.math.py → valida cálculos matemáticos.
test.news.py → valida integração com a API de notícias (inclui mock).
test.weather.py → valida integração com a API de clima (inclui mock).

🧠 Lógica de Implementação

LLM Local (Ollama) → O modelo mistral é usado como cérebro principal.
LangChain Agents → O agente recebe o prompt estruturado, decide se precisa usar uma ferramenta e retorna a resposta final.
Ferramentas → Calculadora local, API pública de Previsão do Tempo e API pública de Notícias. Outras podem ser adicionadas facilmente em tools.py.
FastAPI → Expõe um endpoint simples (/ask) que recebe perguntas em JSON e retorna respostas do agente.

📚 O que eu aprendi

- Como integrar Ollama com LangChain via ChatOllama.
- Diferença entre create_openai_tools_agent (que também funciona com Ollama) e os agentes mais antigos (initialize_agent).
- Importância de configurar variáveis de ambiente para manter o projeto seguro e configurável.
- Como lidar com erros comuns do LangChain (ex: placeholders ausentes no prompt).

🔮 O que faria diferente com mais tempo

- Adicionar uma UI em React para conversar com o assistente de forma mais amigável.
- Implementar memória de longo prazo com banco de dados vetorial.
- Criar mais ferramentas úteis (ex: busca na web, integração com mais APIs externas).
- Escrever testes mais complexos para garantir a robustez do agente.
- Criar logs para aprimorar o monitoramento e debugging.


## 📄 Licença
Este projeto está licenciado sob a licença MIT – veja o arquivo [LICENSE](./LICENSE) para mais detalhes.

## 👥 Créditos
Desenvolvido por SILAS GUILHERME com uso de **LangChain**, **FastAPI** e **Ollama**.
