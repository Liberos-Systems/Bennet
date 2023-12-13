from dataclasses import dataclass, field
from typing import Callable, Union, List, Any

@dataclass
class Field:
    name: str
    value: Any = None
    default_value: Union[Any, Callable[[], Any]] = None
    allowed_values: List[Any] = field(default_factory=list)
    