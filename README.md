# Abnormal Patterns in Continuous Patient Monitoring

**Student:** Sangeetha  
**Coursework:** Assignment 2 – Poster Presentation  
**Dataset:** eICU Collaborative Research Database Demo (v2.0.1), distributed by PhysioNet.

## Project overview
This project explores five routinely monitored ICU vital signs—heart rate (HR), oxygen saturation (SpO₂), mean arterial pressure (MAP), temperature, and respiratory rate—using exploratory data analysis (EDA). It examines missingness, duplicate timestamps, plausible ranges, IQR outliers, distributions, correlations, patient-level differences, and temporal patterns. A transparent rule-based flag summary is included as an educational extension.

## Repository structure
```text
Patient-Monitoring-Sangeetha/
├── README.md
├── data/
│   └── README.md
├── notebooks/
│   └── Patient_Monitoring_Sangeetha.ipynb
├── src/
│   └── monitoring.py
├── results/
│   └── README.md
├── models/
│   └── README.md
├── poster/
│   ├── Patient_Monitoring_Poster_Template.pdf
│   └── poster_content_template.txt
└── requirements.txt
```

## Dataset and access
The notebook downloads `vitalPeriodic.csv.gz` and `patient.csv.gz` from the eICU Demo v2.0.1 dataset hosted by PhysioNet, subject to availability and the dataset's terms. Raw data are deliberately not committed to this repository. See `data/README.md` and the source URL in the notebook.

## How to run
1. Create a Python environment and install dependencies: `pip install -r requirements.txt`.
2. Open `notebooks/Patient_Monitoring_Sangeetha.ipynb` in Jupyter or upload it to Google Colab.
3. Run all cells in order. If running locally, ensure the notebook's working directory is `notebooks/` so the relative `../results/` export path works.
4. Review the printed outputs and saved CSV summaries in `results/`.
5. Select the clearest figures from the notebook, save them in `results/`, and replace all poster placeholders with actual results from your run.

## Methods
- Data exploration and summary statistics.
- Missing-value and duplicate timestamp checks.
- Plausibility-range checks and IQR-based outlier analysis.
- Histograms, count plots, scatter plots, box plots, correlation heatmaps, pair plots, and time-series views.
- Patient-level aggregation for outcome comparisons to reduce row-level pseudoreplication.
- Rule-based threshold flags for descriptive purposes only.

## Important limitations
- The eICU Demo dataset is a limited demonstration sample and may not represent all ICU patients.
- Missing observations may reflect unavailable sensors or recording gaps.
- IQR outliers are not automatically errors; clinically important extreme readings should not be discarded without justification.
- The illustrative thresholds are not patient-specific clinical rules. This is not a medical device, diagnostic model, or validated real-time monitoring system.
- No trained machine-learning model is included in this project.

## Expected outputs
When the notebook runs successfully, the Assignment 1 cells produce analysis tables and figures. The Assignment 2 extension writes:
- `results/abnormal_flag_summary.csv`
- `results/patient_level_summary.csv`

Copy selected plots into `results/` manually if you want them tracked in GitHub. The repository contains templates only until the notebook is executed and results are reviewed.

## Citation
Pollard TJ, Johnson AEW, Raffa JD, Celi LA, Mark RG, Badawi O. The eICU Collaborative Research Database, a freely available multi-center database for critical care research. *Scientific Data*. 2018;5:180178. https://doi.org/10.1038/sdata.2018.178

Dataset: https://physionet.org/content/eicu-crd-demo/2.0.1/
