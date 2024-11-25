import os
import subprocess
from openpyxl import Workbook

# List of IP addresses to check
ip_addresses = [
    "8.8.8.8",    # Google DNS
    "1.1.1.1",    # Cloudflare DNS
    "192.168.1.1" # Local router (example)
]

# Create an Excel workbook and sheet
wb = Workbook()
ws = wb.active
ws.title = "Ping Status"

# Add headers
ws.append(["IP Address", "Status"])

# Ping each IP and record the status
for ip in ip_addresses:
    try:
        # Ping command based on OS
        command = ["ping", "-c", "1", ip] if os.name != "nt" else ["ping", "-n", "1", ip]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        status = "Success" if result.returncode == 0 else "Fail"
    except Exception as e:
        status = f"Error: {e}"
    ws.append([ip, status])

# Save the Excel file
output_file = "IP_Status_Report.xlsx"
wb.save(output_file)
print(f"Excel file saved as {output_file}")
