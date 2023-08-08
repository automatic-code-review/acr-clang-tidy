import json
import os
import jsonschema
import sys

from src import review


def load_config(path):
    with open(path, "r") as arquivo:
        config = json.load(arquivo)
    return config


def load_schema(path):
    with open(path, "r") as schema_file:
        schema = json.load(schema_file)
    return schema


def validate_config(config, schema):
    try:
        jsonschema.validate(config, schema)
    except jsonschema.exceptions.ValidationError as error:
        if "minLength" in error.validator:
            field_name = error.path[-1]
            new_error_message = f"O campo '{field_name}' não pode estar vazio."
            print(f"Erro validando config.json [ACR-CLANG-TIDY]: {new_error_message}")
        else:
            print(
                f"Erro validando config.json [ACR-CLANG-TIDY]: {error.path} {error.message}"
            )
        sys.exit(1)


def write_json_output(data, path):
    with open(path, "w") as arquivo:
        json.dump(data, arquivo, ensure_ascii=False, indent=True)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_config = os.path.join(current_dir, "config.json")
    path_schema_config = os.path.join(current_dir, "config-schema.json")

    schema = load_schema(path_schema_config)
    config = load_config(path_config)

    validate_config(config, schema)

    comments = review.review(config)
    path_output = config["path_output"]

    write_json_output(comments, path_output)
