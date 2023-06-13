# https://www.kaggle.com/datasets/andrewmvd/car-plate-detection

import os
import xml.etree.ElementTree as ET

from tqdm import tqdm

import supervisely as sly
from supervisely.io.fs import get_file_name


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "/Users/almaz/Downloads/CarLicensePlate"
    batch_size = 30
    ds_name = "ds"

    images_path = "images"
    anns_path = "annotations"
    ann_ext = ".xml"

    images_path = os.path.join(dataset_path, images_path)
    anns_path = os.path.join(dataset_path, anns_path)
    images_names = os.listdir(images_path)

    def _create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        file_name = get_file_name(image_path)

        ann_path = os.path.join(anns_path, file_name + ann_ext)

        tree = ET.parse(ann_path)
        root = tree.getroot()

        coords_xml = root.findall(".//bndbox")
        for curr_coord in coords_xml:
            left = int(curr_coord[0].text)
            top = int(curr_coord[1].text)
            right = int(curr_coord[2].text)
            bottom = int(curr_coord[3].text)

            rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
            label = sly.Label(rect, obj_class)
            labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    obj_class = sly.ObjClass("license plate", sly.Rectangle)
    project = api.project.create(workspace_id, project_name)
    meta = sly.ProjectMeta(obj_classes=[obj_class])
    api.project.update_meta(project.id, meta.to_json())
    dataset = api.dataset.create(project.id, ds_name)

    progress = tqdm(total=len(images_names), desc="Create dataset {}".format(ds_name))

    for images_names_batch in sly.batched(images_names, batch_size=batch_size):
        img_pathes_batch = [
            os.path.join(images_path, image_name) for image_name in images_names_batch
        ]

        img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns = [_create_ann(image_path) for image_path in img_pathes_batch]
        api.annotation.upload_anns(img_ids, anns)

        progress.update(len(images_names_batch))

    return project
