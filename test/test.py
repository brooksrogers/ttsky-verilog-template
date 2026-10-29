# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, Timer


@cocotb.test()
async def test_counter(dut):

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    await ClockCycles(dut.clk, 2)
    await Timer(100, unit="ns")
    assert int(dut.uo_out.value) == 0

    # Release reset and enable counting
    dut.rst_n.value = 1
    dut.ui_in.value = 1

    # Count through overflow
    for expected in range(1, 20):
        await ClockCycles(dut.clk, 1)
        await Timer(100, unit="ns")

        actual = int(dut.uo_out.value)
        dut._log.info(
            f"Expected {expected % 16}, got {actual}"
        )
        assert actual == expected % 16

    # Disable counter
    dut.ui_in.value = 0
    await ClockCycles(dut.clk, 3)
    await Timer(100, unit="ns")
    assert int(dut.uo_out.value) == 3

    # Asynchronous reset
    dut.rst_n.value = 0
    await Timer(100, unit="ns")
    assert int(dut.uo_out.value) == 0

    # Unused I/O
    assert int(dut.uio_out.value) == 0
    assert int(dut.uio_oe.value) == 0
