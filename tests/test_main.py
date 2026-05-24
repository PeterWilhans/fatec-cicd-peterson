"""
Testes Unitários - Exemplo FATEC
=================================
Arquivo de exemplo para demonstrar testes automatizados
que serão executados na pipeline CI/CD.

Para executar os testes localmente:
    pip install pytest pytest-cov
    pytest tests/

Para executar com cobertura:
    pytest --cov=. --cov-report=html
"""

import pytest
from main import saudacao, calcular_media, validar_email


class TestSaudacao:
    """Testes para a função saudacao"""
    
    def test_saudacao_com_nome(self):
        """Testa saudação com nome fornecido"""
        resultado = saudacao("FATEC")
        assert resultado == "Olá, FATEC!"
        assert isinstance(resultado, str)
    
    def test_saudacao_nome_vazio(self):
        """Testa saudação com string vazia"""
        resultado = saudacao("")
        assert resultado == "Olá, visitante!"
    
    def test_saudacao_none(self):
        """Testa saudação com None"""
        resultado = saudacao(None)
        assert resultado == "Olá, visitante!"


class TestCalcularMedia:
    """Testes para a função calcular_media"""
    
    def test_media_notas_normais(self):
        """Testa cálculo de média com notas válidas"""
        notas = [8.0, 9.0, 7.0, 10.0]
        resultado = calcular_media(notas)
        assert resultado == 8.5
    
    def test_media_lista_vazia(self):
        """Testa cálculo com lista vazia"""
        resultado = calcular_media([])
        assert resultado == 0.0
    
    def test_media_uma_nota(self):
        """Testa cálculo com apenas uma nota"""
        resultado = calcular_media([7.5])
        assert resultado == 7.5
    
    def test_media_todas_iguais(self):
        """Testa cálculo com notas iguais"""
        notas = [8.0, 8.0, 8.0]
        resultado = calcular_media(notas)
        assert resultado == 8.0


class TestValidarEmail:
    """Testes para a função validar_email"""
    
    def test_email_valido(self):
        """Testa email válido padrão"""
        assert validar_email("aluno@fatec.sp.gov.br") is True
        assert validar_email("professor@fatec.sp.gov.br") is True
    
    def test_email_sem_arroba(self):
        """Testa email sem @"""
        assert validar_email("alunofatec.sp.gov.br") is False
    
    def test_email_vazio(self):
        """Testa email vazio"""
        assert validar_email("") is False
        assert validar_email(None) is False
    
    def test_email_sem_dominio(self):
        """Testa email sem domínio"""
        assert validar_email("aluno@") is False
    
    def test_email_sem_usuario(self):
        """Testa email sem usuário"""
        assert validar_email("@fatec.sp.gov.br") is False
    
    def test_email_multiplos_arrobas(self):
        """Testa email com múltiplos @"""
        assert validar_email("aluno@@fatec.sp.gov.br") is False


# =============================================================================
# TESTES DE INTEGRAÇÃO (Exemplo)
# =============================================================================

class TestIntegracao:
    """Testes de integração para validar o fluxo completo"""
    
    def test_fluxo_completo_aluno(self):
        """Simula um fluxo completo de processamento de aluno"""
        # Dados do aluno
        nome = "João Silva"
        email = "joao.silva@fatec.sp.gov.br"
        notas = [8.5, 9.0, 7.5, 8.0]
        
        # Valida dados
        assert validar_email(email) is True
        
        # Processa saudação
        mensagem = saudacao(nome)
        assert "João Silva" in mensagem
        
        # Calcula média
        media = calcular_media(notas)
        assert media == 8.25
        assert media >= 6.0  # Aprovado


# =============================================================================
# FIXTURES (Dados de teste reutilizáveis)
# =============================================================================

@pytest.fixture
def notas_aprovado():
    """Fixture com notas de aluno aprovado"""
    return [7.0, 8.0, 7.5, 8.5]


@pytest.fixture
def notas_reprovado():
    """Fixture com notas de aluno reprovado"""
    return [4.0, 5.0, 3.5, 5.5]


def test_usando_fixture_aprovado(notas_aprovado):
    """Exemplo de teste usando fixture"""
    media = calcular_media(notas_aprovado)
    assert media >= 6.0


def test_usando_fixture_reprovado(notas_reprovado):
    """Exemplo de teste usando fixture"""
    media = calcular_media(notas_reprovado)
    assert media < 6.0


# =============================================================================
# TESTES PARAMETRIZADOS (Múltiplos casos de teste)
# =============================================================================

@pytest.mark.parametrize("email,esperado", [
    ("aluno@fatec.sp.gov.br", True),
    ("prof@fatec.sp.gov.br", True),
    ("teste@gmail.com", True),
    ("invalido", False),
    ("@fatec.sp.gov.br", False),
    ("aluno@", False),
    ("", False),
])
def test_validar_email_parametrizado(email, esperado):
    """Testa múltiplos emails de uma vez"""
    assert validar_email(email) == esperado


if __name__ == "__main__":
    # Permite executar os testes diretamente: python tests/test_main.py
    pytest.main([__file__, "-v"])
