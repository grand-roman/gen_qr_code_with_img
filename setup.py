import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["path>=16.3.0", "Pillow>=9.0.1", "qrcode>=7.3.1"]

setuptools.setup(
    name="gen-qr-with-img",
    version="1.0.1",
    author="Roman Andreev",
    author_email="grand-roman@yandex.ru",
    description="Generation QR Code with IMG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/grand-roman/gen_qr_code_with_img",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
)