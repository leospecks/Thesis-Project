from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_time_series(
    df,
    column,
    output_path,
    label=None,
    color="green",
    start=None,
    end=None,
    ylabel=None,
    x_step_years=10,
    show=True
):
    series = df[column].copy()
    series.index = pd.to_datetime(series.index)
    series = series.sort_index()

    if start is not None:
        series = series.loc[pd.Timestamp(start):]

    if end is not None:
        series = series.loc[:pd.Timestamp(end)]

    series = series.dropna()

    if series.empty:
        raise ValueError(
            f"Column '{column}' contains no observations "
            "for the selected period."
        )

    x = series.index
    y = series.to_numpy()

    cm = 1 / 2.54

    fig, ax = plt.subplots(
        figsize=(7.8 * cm, 4.5 * cm),
        layout="constrained"
    )

    ax.plot(
        x,
        y,
        color=color,
        linewidth=1,
        label=label or column
    )

    ax.fill_between(
        x,
        y,
        0,
        color=color,
        alpha=0.1
    )

    ax.set_xlabel("Time")

    if ylabel is not None:
        ax.set_ylabel(ylabel)

    ax.legend(frameon=False)
    ax.grid(False)

    ax.spines["bottom"].set_position(("data", 0))
    ax.spines["left"].set_position(("axes", 0))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")

    ax.tick_params(
        axis="both",
        which="major",
        direction="inout",
        length=4,
        width=0.8
    )

    # Control the spacing of x-axis ticks
    if x_step_years is not None:
        ax.xaxis.set_major_locator(
            mdates.YearLocator(base=x_step_years)
        )
        ax.xaxis.set_major_formatter(
            mdates.DateFormatter("%Y")
        )
    else:
        locator = mdates.AutoDateLocator()
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(
            mdates.ConciseDateFormatter(locator)
        )

    ax.set_xlim(x.min(), x.max())
    ax.set_ylim(bottom=min(0, y.min()))

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig.savefig(
        output_path,
        bbox_inches="tight"
    )

    if show:
        plt.show()
    else:
        plt.close(fig)

    return fig, ax