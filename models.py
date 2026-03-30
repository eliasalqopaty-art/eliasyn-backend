class Patient:
    def __init__(self, patient_id, name, history):
        self.patient_id = patient_id
        self.name = name
        self.history = history

    def get_summary(self):
        return f"المريض: {self.name} - السجل: {self.history}"
