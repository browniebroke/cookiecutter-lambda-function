#!/usr/bin/env python
import shutil
import sys
from importlib import import_module
from pathlib import Path


for package_name in sys.argv[1:]:
    print(f"Vendoring {package_name}")
    package = import_module(package_name)
    package_path = package.__path__[0]
    vendor_path = (Path(__file__) / ".." / ".." / "vendor").resolve()
    shutil.copytree(package_path, vendor_path / package_name)
