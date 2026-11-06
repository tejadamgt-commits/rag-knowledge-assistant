import torch
from torch import nn


class TextClassifier(nn.Module):
    """Simple neural network for numerical feature classification."""

    def __init__(
        self,
        input_size: int,
        hidden_size: int,
        num_classes: int,
    ) -> None:
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)
