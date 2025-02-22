class ProjectConfigurationNotFound(Exception):
    """
    Exception raised when the pyproject.toml is unavailable

    Attributes:
        message (str): The error message
    """

    def __init__(self, message: str = "Can not find pyproject.toml"):
        super().__init__(message)
