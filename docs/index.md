# k3log

[![Action-CI](https://github.com/pykit3/k3log/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3log/actions/workflows/python-package.yml)
[![Documentation Status](https://readthedocs.org/projects/k3log/badge/?version=stable)](https://k3log.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3log)](https://pypi.org/project/k3log)

A collection of log utilities for Python logging. Provides helpers for creating loggers, formatters, and file handlers with sensible defaults.

k3log is a component of [pykit3](https://github.com/pykit3) project: a python3 toolkit set.

## Installation

```bash
pip install k3log
```

## Quick Start

```python
import k3log

# Create a logger with default settings
logger = k3log.make_logger('/tmp/myapp')
logger.info('Hello World')

# Add stdout handler to root logger
k3log.add_std_handler(logger)

# Create file handler
handler = k3log.make_file_handler('/tmp/myapp.log')
logger.addHandler(handler)

# Get stack trace as formatted string
stack = k3log.stack_str()
logger.debug('Stack trace: %s', stack)
```

## API Reference

::: k3log

## License

The MIT License (MIT) - Copyright (c) 2015 Zhang Yanpo (张炎泼)
