from torchvision.transforms import v2

from datasets import load_dataset, Dataset

from aicoffee.modules.dataset.base import BaseDataset

# from aicoffee.common.helpers import unique_labels
from aicoffee.core.supported import DATASET


class CatDogDataset(BaseDataset):
    "Using Microsoft's CatDog dataset from Huggingface"

    def __init__(
        self,
        name: str = DATASET.get("vision").get("ms_cats_dogs"),
        test_size: float = 0.1,
    ):
        super().__init__(name=name)
        self.dataset = self._setup_dataset(name)

    def _setup_dataset(self, name: str) -> Dataset:
        dataset = load_dataset(name)  # DatasetDict -> keys = "train"
        dataset = dataset.get("train")
        return dataset

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        return super().__getitem__(idx)

    def _get_description(self):
        labels = ...
        rst = f"""Using {self.name}"""
        return rst

    def transform(self):
        "A suite of augment data methods"
        ...
