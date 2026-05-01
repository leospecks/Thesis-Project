import pandas as pd
from typing import Optional


def dataframe_to_latex(
    df: pd.DataFrame,
    caption: Optional[str] = None,
    label: Optional[str] = None,
    index: bool = True,
    column_format: Optional[str] = None,
    float_format: Optional[str] = None,
    escape: bool = True,
    longtable: bool = False,
) -> str:
    """
    Convert a pandas DataFrame into a LaTeX table string with centering
    and caption placed below the table.
    """
    df_to_export = df.copy()

    if float_format is not None:
        def _fmt(x):
            if isinstance(x, float):
                return format(x, float_format)
            return x
        df_to_export = df_to_export.map(_fmt)

    # Generate only tabular content (no caption/label here)
    latex_tabular = df_to_export.to_latex(
        index=index,
        escape=escape,
        column_format=column_format,
        longtable=longtable,
    )

    # If longtable, return as-is (caption handling differs there)
    if longtable:
        return latex_tabular

    # Build full LaTeX table with caption BELOW
    lines = []
    lines.append(r"\begin{table}[htbp]")
    lines.append(r"\centering")

    lines.append(latex_tabular)

    if caption:
        lines.append(rf"\caption{{{caption}}}")
    if label:
        lines.append(rf"\label{{{label}}}")

    lines.append(r"\end{table}")

    return "\n".join(lines)