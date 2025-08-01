Huffman Encoding TCP/IP Communication

This project demonstrates a simple client-server communication system using Huffman encoding for message compression over TCP/IP sockets. It includes a command-line client, a Streamlit-based GUI client, and a server, all implemented in Python.

FEATURES
--------
- Huffman Encoding/Decoding: Efficiently compress and decompress messages using Huffman coding.
- TCP/IP Communication: Send and receive encoded messages between client and server.
- Text & File Support: Send plain text or the contents of a text file.
- Streamlit GUI: User-friendly web interface for sending messages.
- Logging: Client and server log all communication for auditing and debugging.

PROJECT STRUCTURE
-----------------
- server.py                    # TCP server
- client_cli.py                # CLI client
- client_gui_streamlit.py      # GUI client using Streamlit
- huffman_encoding_decoding.py # Huffman algorithm functions
- file.py                      # File reader utility
- client_log.txt               # Log file for client
- server_log.txt               # Log file for server
- test.txt                     # Sample text file

REQUIREMENTS
------------
- Python 3.7+
- Streamlit (`pip install streamlit`)

USAGE
-----
1. Start the Server:
   python server.py

2. Use the Command-Line Client:
   python client_cli.py

3. Use the Streamlit GUI Client:
   streamlit run client_gui_streamlit.py
   - Open the browser and use the interface to send a message or file.

HUFFMAN ENCODING/DECODING
--------------------------
Implemented in huffman_encoding_decoding.py via:
- huffman_encoding(text)
- huffman_decoding(encoded_text, tree)

LICENSE
-------
This project is for educational purposes.


