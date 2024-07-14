import subprocess

c1=subprocess.run(['python',r'C:\Users\Balkrishna Bharti\Desktop\github\Monitoring-System-for-TeleICU-Patients\app.py'])
if c1:
    print("Doctor\t\t Alarm:Disabled")
else:
    print("To enable alarm press 't/T' :")
    subprocess.run(['python',r'C:\Users\Balkrishna Bharti\Desktop\github\Monitoring-System-for-TeleICU-Patients\obj_det.py'])
