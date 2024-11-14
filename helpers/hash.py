"""Returns a unique hash for a user based on their user ID and username.

Returns:
    str: A unique hash for the user.
"""
from hashlib import sha256


def get_user_hash(user_id: int, user_name: str) -> str:
    """
    Generates a unique hash for a user based on their user ID and username.

    Args:
        user_id (int): The unique identifier of the user.
        user_name (str): The username of the user.

    Returns:
        str: A SHA-256 hash representing the user's combined ID and username.
    """
    return sha256(f"{user_id}{user_name}".encode()).hexdigest()
