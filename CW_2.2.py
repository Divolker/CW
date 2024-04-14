def total_bytes(obj):
    from pathlib import Path
    file_path = Path(obj)
    return file_path.stat().st_size
print(total_bytes("New"))