🚀 Pipeline CI/CD com GitHub Actions e CodeQL — FATEC
📌 Sobre o Projeto
Este projeto foi desenvolvido como atividade prática da FATEC com o objetivo de demonstrar a utilização de uma pipeline CI/CD integrada ao GitHub Actions e à ferramenta de análise estática de segurança CodeQL.

O foco principal foi validar como o CodeQL identifica vulnerabilidades em aplicações Python durante o processo automatizado de integração contínua.

🛠️ Tecnologias Utilizadas
GitHub

GitHub Actions

CodeQL

Python

⚙️ Objetivo da Pipeline
A pipeline foi criada para:

Automatizar testes do projeto

Executar análise de segurança automaticamente

Detectar vulnerabilidades conhecidas no código

Validar boas práticas de desenvolvimento seguro

Demonstrar funcionamento do CodeQL em ambiente real

🔄 Fluxo da Pipeline
Código
Push no GitHub
       ↓
GitHub Actions inicia a pipeline
       ↓
Instala dependências
       ↓
Executa testes automatizados
       ↓
Executa análise de segurança com CodeQL
       ↓
Pipeline aprovada ou bloqueada
🧪 Cenários Testados
✅ Teste 1 — Código Limpo
Código Python sem vulnerabilidades conhecidas

Resultado: Pipeline executada com sucesso, nenhum alerta de segurança encontrado

📷 Evidência:
<img width="1080" height="274" alt="image" src="https://github.com/user-attachments/assets/21690c8f-1bed-4923-828b-2856be04ef23" />

🔒 Teste 2 — Exemplos e boas práticas

Para evitar falsos positivos e exemplificar boas práticas, o repositório não contém exemplos ativos de código vulnerável. Em vez disso, apresentamos abaixo a forma segura recomendada para consultas SQL em SQLite.

Exemplo de código seguro (uso de consultas parametrizadas):

```python
import sqlite3

def buscar_usuario_seguro(username):
       # ✅ SEGURO: uso de parâmetros preparados
       conn = sqlite3.connect('database.db')
       cursor = conn.cursor()

       query = "SELECT * FROM usuarios WHERE username = ?"
       cursor.execute(query, (username,))
       return cursor.fetchall()
```

Problema evitado: Injeção de SQL (CWE-89) — sempre use parâmetros ao inserir valores do usuário em consultas.

📷 Evidência:
<img width="1070" height="291" alt="image" src="https://github.com/user-attachments/assets/fe36d07a-b48a-4369-8bb5-9efad3931c7f" />

🔍 Outras Vulnerabilidades Estudadas
Command Injection (CWE-78)

Path Traversal (CWE-22)

Hard-coded Credentials (CWE-798)

Weak Cryptography (CWE-327)

Insecure Deserialization (CWE-502)

Uso inseguro de eval() (CWE-94)

Geração insegura de números aleatórios (CWE-338)

📚 Aprendizados Obtidos
Funcionamento de uma pipeline CI/CD

Automação de verificações de segurança

Importância da análise estática de código

Detecção de vulnerabilidades com CodeQL

Boas práticas de desenvolvimento seguro

Integração entre GitHub Actions e CodeQL

✅ Conclusão
O projeto demonstrou na prática como ferramentas de segurança podem ser integradas ao processo de desenvolvimento para identificar vulnerabilidades automaticamente antes da publicação.

A utilização do CodeQL junto ao GitHub Actions mostrou-se eficiente para reforçar a segurança da aplicação e aplicar conceitos de DevSecOps dentro da pipeline CI/CD.

👨‍💻 Autor
Projeto desenvolvido para fins acadêmicos na FATEC.
