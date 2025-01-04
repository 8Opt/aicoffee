"""
For the sake of simplicity, this repo only focus on several dataset.
Most of the dataset is heavily depend on Huggingface's dataset.
"""

from typing import Any
from torch.utils.data import Dataset


class BaseDataset(Dataset):
    def __init__(self, name: str):
        super().__init__()

        # TODO: Add more type checking from base so that the dataset modules can easily choose to install from huggingface or torchvisions

        self.name = name

    def __getitem__(self, idx) -> Any:
        """Get item via object's index"""
        pass

    def __len__(self) -> int:
        """Length of the dataset"""
        pass

    def _setup_dataset(self, name: str) -> Any:
        """Download dataset"""
        pass

    def _get_description(self) -> str:
        """Setup description for the dataset, it must consist:
        1. 1-2 samples of the dataset.
        2. (number of labels)
        3.
        """
        pass
