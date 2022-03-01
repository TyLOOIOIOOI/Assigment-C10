
import PatientClass as pc
import ProcedureClass as prc

patient1 = pc.Patient(1, "Matt Jones", "123 Main st, Waco TX 76706", "254-555-7415", True)

practitioner1 = prc.Procedure("Physical Exam","2/15/2022","Dr. Irvine", 250, 1)
practitioner2 = prc.Procedure("MRI","2/15/2022","Dr. Hamilton", 1500, 1)
practitioner3 = prc.Procedure("CT Scan","2/17/2022","Dr. Drey", 1200, 2)

print("*** Patient Bill ***")
patient1.print_Patient() 
print()
practitioner1.print_Procedure()
print() 
practitioner2.print_Procedure()

total_charges = practitioner1.get_charges() + practitioner2.get_charges()
if patient1.get_vs() == True:
    total_charges = total_charges * .6

print()
print("Total Charge: $", format(total_charges,',.2f'))
