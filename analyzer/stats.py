import numpy as np

def compute_basic_stats(students):
    # 1. Extract PUC GPA into a 1D array
    puc_gpas = np.array([s['PUC_GPA'] for s in students])

    # 2. Extract subject GPAs into a 2D array
    maths = np.array([s['Maths_GPA'] for s in students])
    physics = np.array([s['Physics_GPA'] for s in students])
    chem = np.array([s['Chem_GPA'] for s in students])
    subjects = np.column_stack((maths, physics, chem)) # shape (2597, 3)

    # 3. Compute statistics 
    puc_mean = np.mean(puc_gpas)
    puc_max = np.max(puc_gpas)
    puc_min = np.min(puc_gpas)
    puc_std = np.std(puc_gpas)

    subject_means = list(np.mean(subjects,axis=0)) # average per subject

    above_9_count = np.sum(puc_gpas >= 9.0) # boolean mask + sum (True=1, False=0)
    below_7_count = np.sum(puc_gpas < 7.0)

    return {
        'total_students': len(students),
        'puc_mean' : puc_mean,
        'puc_max': puc_max,
        'puc_min': puc_min,
        'puc_std': puc_std,
        'subject_means': subject_means,
        'above_9_count': above_9_count,
        'below_7_count': below_7_count
    }

def get_campus_summary(students):
    # We'll use a simple dictionary to group
    campuses = {}
    for s in students:
        c = s['Campus']
        if c not in campuses:
            campuses[c] = [] # start a list of GPAs for this campus
        campuses[c].append(s['PUC_GPA'])

    summary = {}
    for c, gpas in campuses.items():
        gpa_array = np.array(gpas)
        summary[c] = {
            'count': len(gpa_array),
            'avg_puc_gpa': np.mean(gpa_array),
            'max_puc_gpa': np.max(gpa_array),
            'min_puc_gpa': np.min(gpa_array)
        }
    return summary





