import psutil

def suspicious_process_detector():
    for process in psutil.process_iter(['pid', 'name', 'username']):
        user = process.info['username']
        user_label = 'ADMIN' if user in ['root', 'Administrator'] else 'USER'
        print(f"Process: {process.info['name']}, PID: {process.info['pid']}, User: {user_label}")


suspicious_process_detector()