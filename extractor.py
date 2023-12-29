def extract_text(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    
    for line in lines:
        if line.startswith("%PCAP_BEGIN%"):
            x = line.split("%")
            print(x[2])

filename = "log_1.txt" # replace with your file name
extract_text(filename)