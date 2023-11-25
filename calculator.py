import tkinter as tk

cidr_to_string = {
    "/0": "0.0.0.0",
    "/1": "128.0.0.0",
    "/2": "192.0.0.0",
    "/3": "224.0.0.0",
    "/4": "240.0.0.0",
    "/5": "248.0.0.0",
    "/6": "252.0.0.0",
    "/7": "254.0.0.0",
    "/8": "255.0.0.0",
    "/9": "255.128.0.0",
    "/10": "255.192.0.0",
    "/11": "255.224.0.0",
    "/12": "255.240.0.0",
    "/13": "255.248.0.0",
    "/14": "255.252.0.0",
    "/15": "255.254.0.0",
    "/16": "255.255.0.0",
    "/17": "255.255.128.0",
    "/18": "255.255.192.0",
    "/19": "255.255.224.0",
    "/20": "255.255.240.0",
    "/21": "255.255.248.0",
    "/22": "255.255.252.0",
    "/23": "255.255.254.0",
    "/24": "255.255.255.0",
    "/25": "255.255.255.128",
    "/26": "255.255.255.192",
    "/27": "255.255.255.224",
    "/28": "255.255.255.240",
    "/29": "255.255.255.248",
    "/30": "255.255.255.252",
    "/31": "255.255.255.254",
    "/32": "255.255.255.255"
}


def onRadioSelect():
    if ipv_type.get() == 6:
        mask_entry.config(state="disabled")
    else:
        mask_entry.config(state="normal")


def get_ipv4_class(ip_address):
    first_octet = int(ip_address.split('.')[0])

    if 1 <= first_octet <= 127:
        return "A"
    elif 128 <= first_octet <= 191:
        return "B"
    elif 192 <= first_octet <= 223:
        return "C"
    elif 224 <= first_octet <= 239:
        return "D (Multicast)"
    elif 240 <= first_octet <= 255:
        return "E (Reserved)"
    else:
        return "Invalid IP address"


def on_calculate():
    global ipv_type
    ipValue = entry.get()
    maskValue = mask_entry.get()
    if ipv_type.get() == 4:
        getResultIpV4(ipValue, maskValue)
    else:
        getResultIpV6(ipValue)


def getResultIpV4(ipValue, maskValue):
    result = ""
    ipv4Class = ""
    intIpAddress = list()
    ipAddress = ipValue.strip().split('.')
    maskInBinaryInt = list()
    networkAddress = list()
    broadcastAddress = list()

    if ipValue == "" or maskValue == "":
        result = "Blad w aplikacji"
        result_label.config(text=result)
        return

    if get_ipv4_class(ipValue) != "Invalid IP address":
        ipv4Class = get_ipv4_class(ipValue)

    if maskValue[0] == "/":
        maskInBinaryString = (cidr_to_string[maskValue]).strip().split('.')
    else:
        maskInBinaryString = maskValue.strip().split('.')

    for i in range(4):
        maskInBinaryInt.append(int(maskInBinaryString[i]))
        intIpAddress.append(int(ipAddress[i]))

    if checkIpV4Address(intIpAddress) or checkMask(maskValue):
        binaryIpAddress = [bin(int(octet))[2:].zfill(8) for octet in intIpAddress]
        binaryMask = [bin(octet)[2:].zfill(8) for octet in maskInBinaryInt]

        for i in range(4):
            inverted_mask = 255 - int(binaryMask[i], 2)
            broadcast_octet = int(binaryIpAddress[i], 2) | inverted_mask
            broadcastAddress.append(bin(broadcast_octet)[2:].zfill(8))
            network_octet = int(binaryMask[i], 2) & int(binaryIpAddress[i], 2)
            networkAddress.append(bin(network_octet)[2:].zfill(8))
        decimal_broadcast_address = [str(int(part, 2)) for part in broadcastAddress]
        decimal_network_address = [str(int(part, 2)) for part in networkAddress]

        decimal_network_addressString = ".".join(decimal_network_address)
        decimal_broadcast_addressString = ".".join(decimal_broadcast_address)
        result = (f"Adres sieci to: {decimal_network_addressString}\nAdres rozgloszeniowy to: {decimal_broadcast_addressString}\n"
                  f"Klasa IPv4 to: {ipv4Class}")
    else:
        result = f"Adres IP lub maska jest nieprawidlowa"

    result_label.config(text=result)


def checkIpV4Address(ipv4):
    if ipv4[0] != 0 and len(ipv4) == 4:
        for i in range(4):
            if not (0 <= ipv4[i] <= 255):
                return False
        return True
    return False


def checkMask(mask):
    if mask[0] == "/":
        cidr = int(mask[1:])
        return 0 <= cidr <= 32  # Sprawdzenie poprawności CIDR
    else:
        parts = mask.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit():
                return False
            value = int(part)
            if not (0 <= value <= 255):
                return False
        binary_mask = ''.join(format(int(x), '08b') for x in parts)
        if '01' in binary_mask.strip('0'):
            return False
        return True


def getResultIpV6(ipValue):
    ipv6String = ipValue.strip().split(":")
    result = ""
    ipv6OutPut = ""
    for i, hextet in enumerate(ipv6String):
        if hextet == "0000":
            ipv6String[i] = "0"
        elif len(hextet) > 1:
            ipv6String[i] = hextet.lstrip("0") or "0"
    for i in range(len(ipv6String)):
        if i == len(ipv6String) - 1:
            ipv6OutPut = ipv6OutPut + ipv6String[i]
        else:
            ipv6OutPut = ipv6OutPut + ipv6String[i] + ":"
    result = f"Skrocony ipv6 to: {ipv6OutPut}"
    result_label.config(text=result)


root = tk.Tk()
root.title("Kalkulator adresów sieciowych")
root.geometry("600x500")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

ipv_type = tk.IntVar()
ipv_type.set(4)  # Ustawienie domyślnej wartości na IPv4

ipv4_radio = tk.Radiobutton(frame, text="IPv4", variable=ipv_type, command=onRadioSelect, value=4, font=("Arial", 15))
ipv4_radio.grid(row=0, column=0)

ipv6_radio = tk.Radiobutton(frame, text="IPv6", variable=ipv_type, command=onRadioSelect, value=6, font=("Arial", 15))
ipv6_radio.grid(row=0, column=1)

address_label = tk.Label(frame, text="Adres IP:", font=("Arial", 15))
address_label.grid(row=1, column=0)

entry = tk.Entry(frame, font=("Arial", 15))
entry.grid(row=1, column=1)

mask_label = tk.Label(frame, text="Maska/CIDR:", font=("Arial", 15))
mask_label.grid(row=2, column=0)

mask_entry = tk.Entry(frame, font=("Arial", 15))
mask_entry.grid(row=2, column=1)

calculate_button = tk.Button(frame, text="Oblicz", command=on_calculate, font=("Arial", 15))
calculate_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(frame, text="Wynik obliczeń będzie wyświetlony tutaj.", font=("Arial", 15))
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
