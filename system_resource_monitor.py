# System Resource Monitor
import psutil
import platform
import time

def get_cpu_usage(interval=1):
    """
    Get current CPU usage percentage
    """
    return psutil.cpu_percent(interval=interval)

def get_memory_usage():
    """
    Get memory usage statistics
    """
    memory = psutil.virtual_memory()
    return {
        'total': memory.total / (1024**3),  # Convert to GB
        'used': memory.used / (1024**3),
        'available': memory.available / (1024**3),
        'percent': memory.percent
    }

def get_disk_usage(path='/'):
    """
    Get disk usage for a specific path
    """
    if platform.system() == 'Windows':
        path = 'C:\\'
    
    try:
        disk = psutil.disk_usage(path)
        return {
            'total': disk.total / (1024**3),
            'used': disk.used / (1024**3),
            'free': disk.free / (1024**3),
            'percent': disk.percent
        }
    except:
        return None

def print_system_stats():
    """
    Print comprehensive system statistics
    """
    print("\n=== SYSTEM RESOURCE MONITOR ===")
    print(f"System: {platform.system()} {platform.release()}")
    
    # CPU
    cpu = get_cpu_usage()
    print(f"\nCPU Usage: {cpu}%")
    
    # Memory
    mem = get_memory_usage()
    print(f"\nMemory Usage:")
    print(f"  Total: {mem['total']:.2f} GB")
    print(f"  Used: {mem['used']:.2f} GB")
    print(f"  Available: {mem['available']:.2f} GB")
    print(f"  Percentage: {mem['percent']}%")
    
    # Disk
    disk = get_disk_usage()
    if disk:
        print(f"\nDisk Usage:")
        print(f"  Total: {disk['total']:.2f} GB")
        print(f"  Used: {disk['used']:.2f} GB")
        print(f"  Free: {disk['free']:.2f} GB")
        print(f"  Percentage: {disk['percent']}%")

if __name__ == "__main__":
    print_system_stats()
