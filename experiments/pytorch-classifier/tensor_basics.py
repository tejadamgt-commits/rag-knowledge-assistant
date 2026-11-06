import torch

# Create tensors
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])

# Element-wise operations
print("Addition:", a + b)
print("Multiplication:", a * b)

# Dot product
print("Dot product:", torch.dot(a, b))

# Matrix multiplication
matrix_a = torch.randn(3, 4)
matrix_b = torch.randn(4, 2)

result = matrix_a @ matrix_b

print("Result shape", result.shape)
