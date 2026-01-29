def safe_test_name(name: str) -> str:
    return (
        name.replace(" ", "_")
            .replace("/", "_")
            .replace("\\", "_")
            .replace(":", "_")
            .replace("|", "_")
    )
