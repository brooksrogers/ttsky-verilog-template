<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project implements a 4-bit binary counter
using Verilog.
## How to test

1. Set rst_n to 0 to reset the counter.
2. Set rst_n to 1 to release reset.
3. Set ui_in[0] to 1 to enable counting.
4. Apply clock pulses to clk.
5. Observe the count on uo_out[3:0].
6. Set ui_in[0] to 0 to pause counting.
7. Set rst_n to 0 to reset the counter.
## External hardware
No external hardware is required for simulation.
List external hardware used in your project (e.g. PMOD, LED display, etc), if any
