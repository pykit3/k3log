from importlib.metadata import version

__version__ = version("k3log")

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
