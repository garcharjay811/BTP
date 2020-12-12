import sys
import tensorflow as tf
import numpy as np

def main():
    n_samples = 20
    new_generator_model = tf.keras.models.load_model(sys.argv[1])
    x = np.random.randn(6 * 3 * n_samples)

    X = np.reshape(x, (n_samples, 6, 3))

    generated_sample = new_generator_model.predict(X)

    print(generated_sample)

if __name__ == '__main__':
    main()

