# SAM E51 Curiosity Nano Live Update Project

This repository contains three MPLAB X projects designed for live firmware updates on the SAM E51 Curiosity Nano Board using MPLAB. The live update process utilizes dual flash banks to perform firmware updates with minimal downtime.

## Project Overview

### MPLAB X Projects

- **Live Update Application**: The primary application that can be updated via UART using live update capabilities.
- **Bootloader**: A fail-safe bootloader that manages firmware updates, initially without device fuse configurations.
- **Bootloader with Fuses**: A copy of the bootloader project with fuses enabled, needed only for initial factory programming.

### Workflow

After initial setup, the device operates in a way that allows firmware updates without reprogramming device fuses. This method enables seamless live updates for future firmware releases.

## Setup and Usage

### 1. Initial Factory Programming

**Program the Bootloader with Fuses**: Program the device once using the bootloader with fuses to set up the required configurations for future live updates. This project is located within the e51_uart_fail_safe_bootloader folder and can be opened with e51_uart_fail_safe_bootloader\hex\sam_e51_cnano.X.production_fuses.hex

#### Merging Bootloader and Application

To create a single binary file that combines the bootloader and live update application, use the provided Python script below. **Update the paths** in the script to match your file locations.

```python
merge_script_paths.py

# Define file paths (update these paths as necessary)
bootloader_path = r"<path to repo>\e51_curiosity_uart_live_update\ame51_uart_live_update\firmware\sam_e51_cnano.X\dist\sam_e51_cnano\production\sam_e51_cnano.X.production.bin"
live_update_firmware_path = r"<path to repo>\e51_curiosity_uart_live_update\e51_uart_fail_safe_bootloader\firmware\sam_e51_cnano.X\dist\sam_e51_cnano\production\sam_e51_cnano.X.production.bin"
merge_script_path = r"<path to repo>\e51_curiosity_uart_live_update\btl_app_merge_bin.py"

...

```
## Program the Merged Binary

Once merged, use `btl_host.py` to program the merged binary to the device:

```bash
python btl_host.py -v -s -i COM5 -d same5x -a 0x00080000 -f btl_app_merged.bin
```

# Activate the Application

Press the SW2 switch on the SAM E51 Curiosity Nano Board to swap flash banks and execute the user application from the newly programmed bank.

# Fill Second Flash Bank

Use the live_update.py script to program a copy of the bootloader and live update application into the inactive bank:

``` bash
python live_update.py -v -i COM5 -d same5x -a 0x00080000 -f btl_app_merged.bin
```

## Future Firmware Updates

Subsequent application updates can be applied without reprogramming fuses:

# Run the Live Update

Use live_update.py to update the application firmware:

``` bash
python live_update.py -v -i COM5 -d same5x -a 0x00080000 -f btl_app_merged.bin
```

### Notes

Communication: This example uses UART SERCOM5 for communication between the SAM E51 Curiosity Nano Board and the host PC.
Fuse Programming: Device fuses are only required during initial programming.
Hardware: SAM E51 Curiosity Nano Evaluation Kit