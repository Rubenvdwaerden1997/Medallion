from setuptools import find_packages, setup

setup(
    name="Medallion",
    version="3.0.0",
    description=(
        "Training segmentation models with less labeled data."
    ),
    install_requires=[
        "emmental==0.1.1",
        "torch==1.9.0",
        "torchvision==0.10.0",
        "matplotlib>=3.3.4",
        "scikit-image>=0.17.2",
        "seaborn>=0.11.1",
        "urllib3==1.26.12",
        "pyyaml==5.3.1",
        "setuptools==59.5.0"
    ],
    python_requires=">=3.8",
    scripts=["bin/image_segmentation"],
    packages=find_packages(),
)