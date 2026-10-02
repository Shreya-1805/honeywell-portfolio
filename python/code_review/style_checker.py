"""Tiny automated code-review helper using ast.
Usage: python style_checker.py path/to/dir"""
import ast, sys, pathlib

MAX_FUNC_LINES = 40


def check_file(path: pathlib.Path):
    issues = []
    tree = ast.parse(path.read_text(), filename=str(path))
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if not ast.get_docstring(node):
                issues.append(f"{path}:{node.lineno} '{node.name}' missing docstring")
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            length = node.end_lineno - node.lineno + 1
            if length > MAX_FUNC_LINES:
                issues.append(f"{path}:{node.lineno} '{node.name}' too long ({length} lines)")
        if isinstance(node, ast.ExceptHandler) and node.type is None:
            issues.append(f"{path}:{node.lineno} bare except")
    return issues


if __name__ == "__main__":
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    found = [i for f in root.rglob("*.py") for i in check_file(f)]
    print("\n".join(found) or "No issues found")
    sys.exit(1 if found else 0)
