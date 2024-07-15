# Monitoring System for TeleICU Patients
TeleICU is an innovative solution designed for patient monitoring within hospital intensive care units,can assist the person or doctor available at the physical location and provides round the clock monitoring. 

# Objective
Intention behind developing such system is to avoid human errors and fulfill all type of requests by critical care patients with small number of medical staff.
# Workflow
![workflow](https://github.com/user-attachments/assets/155e5bd1-1771-4822-9f26-0a5ca52a4874)

# Program Execution
The working of the program is divided in two parts:​</br>
1)Person Detection		2)Motion Detection</br>
Person Detection:​</br>
This module is first executed , it will detect type of person present in the ICU , here we are using “face_detection” module for detection. The image of the doctors must be present in the “Doctor” folder before , for training.</br>

Motion Detection:​</br>
Alarm will be disabled if doctor is present in the room otherwise motion detection will get started and if any movements of the patient is detected then alarm will be enabled.​</br>
For more massive movement detection​ the value of "threshold.sum()" should be increased.​</br>
For alarm to to enabled for continuous movement the "alarm_counter" value can be increased.</br>

# Running tests

Test Video</br>
https://github.com/user-attachments/assets/d3c24faa-f238-48d9-9760-9b06f5c5579e
