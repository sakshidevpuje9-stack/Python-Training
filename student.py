
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.fees_paid = 0
        self.attendance = []
        self.receipts = []

    def pay_fee(self, amount):
        self.fees_paid += amount
    

        receipt = {
            "receipt_no": len(self.receipts) + 1,
            "amount": amount
        }

        self.receipts.append(receipt)

    def mark_attendance(self, status):
        self.attendance.append(status)

    def get_student_report(self):
        total_classes = len(self.attendance)
        present = self.attendance.count("P")

        attendance_percent = (
            (present / total_classes) * 100
            if total_classes > 0 else 0
        )

        return {
            "Student ID": self.student_id,
            "Name": self.name,
            "Total Fees Paid": self.fees_paid,
            "Attendance %": round(attendance_percent, 2),
            "Receipts": self.receipts
        }



