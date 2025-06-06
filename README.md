# Unknown Dataset Generator for Image Classification
## Description
This Python script automatically creates a diverse "Unknown" class dataset for machine learning image classification projects. It downloads images from various non-relevant categories that might appear in real-world deployment scenarios, helping models better distinguish between target classes and irrelevant inputs.
The script:
- Downloads images from 25 diverse categories including textures, backgrounds, and non-target objects
- Processes all images to a uniform 224×224 resolution (standard for many CNN architectures)
- Creates a balanced dataset with a configurable maximum number of images
- Cleans up temporary files after processing

## Features
- Uses the Bing Image Downloader for diverse image sourcing
- Supports configurable search terms to customize the "Unknown" class
- Handles errors gracefully when processing problematic images
- Organizes output into a structured directory for easy integration with training pipelines

This tool is perfect for improving model robustness in agricultural/plant disease classification systems by teaching them to reject irrelevant inputs rather than misclassifying them.
