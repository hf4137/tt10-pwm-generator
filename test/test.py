# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, Timer


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 ns (100 MHz)
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5) 
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 5)

    #
    # Increase duty cycle 10 times
    #
    
    dut._log.info("Increasing duty cycle…")

    for _ in range(10):
        dut.ui_in[0].value = 1      # increase duty
        await Timer(25, units="ns")
        dut.ui_in[0].value = 0
        await Timer(25, units="ns")

    #
    # Decrease duty cycle 10 times
    #

    dut._log.info("Decreasing duty cycle…")

    for _ in range(10):
        dut.ui_in[1].value = 1      # decrease duty
        await Timer(25, units="ns")
        dut.ui_in[1].value = 0
        await Timer(25, units="ns")

    #
    # Allow time to observe PWM output
    #
    
    await ClockCycles(dut.clk, 200)

    dut._log.info("PWM generator cocotb test completed")
