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
    Convert a pandas DataFrame into a LaTeX table fitted to \\textwidth.
    Uses tabularx so text columns wrap nicely and the table spans the page width.
    Caption is placed above the table.
    """
    df_to_export = df.copy()

    if float_format is not None:
        def _fmt(x):
            if isinstance(x, float):
                return format(x, float_format)
            return x

        df_to_export = df_to_export.map(_fmt)

    if longtable:
        return df_to_export.to_latex(
            index=index,
            escape=escape,
            column_format=column_format,
            longtable=True,
        )

    ncols = len(df_to_export.columns) + int(index)

    if column_format is None:
        # First column wraps; remaining columns right-aligned
        column_format = "X" + "r" * (ncols - 1)

    latex_tabular = df_to_export.to_latex(
        index=index,
        escape=escape,
        column_format=column_format,
    )

    latex_tabular = latex_tabular.replace(
        rf"\begin{{tabular}}{{{column_format}}}",
        rf"\begin{{tabularx}}{{\textwidth}}{{{column_format}}}"
    )

    latex_tabular = latex_tabular.replace(
        r"\end{tabular}",
        r"\end{tabularx}"
    )

    lines = []
    lines.append(r"\begin{table}[htbp]")
    lines.append(r"\centering")

    if caption:
        lines.append(rf"\caption{{{caption}}}")
    if label:
        lines.append(rf"\label{{{label}}}")

    lines.append(latex_tabular)
    lines.append(r"\end{table}")

    return "\n".join(lines)