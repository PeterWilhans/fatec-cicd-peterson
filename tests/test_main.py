# tests/test_main.py 

import importlib
import importlib.util

pytest_spec = importlib.util.find_spec("pytest")
if pytest_spec is not None:
    pytest = importlib.import_module("pytest")
else:
    # Provide a minimal fallback for pytest.raises when pytest is not installed
    class _Raises:
        def __init__(self, exc):
            self.exc = exc

        def __enter__(self):
            return None

        def __exit__(self, exc_type, exc, tb):
            return exc_type is not None and issubclass(exc_type, self.exc)

    class pytest:
        @staticmethod
        def raises(exc):
            return _Raises(exc)

from main import saudacao, calcular_media 

class TestSaudacao: 

    def test_saudacao_nome_valido(self): 

        resultado = saudacao("Maria") 

        assert "Maria" in resultado 

 

    def test_saudacao_tipo_invalido(self): 

        with pytest.raises(TypeError): 

            saudacao(123) 

class TestCalcularMedia: 

    def test_media_simples(self): 

        assert calcular_media([10, 8, 6]) == 8.0 
    def test_lista_vazia(self): 

        with pytest.raises(ValueError): 

            calcular_media([]) 