class ApplicationLayer:
    def send(self, data):
        print("[Application Layer] Sending Data:", data)
        return f"AppData({data})"

    def receive(self, data):
        print("[Application Layer] Received Data:", data)
        return data.replace("AppData(", "").rstrip(")")

class PresentationLayer:
    def send(self, data):
        encoded_data = data.encode("utf-8").hex()  
        print("[Presentation Layer] Encoding Data:", encoded_data)
        return f"PresData({encoded_data})"

    def receive(self, data):
        hex_str = data.replace("PresData(", "").rstrip(")")
        decoded_data = bytes.fromhex(hex_str).decode("utf-8")
        print("[Presentation Layer] Decoding Data:", decoded_data)
        return decoded_data

class SessionLayer:
    def send(self, data):
        session_data = f"Session({data})" 
        print("[Session Layer] Managing Session:", session_data)
        return session_data

    def receive(self, data):
        session_data = data.replace("Session(", "").rstrip(")")
        print("[Session Layer] Session Retrieved:", session_data)
        return session_data

class TransportLayer:
    def send(self, data):
        transport_data = f"Transport({data})" 
        print("[Transport Layer] Segmenting Data:", transport_data)
        return transport_data

    def receive(self, data):
        transport_data = data.replace("Transport(", "").rstrip(")")
        print("[Transport Layer] Reassembling Segments:", transport_data)
        return transport_data

class NetworkLayer:
    def send(self, data):
        packet = f"Packet({data})"
        print("[Network Layer] Routing Packet:", packet)
        return packet

    def receive(self, data):
        packet = data.replace("Packet(", "").rstrip(")")
        print("[Network Layer] Packet Arrived:", packet)
        return packet

class DataLinkLayer:
    def send(self, data):
        frame = f"Frame({data})"
        print("[Data Link Layer] Creating Frame:", frame)
        return frame

    def receive(self, data):
        frame = data.replace("Frame(", "").rstrip(")")
        print("[Data Link Layer] Frame Received:", frame)
        return frame

class PhysicalLayer:
    def send(self, data):
        bits = ''.join(format(ord(i), '08b') for i in data)
        print("[Physical Layer] Transmitting Bits:", bits)
        return bits

    def receive(self, data):
        chars = ''.join(chr(int(data[i:i+8], 2)) for i in range(0, len(data), 8))
        print("[Physical Layer] Bits to Characters:", chars)
        return chars

def simulate_osi_transmission(data):
    app = ApplicationLayer()
    pres = PresentationLayer()
    sess = SessionLayer()
    trans = TransportLayer()
    net = NetworkLayer()
    data_link = DataLinkLayer()
    phys = PhysicalLayer()

    data = app.send(data)
    data = pres.send(data)
    data = sess.send(data)
    data = trans.send(data)
    data = net.send(data)
    data = data_link.send(data)
    data = phys.send(data)

    print("\n-Data Successfully Sent over Network-\n")

    data = phys.receive(data)
    data = data_link.receive(data)
    data = net.receive(data)
    data = trans.receive(data)
    data = sess.receive(data)
    data = pres.receive(data)
    data = app.receive(data)

    print("\nFinal Data at Receiver:", data)

print("--- OSI Model Simulation ---\n")
print("Initializing...\n")
print("...\n")
print("...\n")
print("...\n")
user_input = input("Enter a string: ")
simulate_osi_transmission(user_input)
