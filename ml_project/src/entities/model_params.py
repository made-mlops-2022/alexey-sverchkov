from dataclasses import dataclass
from marshmallow_dataclass import class_schema
import yaml


@dataclass()
class ModelParams:
    model_type: str

ModelParamsSchema = class_schema(ModelParams)

def read_model_params(path):
    with open(path, "r") as fin:
        schema = ModelParamsSchema()
        return schema.load(yaml.safe_load(fin))
