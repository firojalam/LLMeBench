import os

from llmebench.datasets import CheckworthinessDataset
from llmebench.models import BLOOMPetalModel
from llmebench.tasks import CheckworthinessTask


def config():
    return {
        "dataset": CheckworthinessDataset,
        "dataset_args": {},
        "task": CheckworthinessTask,
        "task_args": {},
        "model": BLOOMPetalModel,
        "model_args": {
            "api_url": os.environ["API_URL"],
            "class_labels": ["0", "1"],
            "max_tries": 3,
        },
        "general_args": {
            "data_path": "data/factuality_disinformation_harmful_content/checkworthyness/turkish/CT22_turkish_1A_checkworthy_test_gold.tsv"
        },
    }


def prompt(input_sample):
    return {
        "prompt": "Classify the tweet as checkworthy or not checkworthy. Provide only label.\n\n"
        + "tweet: "
        + input_sample
        + "label: \n"
    }


def post_process(response):
    label = response["outputs"].strip().lower()
    label = label.replace("<s>", "").replace("</s>", "").strip()

    label_fixed = None

    if label == "checkworthy":
        label_fixed = "1"
    elif (
        label == "not_checkworthy."
        or label == "not checkworthy"
        or label == "no checkworthy"
    ):
        label_fixed = "0"

    return label_fixed
