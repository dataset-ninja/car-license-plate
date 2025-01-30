Dataset **Car License Plate** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzEwMDVfQ2FyIExpY2Vuc2UgUGxhdGUvY2FyLWxpY2Vuc2UtcGxhdGUtRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAiNDZEVlBiQWR0VUdtTWlTekNzS09zOVU5R0h0RW52OUZIay9nQlZ4Rmtxaz0ifQ==)

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