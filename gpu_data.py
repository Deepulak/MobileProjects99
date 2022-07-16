import GPUtil
from tabulate import tabulate

def graphics_info():
	gpus = GPUtil.getGPUs()
	list_gpus = []
	for gpu in gpus:
		gpu_id = gpu.id 	# GPU Id
		gpu_name = gpu.name # GPU Name
		gpu_load = f"{gpu.load*100}%" # Gpu usage
		gpu_free_memory = f"{gpu.memoryFree}MB" # free memory
		gpu_used_memory = f"{gpu.memoryUsed}MB" # used memory
		gpu_total_memory = f"{gpu.memoryTotal}MB" # total memory
		gpu_temperature = f"{gpu.temperature} C"   # Temperature
		gpu_uuid = gpu.gpu_uuid
		list_gpus.append((gpu_id, gpu_name, gpu_load,
			gpu_free_memory, gpu_used_memory, gpu_total_memory,
			gpu_temperature, gpu_uuid
		))

	return str(tabulate(list_gpus, headers=("id", "name", "load", "free memory",
		"used memory", "total memory", "temperature", "uuid"),
		tablefmt="pretty")) 


if __name__ == "__main__":
	print(graphics_info)	