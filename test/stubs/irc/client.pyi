class Event:
  def __init__(self, type: str, source: NickMask, target: str, arguments: List[str] = None, tags: List[str] = None) -> None: ...
  arguments = ... # type: List[str]
class NickMask(str): ...
class SimpleIRCClient: ...
class ServerConnection: ...
