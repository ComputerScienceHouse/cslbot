from typing import IO
class SectionProxy:
  def __getitem__(self, key: str) -> str: ...
class Interpolation: ...
class ExtendedInterpolation(Interpolation): ...
class ConfigParser:
  def __init__(self, interpolation: Interpolation = None) -> None: ...
  def __getitem__(self, key: str) -> SectionProxy: ...
  def read_file(self, file: IO[str]) -> None: ...
