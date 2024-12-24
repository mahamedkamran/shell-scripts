import paramiko
import os
from datetime import datetime

# Configuration
LOCAL_FILE = "C:\\New folder\\testing_backup.txt"
REMOTE_HOST = "44.197.219.176"
REMOTE_USER = "ubuntu"
REMOTE_DIR = "/home/ubuntu/backup"
PRIVATE_KEY_PATH = "test.pem"
LOG_FILE = "backup_log.txt"

def log_message(message):
    """Logs messages with a timestamp to a file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] {message}\n")
    print(f"[{timestamp}] {message}")

def sftp_upload_file(local_file, remote_dir, sftp):
    """Uploads a single file to the remote directory using SFTP."""
    remote_path = os.path.join(remote_dir, os.path.basename(local_file)).replace("\\", "/")
    sftp.put(local_file, remote_path)
    log_message(f"Uploaded file: {local_file} to {remote_path}")

def perform_backup():
    """Performs the backup operation using SFTP."""
    try:
        log_message("Starting backup operation...")

        # Set up SSH client
        key = paramiko.RSAKey.from_private_key_file(PRIVATE_KEY_PATH)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(REMOTE_HOST, username=REMOTE_USER, pkey=key)

        # Set up SFTP client
        sftp = ssh.open_sftp()

        # Ensure remote directory exists
        try:
            sftp.listdir(REMOTE_DIR)
        except FileNotFoundError:
            sftp.mkdir(REMOTE_DIR)
            log_message(f"Created remote directory: {REMOTE_DIR}")

        # Upload file
        sftp_upload_file(LOCAL_FILE, REMOTE_DIR, sftp)

        log_message("Backup operation completed successfully.")
        sftp.close()
        ssh.close()

    except Exception as e:
        log_message(f"ERROR: Backup operation failed - {str(e)}")

if __name__ == "__main__":
    perform_backup()
