import socket

script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/EdgeIY/infiniteyield/master/source"))()'
header = bytearray(16)
header[8:12] = (len(script) + 1).to_bytes(4, 'little')

with socket.create_connection(('127.0.0.1', 5553), timeout=3) as conn:
    conn.sendall(header + script.encode() + b'\0')
    print('F12 in Roblox to see script activity.')
