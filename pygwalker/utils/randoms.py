import string
import secrets


def rand_str(n: int = 8, options: str = string.ascii_letters + string.digits) -> str:
    return ''.join(secrets.SystemRandom().sample(options, n))
