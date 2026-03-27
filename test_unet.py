import torch
from unet import UNet

def test_unet():
    # Parameters
    n_channels = 3
    n_classes = 1
    batch_size = 2
    height, width = 256, 256

    # Instantiate model
    model = UNet(n_channels=n_channels, n_classes=n_classes)
    
    # Create a dummy input tensor
    x = torch.randn(batch_size, n_channels, height, width)
    
    # Forward pass
    output = model(x)
    
    # Print results
    print(f"Input shape: {x.shape}")
    print(f"Output shape: {output.shape}")
    
    # Assert output shape
    assert output.shape == (batch_size, n_classes, height, width), "Output shape mismatch!"
    print("Test passed! U-Net architecture is correctly implemented.")

if __name__ == "__main__":
    try:
        test_unet()
    except Exception as e:
        print(f"Test failed with error: {e}")
