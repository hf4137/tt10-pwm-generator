<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

The Pulse Width Modulation Generator consists of, multiplexers, counters, storage registers, and flip flops for different purposes. The inputs inc_duty and dec_duty are designed to control the duty cycle at some specified resolution. The resolution of this design is 10. This means that there is 11 possible duty cycle values (10% * n, where n is an integer that can range from 0 to 10). these inputs are fed into two flip flops each that "debounce" the button inputs if implemented on an FPGA. Then the output of those flip flops is sent to a sequence of logic that will increment a 4-bit value that countains the current duty cycle. A counter that increments every clock cycle is compared against this stored value in a multiplexer. If the duty value is greater than the current counter value, the multiplexer outputs a 1, otherwise its a 0. This value is the PWM output.

## How to test

You test it by running all possible inputs and checking if the outputs match the expected values. Refer to the truth table of the PWM_Generator below

| Clk | Counter_PWM | inc_duty | dec_duty | PWM_OUT | DUTY%      | 
|-----|-------------|----------|----------|---------|------------| 
| ^   | x>DUTY      | 0        |  0       |  0      | DUTY%      |
| ^   | x<DUTY      | 0        |  0       |  1      | DUTY%      | 
| ^   | x>DUTY      | ^        |  0       |  0      | DUTY% + 10%|
| ^   | x<DUTY      | ^        |  0       |  1      | DUTY% + 10%|
| ^   | x>DUTY      | 0        |  ^       |  0      | DUTY% - 10%|
| ^   | x<DUTY      | 0        |  ^       |  1      | DUTY% - 10%|

## External hardware

List external hardware used in your project (e.g. PMOD, LED display, etc), if any
NONE 

## Pinout 

### Inputs 

| Pin     | Name          | 
|---------|---------------| 
| ui[0]   | inc_duty      | 
| ui[1]   | dec_duty      | 
| ui[2]   |               | 
| ui[3]   |               |
| ui[4]   |               |
| ui[5]   |               |
| ui[6]   |               |
| ui[7]   |               | 

### Outputs 

| Pin     | Name          | 
|---------|---------------| 
| uo[0]   | PWM_OUT       |   
| uo[1]   |               |   
| uo[2]   |               |   
| uo[3]   |               |   
| uo[4]   |               |
| uo[5]   |               |
| uo[6]   |               |
| uo[7]   |               |
