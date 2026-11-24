import os

ENTRY = "calendar-vampire"


def output_path():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, "entry.txt")


def write_entry():
    # One word for the boss, written exactly as entered: it only ever
    # appears after dark, in meetings nobody agreed to attend.
    if not ENTRY.strip():
        raise SystemExit("entry must not be blank")
    with open(output_path(), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    write_entry()
