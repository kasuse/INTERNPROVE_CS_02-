from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    # Load the image
    image = Image.open(image_path)
    image_data = np.array(image)

    # Perform encryption by adding a key to each pixel value
    encrypted_data = (image_data + key) % 256  # Keeping pixel values in valid range (0-255)

    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_data.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    # Load the encrypted image
    image = Image.open(image_path)
    image_data = np.array(image)

    # Perform decryption by subtracting the key
    decrypted_data = (image_data - key) % 256  # Reverting the encryption

    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_data.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

# Example usage:
image_path = "input_image.png"  # Path to the original image
encrypted_path = "encrypted_image.png"  # Path to save encrypted image
decrypted_path = "decrypted_image.png"  # Path to save decrypted image
key = 50  # Simple key for encryption/decryption

# Encrypt the image
encrypt_image(image_path, encrypted_path, key)

# Decrypt the image
decrypt_image(encrypted_path, decrypted_path, key)
