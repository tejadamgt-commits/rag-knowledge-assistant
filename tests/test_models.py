import torch

from app.ml.models import TextClassifier


def test_model_output_shape():
    model = TextClassifier(
        input_size=10,
        hidden_size=32,
        num_classes=3,
    )

    inputs = torch.randn(8, 10)
    outputs = model(inputs)

    assert outputs.shape == (8, 3)
