from llmebench.datasets import ARCDDataset
from llmebench.models import LegacyOpenAIModel
from llmebench.tasks import QATask


def metadata():
    return {
        "author": "Arabic Language Technologies, QCRI, HBKU",
        "model": "gpt-35-turbo (version 0301)",
        "description": "GPT35 model hosted on Azure, using the Completion API. API version '2023-03-15-preview'.",
        "scores": {"F1": "0.502"},
    }


def config():
    return {
        "dataset": ARCDDataset,
        "dataset_args": {},
        "task": QATask,
        "task_args": {},
        "model": LegacyOpenAIModel,
        "model_args": {
            "max_tries": 3,
        },
    }


def prompt(input_sample):
    return {
        "system_message": "Assistant is a large language model trained by OpenAI.",
        "messages": [
            {
                "sender": "user",
                "text": f"Your task is to answer questions in Arabic based on a given context.\nNote: Your answers should be spans extracted from the given context without any illustrations.\nYou don't need to provide a complete answer\nContext:{input_sample['context']}\nQuestion:{input_sample['question']}\nAnswer:",
            }
        ],
    }


def post_process(response):
    return response["choices"][0]["text"]
