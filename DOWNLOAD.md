Dataset **Car License Plate** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/5/R/m5/MzylmEpcZsWy0ijvl2WTbaM9E7gn8D0pVFCG7wcOUeDbmd221xLsRsJPyJAKOPpNE7GSpz3Eb1CkchBaVr7UdFx7PaPp5NQG172yK19VZDlAn2scCmYT1MZuygmI.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Car License Plate', dst_path='~/dtools/datasets/Car License Plate.tar')
```
The data in original format can be 🔗[downloaded here.](https://www.kaggle.com/datasets/andrewmvd/car-plate-detection/download?datasetVersionNumber=1)