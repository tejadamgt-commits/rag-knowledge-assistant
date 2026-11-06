import torch
from torch import nn
from torch.optim import Adam


def train_model(
    model: nn.Module,
    features: torch.Tensor,
    labels: torch.Tensor,
    epochs: int = 100,
    learning_rate: float = 0.001,
) -> list[float]:
    """Train a classification model on a feature tensor."""

    criterion = nn.CrossEntropyLoss()
    optimizer = Adam(
        model.parameters(),
        lr=learning_rate,
    )

    model.train()
    history = []

    for epoch in range(epochs):
        optimizer.zero_grad()

        logits = model(features)
        loss = criterion(logits, labels)

        loss.backward()
        optimizer.step()

        history.append(loss.item())

        if (epoch + 1) % 10 == 0:
            print(f"Epoch {epoch + 1}/{epochs} Loss: {loss.item():.4f}")

    return history
