import numpy as np
from model import build_model

X = np.random.rand(1000, 1) * 5000
y = (X > 3000).astype(int)

model = build_model()
model.fit(X, y, epochs=5, batch_size=32)

model.save("fraud_model")
