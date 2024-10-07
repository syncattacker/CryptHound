#!/usr/bin/env python3

# Library Imports

import os
import psutil
import platform
import subprocess


# Check for virtualization environment.

def isVirtualEnv() -> bool :
    '''
    Returns True if executed inside a virtualized environment else False.
    Checks if /.dockerenv is present typically present in Docker containers. Additionally checks /proc/1/cgroup to look for indicators of containerization.
    For Linux Systems, checks /proc/cpuinfo the presence of string "Hypervisor" indicates that the system is running under a hypervisor.
    Trys to run dmidecode ( A Linux Utility ) to fetch the system manufacturer, which may return specific strings for VMs.
    If none of the indicators is found then returns it is running on Physical Machine
    '''
    if os.path.exists( "./dockerenv" ):

        return True
    
    try:
        with open( "/proc/cpuinfo", "r" ) as cpuinfo:
            if "hypervisor" in cpuinfo.read():
                return True
    except FileNotFoundError:
        pass

    if os.path.exists( "/proc/1/cgroup" ):
        try:
            with open( "/proc/1/cgroup", "r" ) as cgroup:
                if "docker" in cgroup.read() or "lxc" in cgroup.read():
                    return True
        except FileNotFoundError:
            pass

        if platform.system() == "Linux":
            try:
                execute = subprocess.check_output(["dmidecode", "-s", "system-manufacturer"], universal_newlines = True).strip()
                if execute in ["VMware, Inc.", "Microsoft Corporation", "innotek GmbH", "QEMU"]:
                    return True
            except ( subprocess.CalledProcessError, FileNotFoundError ):
                pass

        return False
    


def getInfoormation() -> dict :

    '''
    Returns the System Information (OS Details, CPU Information, Memory Information) if the device is not a virtual environment.
    '''

    osInfo = platform.uname()

    cpuInfo = {
        "Physical Cores" : psutil.cpu_count( logical = False ),
        "Total Cores" : psutil.cpu_count( logical = True ),
        "Frequency (MHz)" : psutil.cpu_freq().current,
        "CPU Usage (%)" : psutil.cpu_percent( interval = 1 ),
        "CPU Model" : platform.processor(),
    }

    ramInfo = {
        "Memory Available (GB)": f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB",
        "Memory Free (GB)": f"{psutil.virtual_memory().available / (1024 ** 3):.2f} GB",
        "Memory Used (GB)": f"{psutil.virtual_memory().used / (1024 ** 3):.2f} GB",
        "Memory Usage (%)": f"{psutil.virtual_memory().percent}%",
    }

    systemInfo = {
        "System Information": {
            "System": osInfo.system,
            "Release": osInfo.release,
            "Version": osInfo.version,
            "Machine": osInfo.machine,
            "Node Name": osInfo.node
        },
        "CPU Information": cpuInfo,
        "RAM Information": ramInfo,
    }

    return systemInfo


if __name__ == '__main__':
    if isVirtualEnv():
        print("Virtual Environment Detected. \nGetting back to original behaviour.")
    else:
        detail = getInfoormation()
        print(getInfoormation.__doc__)
