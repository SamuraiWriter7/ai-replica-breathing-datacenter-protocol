from pathlib import Path
import json
import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    (
        "Replica Agent",
        ROOT / "schemas" / "replica-agent.schema.json",
        ROOT / "examples" / "replica-agent.example.yaml",
    ),
    (
        "Replica Breathing Cycle",
        ROOT / "schemas" / "replica-breathing-cycle.schema.json",
        ROOT / "examples" / "replica-breathing-cycle.example.yaml",
    ),
    (
        "Promotion Policy",
        ROOT / "schemas" / "promotion-policy.schema.json",
        ROOT / "examples" / "promotion-policy.example.yaml",
    ),
    (
        "Staging Policy",
        ROOT / "schemas" / "staging-policy.schema.json",
        ROOT / "examples" / "staging-policy.example.yaml",
    ),
    (
        "Exhalation Record",
        ROOT / "schemas" / "exhalation-record.schema.json",
        ROOT / "examples" / "exhalation-record.example.yaml",
    ),
    (
        "Retention Rule",
        ROOT / "schemas" / "retention-rule.schema.json",
        ROOT / "examples" / "retention-rule.example.yaml",
    ),
    (
        "Repair Policy",
        ROOT / "schemas" / "repair-policy.schema.json",
        ROOT / "examples" / "repair-policy.example.yaml",
    ),
    (
        "Repair Loop",
        ROOT / "schemas" / "repair-loop.schema.json",
        ROOT / "examples" / "repair-loop.example.yaml",
    ),
    (
        "Repair Record",
        ROOT / "schemas" / "repair-record.schema.json",
        ROOT / "examples" / "repair-record.example.yaml",
    ),
]

def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_target(name: str, schema_path: Path, example_path: Path) -> None:
    print(f"[validate] {name}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(example), key=lambda e: e.path)

    if errors:
        for error in errors:
            path = ".".join(str(p) for p in error.path) or "<root>"
            print(f"[error] {path}: {error.message}")
        raise SystemExit(1)

    print(f"[ok] {example_path.name} is valid")


def main() -> None:
    for name, schema_path, example_path in VALIDATION_TARGETS:
        validate_target(name, schema_path, example_path)


if __name__ == "__main__":
    main()
