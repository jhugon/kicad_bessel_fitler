# LC Bessel Filter in KiCAD

3th order Pi filter with 50 ohm in/out impedance

E24 series caps seems available as 1% 1206.

Coilcraft makes variable inductors and fixed 1206CS series in E12 values.

From SPICE studies on 10 MHz, it seems that even 5% values for all components
will be fine. There is already a bit of ripple at the end of the impulse
response, and the component variation is smaller than the ripple.

I'm going to make a main branch with a variable inductor as well as another
branch with a 1206CS fixed inductor.

## For 6 MHz

27 ns time const and 58 ns rise time

- L1 = 1u287
- C1 = 179p
- C2 = 1n169

Parts:

- L1 = 143-18J12L (unshielded over 1 uH)
- C1 = 180p
- C2 = 1200p

## 10 MHz

16 ns time const and 35 ns rise time.

- L1 = 772n3
- C1 = 107p4
- C2 = 701p4

Parts:

- L1 = 143-17J12SL
- C1 = 110p
- C2 = 680p

## 20 MHz

8 ns time const and 16 ns rise time

- L1 = 386n2
- C1 = 53p70
- C2 = 350p7

Parts:

- L1 = 143-09J12SL
- C1 = 56p
- C2 = 360p

## 40 MHz

4 ns time const and 8.8 ns rise time

- L1 = 193n1
- C1 = 26p85
- C2 = 175p3

Parts:

- L1 = 144-07J12SL
- C1 = 27p
- C2 = 180p
