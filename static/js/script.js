```javascript
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("simulation-form");
    const button = document.getElementById("run-button");
    const results = document.getElementById("results");

    // Menampilkan status ketika simulasi dijalankan
    if (form && button) {
        form.addEventListener("submit", function (event) {
            const iterations = Number(
                document.getElementById("iterations").value
            );

            const threshold = Number(
                document.getElementById("threshold").value
            );

            if (
                !Number.isInteger(iterations) ||
                iterations < 5000 ||
                iterations > 200000
            ) {
                event.preventDefault();

                alert(
                    "Jumlah iterasi harus antara 5.000 dan 200.000."
                );

                return;
            }

            if (!Number.isFinite(threshold) || threshold <= 0) {
                event.preventDefault();

                alert(
                    "Batas keterlambatan harus lebih besar dari 0."
                );

                return;
            }

            button.disabled = true;

            button.innerHTML =
                "<span>Menjalankan simulasi...</span>" +
                "<span>⏳</span>";
        });
    }

    // Jika hasil sudah tersedia, arahkan layar ke bagian hasil
    if (results) {
        results.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }
});
```