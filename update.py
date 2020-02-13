import subprocess

command = "find -type f"
command_list = command.split(' ')

out = subprocess.Popen(command_list,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

files = str(out.communicate()[0].decode('utf-8')).splitlines()

home = '/home/stelios/'

for versioned_file in files:
    if versioned_file.startswith('./.git'):
        continue
    home_file = home + versioned_file
    command = ['rsync', home_file, versioned_file]
    subprocess.Popen(command,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
