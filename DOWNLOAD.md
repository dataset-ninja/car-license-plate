Dataset **Car License Plate** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMTAwNV9DYXIgTGljZW5zZSBQbGF0ZS9jYXItbGljZW5zZS1wbGF0ZS1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJ3RFRJN0J1T0VNNzdNc0NMbTJGZ3dKWTc5L200VXF2WEtBTUloYjM0dEJ3PSJ9?response-content-disposition=attachment%3B%20filename%3D%22car-license-plate-DatasetNinja.tar%22)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Car License Plate', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/andrewmvd/car-plate-detection/download?datasetVersionNumber=1).