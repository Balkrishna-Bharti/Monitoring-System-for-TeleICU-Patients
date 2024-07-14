# Monitoring System for TeleICU Patients
TeleICU is an innovative solution designed for patient monitoring within hospital intensive care units,can assist the person or doctor available at the physical location and provides round the clock monitoring. 

# Workflow
![workflow](https://github.com/user-attachments/assets/155e5bd1-1771-4822-9f26-0a5ca52a4874)

# Program Execution
"call.py" file is executed,which calls : <br/>
The file "app.py" is designed for face detection, specifically targeting the faces of doctors which must be pretrained. Images of the doctors should be stored in the "Doctor" folder. If a doctor is detected, the monitoring system will be disabled.<br/>
The "obj_det.py" file is invoked to detect patient movements, including attacks or movements of body parts.

# Running tests


