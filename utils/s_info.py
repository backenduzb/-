import psutil

async def get_server_info():
    cpu_utilization = f"{psutil.cpu_percent(interval=1)}%"
    ram = psutil.virtual_memory()
    ram_utilization = f"{ram.percent}%"
    return [cpu_utilization, ram_utilization]
    