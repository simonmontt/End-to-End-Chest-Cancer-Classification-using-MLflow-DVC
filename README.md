# End-to-End-Chest-Cancer-Classification-using-MLflow-DVC


## Workflow

1. Update config.yaml
2. Update secrets.yaml [Optional] # Just if there's a secret credential/file
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtube.com/playlist?list=PLkz_y24mlSJZrqiZ4_cLUiP0CBN5wFmTb&si=zEp_C8zLHt1DzWKK)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/simonmontt/End-to-End-Chest-Cancer-Classification-using-MLflow-DVC.mlflow \
MLFLOW_TRACKING_USERNAME=simonmontt \
MLFLOW_TRACKING_PASSWORD=b6cd9be87f377a371f06a721028cc2bf17be5e4c \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/simonmontt/End-to-End-Chest-Cancer-Classification-using-MLflow-DVC.mlflow

export MLFLOW_TRACKING_USERNAME=simonmontt 

export MLFLOW_TRACKING_PASSWORD=b6cd9be87f377a371f06a721028cc2bf17be5e4c
                                
```