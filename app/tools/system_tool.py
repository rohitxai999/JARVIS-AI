import psutil


class SystemTool:


    def cpu_usage(self):

        return psutil.cpu_percent()


    def memory_usage(self):

        memory = psutil.virtual_memory()

        return memory.percent


    def disk_usage(self):

        disk = psutil.disk_usage("/")

        return disk.percent