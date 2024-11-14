import subprocess
import os

# Define file paths (check that these paths are correct and that files exist in these locations)
bootloader_path = r"C:\Users\surface\Desktop\Saile Gauge\e51dev\same51_uart_live_update\firmware\sam_e51_cnano.X\dist\sam_e51_cnano\production\sam_e51_cnano.X.production.bin"
live_update_firmware_path = r"C:\Users\surface\Desktop\Saile Gauge\e51dev\same51_uart_live_update\firmware\sam_e51_cnano.X\dist\sam_e51_cnano\production\sam_e51_cnano.X.production.bin"
merge_script_path = r"C:\Users\surface\Desktop\Saile Gauge\utilities\btl_app_merge_bin.py"

# Check if each path exists and display an error if any are missing
if not os.path.isfile(bootloader_path):
    print(f"Error: Bootloader file not found at {bootloader_path}")
    exit(1)
if not os.path.isfile(live_update_firmware_path):
    print(f"Error: Application file not found at {live_update_firmware_path}")
    exit(1)
if not os.path.isfile(merge_script_path):
    print(f"Error: Merge script not found at {merge_script_path}")
    exit(1)

print("Bootloader path:", bootloader_path)
print("Live Update Firmware path:", live_update_firmware_path)
print("Merge script path:", merge_script_path)


# Construct and run the command with proper error handling
try:
    result = subprocess.run([
        "python", merge_script_path,
        "-o", "0x00002000",
        "-b", bootloader_path,
        "-a", live_update_firmware_path
    ], check=True, capture_output=True, text=True)

    print("Merging completed successfully.")
    print("Output:", result.stdout)

except subprocess.CalledProcessError as e:
    print("An error occurred during the merge process.")
    print("Error Message:", e.stderr)
    print("Command Output:", e.output)

except FileNotFoundError:
    print("The specified Python executable or script file was not found. Please check the paths.")



#python btl_app_merge_bin.py -o 0x2000 -b "C:\Users\surface\Desktop\Saile Gauge\e51dev\e51_uart_fail_safe_bootloader\hex\e51_uart_fail_safe_bootloader.production.bin" -a "C:\Users\surface\Desktop\Saile Gauge\e51dev\same51_uart_live_update\hex\same51_uart_live_update.production.bin"