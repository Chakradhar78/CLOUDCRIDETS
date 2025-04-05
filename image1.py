from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    # Open the image and convert to RGB
    img = Image.open(input_path).convert('RGB')
    # Convert image to numpy array
    img_array = np.array(img, dtype=np.uint8)
    
    # Generate a key array of the same shape as the image
    key_array = np.random.randint(0, 256, size=img_array.shape, dtype=np.uint8) % key
    
    # Perform XOR operation for encryption
    encrypted_array = np.bitwise_xor(img_array, key_array)
    
    # Convert back to image
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)
    print(f"Encrypted image saved as {output_path}")
    return key_array  # Return key for decryption

def decrypt_image(encrypted_path, output_path, key_array):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_path)
    encrypted_array = np.array(encrypted_img, dtype=np.uint8)
    
    # Perform XOR with the same key to decrypt
    decrypted_array = np.bitwise_xor(encrypted_array, key_array)
    
    # Convert back to image
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_path)
    print(f"Decrypted image saved as {output_path}")

# Example usage
if __name__ == "__main__":
    input_image =  "E:\\CLOUDCRIDETS\\ganesh.jpg" # Replace with your image path
    encrypted_image = "encrypted.png"
    decrypted_image = "decrypted.png"
    encryption_key = 42  # Simple key (can be any integer 0-255)

    # Encrypt the image
    key_used = encrypt_image(input_image, encrypted_image, encryption_key)
    
    # Decrypt the image
    decrypt_image(encrypted_image, decrypted_image, key_used)