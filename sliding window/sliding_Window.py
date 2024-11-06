import time
import random

class Frame:
    def __init__(self, frame_no, data):
        self.frame_no = frame_no
        self.data = data
        self.acknowledged = False

def send_frames(frames, window_size, base):
    print("\n--- Sending Frames ---")
    for i in range(window_size):
        if base + i < len(frames) and not frames[base + i].acknowledged:
            print(f"Sent Frame {frames[base + i].frame_no}: {frames[base + i].data}")
    print("Frames sent, waiting for acknowledgments...\n")

def receive_frames(frames, window_size, base):
    print("\n--- Receiving Frames ---")
    for i in range(window_size):
        if base + i < len(frames) and not frames[base + i].acknowledged:
            # Simulate error with 20% probability
            if random.random() < 0.2:
                print(f"Received Frame {frames[base + i].frame_no}: {frames[base + i].data} [ERROR]")
                # Send NACK
                frames[base + i].acknowledged = False
            else:
                print(f"Received Frame {frames[base + i].frame_no}: {frames[base + i].data} [OK]")
                # Send ACK
                frames[base + i].acknowledged = True

def sliding_window_protocol():
    window_size = int(input("Enter window size: "))
    message = input("Enter a message to send: ")

    # Initialize frames
    frames = [Frame(i, message[i]) for i in range(len(message))]
    base = 0  # Start of the window

    while base < len(frames):
        # Send frames in the current window
        send_frames(frames, window_size, base)
       
        time.sleep(2)  # Simulate delay
       
        # Receive acknowledgments for the frames in the current window
        receive_frames(frames, window_size, base)
       
        # Slide the window: Move base to the first unacknowledged frame
        while base < len(frames) and frames[base].acknowledged:
            base += 1

        if base < len(frames):
            print("\nResending unacknowledged frames...\n")
            time.sleep(2)  # Simulate delay before resending

    print("\nAll frames sent and acknowledged!")

if __name__ == "__main__":
    sliding_window_protocol()
