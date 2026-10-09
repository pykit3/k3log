from .log import (
    add_std_handler,
    deprecate,
    get_datefmt,
    get_fmt,
    get_root_log_fn,
    make_file_handler,
    make_formatter,
    make_logger,
    set_logger_level,
    stack_format,
    stack_list,
    stack_str,
)

__all__ = [
    "add_std_handler",
    "deprecate",
    "get_datefmt",
    "get_fmt",
    "get_root_log_fn",
    "make_file_handler",
    "make_formatter",
    "make_logger",
    "set_logger_level",
    "stack_format",
    "stack_list",
    "stack_str",
]


def __getattr__(name: str) -> str:
    # importlib.metadata takes about 20 ms to import, so it is loaded only
    # when __version__ is read
    if name != "__version__":
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    from importlib.metadata import version

    return version("k3log")
