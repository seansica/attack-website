from . import matrices
from . import matrices_config


def get_priority():
    return matrices_config.priority


def get_menu():
    return {
        "display_name": matrices_config.module_name,
        "module_name": matrices_config.module_name,
        "url": "/matrices/",
        "external_link": False,
        "priority": matrices_config.priority,
        "children": [],
    }


def run_module():
    return (matrices.generate_matrices(), matrices_config.module_name)
