from .ankes import register as register_ankes
from .com import register as register_com

__all__ = ["register"]

def register(client):
    register_ankes(client)
    register_com(client)