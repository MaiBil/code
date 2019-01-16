"""
Patient / Doctor Scheduler - Create a patient class and a
doctor class. Have a doctor that can handle multiple patients
and setup a scheduling program where a doctor can only handle
16 patients during an 8 hr work day.
"""

class Doctor:

	def __init__(self, num_of_patients, work_day_hours):
		self.num_of_patients = num_of_patients
		self.work_day_hours = work_day_hours
		self.total_patients_can_handle = 2*work_day_hours


	def scheduling(self):
		if num_of_patients < total_patients_can_handle:
			return True
		else:
			appointment = False
			return False


class Patient:

	def __init__(self):
		pass


	def get_appointment(self, Doctor):
		if Doctor.scheduling():
			return True
		else:
			return False


DrMike = Doctor(10,8)
Steve = Patient(DrMike)

print(Steve.get_appointment())