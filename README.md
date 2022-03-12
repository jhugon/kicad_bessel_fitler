# LC Bessel Filter in KiCAD

5th order Pi filter

## For 5 MHz

See schematic for component values

Resonant frequencies:

- L1C1 = 16.8 MHz
- L1C2 = 7.82 MHz
- L2C2 = 5.29 MHz
- L2C3 = 3.15 MHz

Finding trimmable L2=1u77 is a problem, since Coilcraft's don't go much over
1u.

## 9.82 MHz

16 ns time const and 36 ns rise time.

This seems to be the minumum freq you can do with a 5th order LP fitler and keep L2 <= 900n.

- C1 = 56p50
- L1 = 411n0
- C2 = 260p6
- L2 = 900n3
- C3 = 732p0

Resonant frequencies:

C1L1 = 33.0 MHz
C2L1 = 15.4 MHz
C2L2 = 10.4 MHz
C3L2 = 6.20 MHz

Parts:

- L1 = Coilcraft 143-10J12SL
- L2 = Coilcraft 143-20J12SL
- C1 = 56p
- C2 = 270p
- C3 = 750p
