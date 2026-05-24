# PDAC-AgenticNet

Machine learning based pharmacogenomic drug-response prediction for pancreatic ductal adenocarcinoma (PDAC).

## Clean Folder Structure

```text
DengueScope/
│
├── README.md
├── requirements.txt
├── environment.yml
│
├── data/
│   ├── raw/
│   │   ├── pan_data.csv
│   │   ├── shrunk_biomarker_validation.csv
│   │   └── shrunk_crispr_validation.csv
│   └── processed/
│       ├── processed_drug_data (2).csv
│       └── scaled_Data.csv
│
├── src/
│   ├── preprocessing.py
│   ├── model.py
│   ├── train.py
│   └── evaluate.py
│
├── notebooks/
│   └── experiments.ipynb
│
├── results/
│   ├── tables/
│   │   ├── dataset_summary.csv
│   │   └── performance_metrics.csv
│   ├── figures/
│   │   ├── fig1.png
│   │   ├── fig2.png
│   │   └── ...
│   └── logs/
│
├── models/
│   └── best_model.pkl
│
└── docs/
    └── methodology.md
```

## Dataset

- Source: PDAC pharmacogenomic drug-response dataset with external CCLE/DepMap biomarker and CRISPR validation subsets.
- Samples:
  - Discovery dataset: 2,223 rows
  - Processed modeling dataset: 1,974 rows
  - External biomarker validation: 1,406 cell lines
  - External CRISPR validation: 1,208 cell lines
- Features: Drug metadata, target pathway, genomic feature name, IC50 response features, p-values, encoded categorical features, pathway score, and binary response label.
- Target: Drug response / sensitivity derived from `ic50_effect_size` and `Response_Label`.

Full dataset summary:

| Dataset | Samples | Features | File |
|---|---:|---:|---|
| Discovery drug response data | 2,223 | 22 | `data/raw/pan_data.csv` |
| Processed drug response data | 1,974 | 16 | `data/processed/processed_drug_data (2).csv` |
| Scaled modeling data | 1,974 | 25 | `data/processed/scaled_Data.csv` |
| Biomarker validation data | 1,406 | 25 | `data/raw/shrunk_biomarker_validation.csv` |
| CRISPR validation data | 1,208 | 19 | `data/raw/shrunk_crispr_validation.csv` |

## Results

### Model Performance

| Model | Accuracy | Precision | Recall | F1-score | AUC |
|---|---:|---:|---:|---:|---:|
| Stacked Ensemble | 99.24% | - | - | - | 1.000 |
| Stacked Ensemble + ElasticNet | 99.49% | - | - | - | 1.000 |
| ElasticNet | 94.68% | 92.93% | 96.85% | 94.84% | - |
| RandomForest | 98.89% | 98.93% | 98.87% | 98.89% | - |
| XGBoost | 99.04% | 99.14% | 98.96% | 99.04% | - |
| MultiTask DNN | 93.72% | 89.92% | 98.48% | 94.00% | - |
| External CCLE Domain-Aligned Validation | 82.36% | - | - | - | 0.9183 |
| External CRISPR Validation | 78.64% | - | - | - | 0.8818 |

Complete metrics are available at:

- `results/tables/performance_metrics.csv`

### Regression / Advanced Model Results

| Model | R2 | MSE |
|---|---:|---:|
| ElasticNet | 0.9569 | 0.001404 |
| RandomForest | 0.9930 | 0.000234 |
| XGBoost | 0.9960 | 0.000132 |
| MultiTask DNN | 0.9467 | 0.001700 |
| GNN Edge Predictor | 0.9979 | 0.000073 |
| Bayesian Hierarchical Model | 0.3630 | 0.020842 |

## Visual Proof

All generated figures are stored in `results/figures/`.

| Figure | Preview |
|---|---|
| fig1 | ![fig1](results/figures/fig1.png) |
| fig2 | ![fig2](results/figures/fig2.png) |
| fig3 | ![fig3](results/figures/fig3.png) |
| fig4 | ![fig4](results/figures/fig4.png) |
| fig5 | ![fig5](results/figures/fig5.png) |
| fig6 | ![fig6](results/figures/fig6.png) |
| fig7 | ![fig7](results/figures/fig7.png) |
| fig8 | ![fig8](results/figures/fig8.png) |
| fig9 | ![fig9](results/figures/fig9.png) |
| fig10 | ![fig10](results/figures/fig10.png) |
| fig11 | ![fig11](results/figures/fig11.png) |
| fig12 | ![fig12](results/figures/fig12.png) |
| fig13 | ![fig13](results/figures/fig13.png) |
| fig14 | ![fig14](results/figures/fig14.png) |
| fig15 | ![fig15](results/figures/fig15.png) |
| fig16 | ![fig16](results/figures/fig16.png) |
| fig17 | ![fig17](results/figures/fig17.png) |
| fig18 | ![fig18](results/figures/fig18.png) |
| fig19 | ![fig19](results/figures/fig19.png) |
| fig20 | ![fig20](results/figures/fig20.png) |
| fig21 | ![fig21](results/figures/fig21.png) |
| fig22 | ![fig22](results/figures/fig22.png) |
| fig23 | ![fig23](results/figures/fig23.png) |
| fig25 | ![fig25](results/figures/fig25.png) |
| fig34 | ![fig34](results/figures/fig34.png) |

## Reproducibility

To reproduce results:

```bash
git clone https://github.com/your-username/PDAC-AgenticNet.git
cd PDAC-AgenticNet
pip install -r requirements.txt
python src/train.py
python src/evaluate.py
```

The full experimental workflow is available in:

```bash
jupyter notebook notebooks/experiments.ipynb
```

## Key Contributions

- Developed a PDAC drug-response prediction workflow using machine learning and pharmacogenomic features.
- Achieved high internal model performance with Stacked Ensemble, RandomForest, XGBoost, and MultiTask DNN models.
- Compared multiple model families, including ensemble ML, deep learning, GNN, and Bayesian modeling.
- Added external validation using CCLE/DepMap biomarker data and CRISPR dependency data.
- Provided reviewer-friendly results tables, figures, methodology documentation, and reproducibility commands.

## Documentation

- Methodology: `docs/methodology.md`
- Dataset summary: `results/tables/dataset_summary.csv`
- Performance metrics: `results/tables/performance_metrics.csv`
