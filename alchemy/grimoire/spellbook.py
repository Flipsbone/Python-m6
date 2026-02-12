
def record_spell(spell_name:str, ingredients:str) -> str:
    try:
        from alchemy.grimoire.validator import validate_ingredients
        result = validate_ingredients(ingredients)
        if result == "VALID":
            return f"Spell recorded: {spell_name} ({ingredients} - {result})"
        else:
            return f"Spell rejected: {spell_name} ({ingredients} - {result})"
    except Exception as e:
        return f"Error processing spell '{spell_name}': {e}"