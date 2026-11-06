import torch
from torch import nn


def evaluate_model(
    model: nn.Module,
    features: torch.Tensor,
    labels: torch.Tensor,
) -> dict[str, float]:
    """Evaluate classification accuracy and loss."""

    model.eval()

    with torch.no_grad():
        logits = model(features)
        loss = nn.CrossEntropyLoss()(logits, labels)

        predictions = logits.argmax(dim=1)
        accuracy = (predictions == labels).float().mean()

    return {
        "loss": loss.item(),
        "accuracy": accuracy.item(),
    }
