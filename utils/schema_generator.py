import json
from genson import SchemaBuilder
from typing import Dict, Any


def generate_flexible_schema(response_json: Dict[str, Any], output_file: str) -> Dict:
    """
    Генерирует гибкую JSON Schema из респонса API

    Args:
        response_json: JSON объект из response.json()
        output_file: Путь для сохранения схемы

    Returns:
        Сгенерированная схема
    """
    builder = SchemaBuilder()
    builder.add_object(response_json)
    schema = builder.to_schema()

    # Делаем схему более гибкой
    schema = make_schema_flexible(schema)

    # Сохраняем в файл
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(schema, f, indent=2, ensure_ascii=False)

    return schema


def make_schema_flexible(schema: Any) -> Any:
    """
    Рекурсивно убирает слишком строгие ограничения из схемы

    Удаляет:
    - enum (конкретные значения)
    - minItems/maxItems (ограничения размера массивов)
    - pattern (регулярные выражения для строк)
    """
    if isinstance(schema, dict):
        # Убираем строгие ограничения
        for strict_key in ['enum', 'minItems', 'maxItems', 'pattern']:
            if strict_key in schema:
                del schema[strict_key]

        # Рекурсивно обрабатываем вложенные структуры
        for key, value in schema.items():
            if isinstance(value, (dict, list)):
                schema[key] = make_schema_flexible(value)

    elif isinstance(schema, list):
        return [make_schema_flexible(item) for item in schema]

    return schema


def generate_schema_from_response(response, output_file: str) -> Dict:
    """
    Удобная функция которая принимает requests.Response объект

    Args:
        response: объект requests.Response
        output_file: путь для сохранения схемы

    Returns:
        Сгенерированная схема
    """
    return generate_flexible_schema(response.json(), output_file)