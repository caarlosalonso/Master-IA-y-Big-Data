train_notes = [[2.5, 5], [5, 10], [10, 20]]
model_approved = [estudiante for estudiante in train_notes if estudiante[0] >= 5 and estudiante[1] >= 10]
print(f"Estudiantes aprovados: {model_approved}")