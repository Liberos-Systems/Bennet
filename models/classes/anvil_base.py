import json
import python_jsonschema_objects as pjo
from common.common import ic

try:
    with open('models/schemes/anvil_base_schema.json', 'r') as file:
        schema = json.load(file)
except FileNotFoundError:
    ic("Error: Could not read the file 'models/schemes/anvil_base_schema.json'")
    schema = {}

main_builder = pjo.ObjectBuilder(schema)
main_namespace = main_builder.build_classes()
AnvilBase = main_namespace.AnvilBase

AnvilBase.scripts = []

scripts_builder = pjo.ObjectBuilder(schema['properties']['scripts']['items'])
scripts_namespace = scripts_builder.build_classes()
AnvilBase.scripts.append(scripts_namespace.Script())

repository_builder = pjo.ObjectBuilder(schema['properties']['repository'])
repository_namespace = repository_builder.build_classes()
repository_instance=repository_namespace.Repository()
AnvilBase.repository = repository_instance

