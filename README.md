# FATEC CI/CD - Pipeline de Integração Contínua e Entrega Contínua

> Projeto de demonstração de um **pipeline CI/CD seguro** com análise de segurança (CodeQL), testes automatizados e deploy para ambiente de stage.

## 📋 Visão Geral

Este projeto implementa um pipeline CI/CD completo usando **GitHub Actions** que:

1. ✅ **Analisa segurança** com CodeQL (detecta vulnerabilidades como SQL Injection)
2. 🧪 **Executa testes automatizados** com pytest
3. 📊 **Verifica qualidade do código** com flake8
4. 🚀 **Faz deploy** para ambiente de stage

## 🏗️ Estrutura do Projeto

```
fatec-cicd-vitorlima/
├── .github/
│   ├── workflows/
│   │   ├── ci-cd-pipeline.yml      # Workflow principal com 3 jobs
│   │   └── codeql.yml              # Análise CodeQL
│   └── codeql-config.yml           # Configuração de análise
├── main.py                          # Código Python funcional
├── tests/
│   └── test_main.py                # Suite de testes
├── requirements.txt                # Dependências do projeto
├── .gitignore                      # Arquivos ignorados pelo Git
└── README.md                       # Este arquivo
```

## 🚀 Pipeline CI/CD

### Jobs Executados

```
push/pull_request/workflow_dispatch
    │
    ├─→ JOB 1: 🔒 Análise CodeQL
    │   ├─ Inicializa CodeQL
    │   ├─ Executa análise de segurança
    │   └─ Gera relatório de vulnerabilidades
    │
    ├─→ JOB 2: 🧪 Testes Automatizados (aguarda Job 1 ✅)
    │   ├─ Executa pytest
    │   ├─ Verifica qualidade com flake8
    │   └─ Relatório de testes
    │
    └─→ JOB 3: 🚀 Deploy para Stage (aguarda Job 1 e 2 ✅)
        ├─ Faz checkout
        ├─ Simula deploy
        └─ Marca como sucesso
```

## 📊 Teste 1: Código Seguro → ✅ Todos os Jobs Verdes

### Resultado Esperado
- ✅ **Job 1 (CodeQL)** → PASSOU
- ✅ **Job 2 (Testes)** → PASSOU  
- ✅ **Job 3 (Deploy)** → PASSOU

### Evidência
Commit: `1cea720` - "fix: corrige SQL Injection com query parametrizada"

Código corrigido com query parametrizada:
```python
cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
```

Acesse: https://github.com/vitorlima1235/fatec-cicd-vitorlima/actions

## ❌ Teste 2: Código Vulnerável → Job 1 Falha

### Código Vulnerável Introduzido
```python
# ⚠️ SQL INJECTION - NUNCA FAÇA ISSO!
cursor.execute(f"SELECT * FROM users WHERE id={user_id}")
```

### Resultado Observado
- ❌ **Job 1 (CodeQL)** → **FALHOU** (detectou vulnerabilidade)
- ⬜ **Job 2 (Testes)** → NÃO EXECUTOU (bloqueado pela falha)
- ⬜ **Job 3 (Deploy)** → NÃO EXECUTOU (bloqueado pela falha)

### Evidência
Commit: `f3d34b5` - "test: código vulnerável - SQL Injection"

Alerta de segurança detectado em: **Security → Code scanning alerts**

Tipo: **SQL Injection via string formatting**

## ✅ Teste 3: Correção Aplicada → Pipeline Verde Novamente

### Código Corrigido
```python
# ✅ SEGURO - Query parametrizada
cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
```

### Resultado
- ✅ **Job 1 (CodeQL)** → PASSOU (nenhuma vulnerabilidade)
- ✅ **Job 2 (Testes)** → PASSOU (testes executados com sucesso)
- ✅ **Job 3 (Deploy)** → PASSOU (deployment concluído)

## 📝 Histórico de Commits

```bash
f8c34f8 - chore: melhora configuração CodeQL - adiciona paths-ignore adicionais
1cea720 - fix: corrige SQL Injection com query parametrizada
f3d34b5 - test: código vulnerável - SQL Injection
fb49f44 - fix: corrige sintaxe YAML do workflow CI/CD
2eaceb1 - feat: pipeline CI/CD inicial com código seguro
```

## 🧪 Executar Testes Localmente

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar testes
pytest tests/ -v

# Verificar qualidade do código
flake8 . --max-line-length=120 --exclude=venv

# Análise de segurança (local)
bandit -r . -ll
```

## 🔐 Configurações de Segurança

### GitHub Advanced Security
- ✅ CodeQL habilitado
- ✅ Code scanning alerts ativo
- ✅ Dependabot habilitado

### Environments
- ✅ Environment "stage" criado
- ✅ Protection rules configuradas

## 📦 Testes Inclusos

### TestSaudacao
```python
def test_saudacao_nome_valido(self):
    resultado = saudacao("Maria")
    assert "Maria" in resultado

def test_saudacao_tipo_invalido(self):
    with pytest.raises(TypeError):
        saudacao(123)
```

### TestCalcularMedia
```python
def test_media_simples(self):
    assert calcular_media([10, 8, 6]) == 8.0

def test_lista_vazia(self):
    with pytest.raises(ValueError):
        calcular_media([])
```

**Resultado:** ✅ 4/4 testes passando

## 🎯 Aprendizados Principais

1. **CodeQL como guardião de segurança** - Bloqueia código vulnerável antes do deploy
2. **Pipeline como barreira de qualidade** - Garante que apenas código testado entra em produção
3. **Automação reduz riscos** - Detecta vulnerabilidades sem intervenção manual
4. **Segurança desde o início** - Análise de segurança é o primeiro job, não o último

## 🔗 Links Úteis

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [CodeQL Documentation](https://codeql.github.com/)
- [OWASP SQL Injection Prevention](https://owasp.org/www-community/attacks/SQL_Injection)

---

**Status:** ✅ CI/CD Pipeline 100% Funcional e Seguro | Todos os testes passando 🟢