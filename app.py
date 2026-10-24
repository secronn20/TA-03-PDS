from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from io import BytesIO
import base64
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(
    BASE_DIR, "data", "Food_Delivery_Times.csv"
)

DURATION_COL = "Delivery_Time_min"


def load_data():
    df = pd.read_csv(DATA_PATH)

    if DURATION_COL not in df.columns:
        raise ValueError(
            f"Kolom {DURATION_COL} tidak ditemukan."
        )

    durations = pd.to_numeric(
        df[DURATION_COL], errors="coerce"
    ).dropna()

    durations = durations[durations > 0]

    if durations.empty:
        raise ValueError(
            "Tidak ditemukan data durasi yang valid."
        )

    return df, durations.to_numpy(dtype=float)


def create_histogram(results, threshold, mean_value):
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.hist(
        results,
        bins=30,
        edgecolor="white",
        alpha=0.85
    )

    ax.axvline(
        threshold,
        linestyle="--",
        linewidth=2,
        label=f"Batas keterlambatan: {threshold:g} menit"
    )

    ax.axvline(
        mean_value,
        linestyle=":",
        linewidth=2,
        label=f"Mean: {mean_value:.2f} menit"
    )

    ax.set_title("Distribusi Hasil Simulasi Monte Carlo")
    ax.set_xlabel("Durasi Pengiriman (menit)")
    ax.set_ylabel("Frekuensi")
    ax.legend()

    fig.tight_layout()

    buffer = BytesIO()

    fig.savefig(
        buffer,
        format="png",
        dpi=130,
        bbox_inches="tight"
    )

    plt.close(fig)
    buffer.seek(0)

    return base64.b64encode(
        buffer.read()
    ).decode("utf-8")


@app.route("/", methods=["GET", "POST"])
def index():
    df, durations = load_data()

    stats_data = {
        "rows": len(df),
        "valid_count": len(durations),
        "mean": np.mean(durations),
        "std": np.std(durations, ddof=1),
        "median": np.median(durations),
        "min": np.min(durations),
        "max": np.max(durations),
    }

    threshold = 60.0
    iterations = 10000

    result = None
    error = None

    if request.method == "POST":
        try:
            threshold = float(
                request.form.get("threshold", 60)
            )

            iterations = int(
                request.form.get("iterations", 10000)
            )

            if threshold <= 0:
                raise ValueError(
                    "Batas keterlambatan harus lebih dari 0."
                )

            if not 5000 <= iterations <= 200000:
                raise ValueError(
                    "Iterasi harus antara 5.000 dan 200.000."
                )

            rng = np.random.default_rng(42)

            simulated = rng.choice(
                durations,
                size=iterations,
                replace=True
            )

            late_count = int(
                np.sum(simulated > threshold)
            )

            late_probability = (
                late_count / iterations
            ) * 100

            historical_probability = (
                np.mean(durations > threshold) * 100
            )

            simulated_mean = np.mean(simulated)

            histogram = create_histogram(
                simulated,
                threshold,
                simulated_mean
            )

            result = {
                "iterations": iterations,
                "threshold": threshold,
                "mean": simulated_mean,
                "std": np.std(simulated, ddof=1),
                "median": np.median(simulated),
                "late_count": late_count,
                "on_time_count": iterations - late_count,
                "late_probability": late_probability,
                "historical_probability": historical_probability,
                "difference": abs(
                    late_probability - historical_probability
                ),
                "histogram": histogram,
            }

        except (ValueError, TypeError) as exc:
            error = str(exc)

    return render_template(
        "index.html",
        stats=stats_data,
        result=result,
        error=error,
        threshold=threshold,
        iterations=iterations
    )


if __name__ == "__main__":
    app.run(debug=True)