Dataset **Car License Plate** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/6/U/zK/9U0GLkBsxKY8tESvRo5OvCczodsb5RcCQ3ChUxEhyxJfYB3Hzd5sSOvGwemAqWKUXmC22iHMSssQtCT1rVYLvkUY8dDXlapzQRDMjyLEilo42JFoP1hVjJP6qEfX.tar)

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