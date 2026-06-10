from app.tools.calculator_tool import calculator_tool
from app.tools.text_stats_tool import text_stats_tool

def test_calculator():
    result = calculator_tool("20/5")
    assert result==4

def test_text_stats():
    result = text_stats_tool("Learning is fun")
    assert result['words']==3