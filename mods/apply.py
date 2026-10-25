import pathlib
import sys

SRC = pathlib.Path("app/src/io/freemytv")

CLOCK12 = """package io.freemytv;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

final class Clock12 {
    private Clock12() {}

    static String format(long millis) {
        return new SimpleDateFormat("h:mm a", Locale.US).format(new Date(millis));
    }
}
"""

(SRC / "Clock12.java").write_text(CLOCK12, encoding="utf-8")

total = 0
for f in sorted(SRC.glob("*.java")):
    if f.name in ("Ui.java", "Clock12.java"):
        continue
    text = f.read_text(encoding="utf-8")
    n = text.count("Ui.clock(")
    if n:
        f.write_text(text.replace("Ui.clock(", "Clock12.format("), encoding="utf-8")
        total += n
        print(f"{f.name}: {n} cambio(s) de reloj")

if total == 0:
    sys.exit("ERROR: no encontre Ui.clock( en el codigo")
print("Reloj de 12 horas aplicado")
