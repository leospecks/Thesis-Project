from pathlib import Path


def save_tex_var(name, value, out_dir="../1_latex/1.6_variables", marker=False):
    """
    Save a single Python variable to its own .tex file.

    If marker=True, the value is wrapped in \\bluemarker{}.
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    file_path = out_dir / f"{name}.tex"

    value = str(value).strip()

    if marker:
        value = rf"\bluemarker{{{value}}}"

    file_path.write_text(value, encoding="utf-8")

    return file_path