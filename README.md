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

# Sychronously Tuned Filter

For each section:

Q = Qtot * sqrt(2^(1/n)-1)

or

BW = BWtot * sqrt(2^(1/n)-1)

For n = 3, 5, and 7, the sqrt term is: 0.6436, 0.3856, 0.3226

zeta = 2Q, so critically damped is Q = 0.5

So critically damped section Q for n = 3, 5, 7 is: 0.3218, 0.1928, 0.1613

For 10 MHz BWtot, BW for each section for n = 3, 5, 7 is: 6.436, 3.856, 3.226 MHz

A critically damped RLC LP filter has C = 1/(2R omega_0) and L = 2R/(omega_0).
So for 10 MHz and R = 50 ohms: C = 159.2p and L = 1.592u. That would seem to
give an input and output impedance of 100 ohms from Z = sqrt(L/C). Cutting the
total C in half across a pi network may help? But then this Pi network will
have the wrong BW and Q?
