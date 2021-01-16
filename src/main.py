import subprocess
import time

site = "steampowered.com"

def runPing():
	p = subprocess.Popen(["ping", site, "-i", "0.2"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	while 1 == 1:
		retcode = p.poll()
		line = p.stdout.readline()
		yield line
		if retcode is not None:
			break

for line in runPing():
	print("\x1b[2K", end="", flush=True)
	print("\x1b[20D", end="", flush=True);
	if len(line.split()) < 8: continue
	ms = ((str(line).split()[7]).split("=")[1])
	if not "." in ms:
		ms += ".0"
	print(ms, end="", flush=True)
	print("ms", end="", flush=True)
	#time.sleep(0.3)
