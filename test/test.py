# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, Timer


@cocotb.test()
async def test_counter(dut):

    # Initialize inputs
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    # Start clock
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Verify reset
    await ClockCycles(dut.clk, 2)
    await Timer(1, unit="ns")
    assert int(dut.uo_out.value) == 0

    # Enable counter
    dut.rst_n.value = 1
    dut.ui_in.value = 1

    # Verify counting and overflow
    for expected in range(1, 20):
        await ClockCycles(dut.clk, 1)
        await Timer(1, unit="ns")

        actual = int(dut.uo_out.value)
        assert actual == expected % 16, (
            f"Expected {expected % 16}, got {actual}"
        )

    # Verify enable = 0 stops counting
    dut.ui_in.value = 0
    await ClockCycles(dut.clk, 3)
    await Timer(1, unit="ns")
    assert int(dut.uo_out.value) == 3

    # Verify asynchronous reset
    dut.rst_n.value = 0
    await Timer(1, unit="ns")
    assert int(dut.uo_out.value) == 0

    # Verify unused bidirectional pins
    assert int(dut.uio_out.value) == 0
    assert int(dut.uio_oe.value) == 0
