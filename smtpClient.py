import socket
#from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((mailserver, port))
        #print("Connected to the mail server")
    except Exception as e:
        #print("Error connecting to the mail server: ", e)
        exit()
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
     #print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mail_from = "MAIL FROM: <sk11321@example.com>\r\n"
    clientSocket.send(mail_from.encode())
    recv = clientSocket.recv(1024).decode()
    #print("Server response:", recv)
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcpt_to = "RCPT TO: <nyu@example.com>\r\n"
    clientSocket.send(rcpt_to.encode())
    recv = clientSocket.recv(1024).decode()
    #print("Server response:", recv)
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    data_cmd = "DATA\r\n"
    clientSocket.send(data_cmd.encode())
    recv = clientSocket.recv(1024).decode()
    #print("Server response:", recv)
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv = clientSocket.recv(1024).decode()
    #print("Server response:", recv)
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quit_cmd = "QUIT\r\n"
    clientSocket.send(quit_cmd.encode())
    recv = clientSocket.recv(1024).decode()
    #print("Server response:", recv)
    # Fill in end

    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')