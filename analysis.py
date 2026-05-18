import numpy as np
import matplotlib.pyplot as plt


# ==========================
# LOAD DATA
# ==========================
headers = np.genfromtxt(
    "./data/student_data.csv",
    delimiter=",",
    dtype=str,
    max_rows=1
)

student_data = np.genfromtxt(
    "./data/student_data.csv",
    delimiter=",",
    skip_header=1,
    dtype=str
)

G3_col = student_data[:, 32].astype(int)

print("===== STUDENT PERFORMANCE ANALYSIS =====")


# ==========================
# STUDYTIME ANALYSIS
# ==========================
print("\n===== STUDYTIME ANALYSIS =====")

studytime_col = student_data[:, 13].astype(int)

for level in [1, 2, 3, 4]:
    avg = np.mean(G3_col[studytime_col == level])
    print(f"Studytime {level}: {avg:.2f}")


# ==========================
# FAILURES ANALYSIS
# ==========================
print("\n===== FAILURES ANALYSIS =====")

fail_col = student_data[:, 14].astype(int)

for level in [0, 1, 2, 3]:
    avg = np.mean(G3_col[fail_col == level])
    std = np.std(G3_col[fail_col == level])

    print(f"Failures {level} Mean: {avg:.2f}")
    print(f"Failures {level} Std : {std:.2f}")


# ==========================
# GENDER ANALYSIS
# ==========================
print("\n===== GENDER ANALYSIS =====")

sex_col = student_data[:, 1]

for gender in ["M", "F"]:
    avg = np.mean(G3_col[sex_col == gender])
    print(f"{gender}: {avg:.2f}")


# ==========================
# ABSENCES ANALYSIS
# ==========================
print("\n===== ABSENCES ANALYSIS =====")

absences_col = student_data[:, 29].astype(int)

ranges = [(0, 5), (6, 10), (11, 15), (16, 100)]

for low, high in ranges:
    mask = (absences_col >= low) & (absences_col <= high)
    avg = np.mean(G3_col[mask])
    print(f"{low}-{high}: {avg:.2f}")


# ==========================
# GOOUT ANALYSIS
# ==========================
print("\n===== GOOUT ANALYSIS =====")

goout_col = student_data[:, 25].astype(int)

for level in [1, 2, 3, 4, 5]:
    avg = np.mean(G3_col[goout_col == level])
    print(f"Level {level}: {avg:.2f}")


# ==========================
# HIGHER EDUCATION ANALYSIS
# ==========================
print("\n===== HIGHER EDUCATION ANALYSIS =====")

higher_col = student_data[:, 20]

for option in ["yes", "no"]:
    avg = np.mean(G3_col[higher_col == option])
    std = np.std(G3_col[higher_col == option])

    print(f"{option} Mean: {avg:.2f}")
    print(f"{option} Std : {std:.2f}")


# ==========================
# INTERNET ANALYSIS
# ==========================
print("\n===== INTERNET ANALYSIS =====")

internet_col = student_data[:, 21]

for option in ["yes", "no"]:
    avg = np.mean(G3_col[internet_col == option])
    std = np.std(G3_col[internet_col == option])

    print(f"{option} Mean: {avg:.2f}")
    print(f"{option} Std : {std:.2f}")


# ==========================
# SCHOOL SUPPORT ANALYSIS
# ==========================
print("\n===== SCHOOL SUPPORT ANALYSIS =====")

schoolsup_col = student_data[:, 15]

for option in ["yes", "no"]:
    avg = np.mean(G3_col[schoolsup_col == option])
    print(f"{option}: {avg:.2f}")


# ==========================
# FINAL FINDINGS
# ==========================
print("\n===== FINAL FINDINGS =====")
print("1. Failures had the strongest negative impact on grades")
print("2. Higher education aspiration showed strong positive effect")
print("3. Internet access showed moderate positive effect")
print("4. Other factors showed weaker influence")