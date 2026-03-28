import torch
import torchvision

def main():
    print('Neural Vision Core Initialized')
    model = torchvision.models.resnet50(pretrained=True)
    model.eval()
    print('Model loaded successfully')

if __name__ == '__main__':
    main()