import json
import jsonschema
from jsonschema import validate
from jsonschema.validators import Draft7Validator

# Load the schema
with open("schema/business_loan_schema.v0.1.2.json", "r") as f:
    schema = json.load(f)

# Validate the schema itself
Draft7Validator.check_schema(schema)
print("Schema is valid!") 