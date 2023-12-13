from dataclasses import dataclass, field
from typing import List, Any
from data.field import Field
from icecream import ic

@dataclass
class Project:
    name: Field = Field("name", None, None, ["any"])
    version: Field = Field("version", None, "1.0.0", ["any"])
    description: Field = Field("description", None, None, ["any"])
    main: Field = Field("main", None, "index.js", ["any"])
    scripts: Field = Field("scripts", None, dict(), ["any"])
    keywords: Field = Field("keywords", None, list(), ["any"])
    author: Field = Field("author", None, None, ["any"])
    license: Field = Field("license", None, "GNU GPL", ["any"])
    dependencies: Field = Field("dependencies", None, dict(), ["any"])
    devDependencies: Field = Field("devDependencies", None, dict(), ["any"])

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value
    