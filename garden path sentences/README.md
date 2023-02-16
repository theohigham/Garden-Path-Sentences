# Garden Path Sentences

This is a Python project that uses the spaCy library to tokenize and perform entity recognition on a list of garden path sentences.

## Requirements

- Python 3.6 or higher
- pip3
- Docker (optional)

## Installation

Before you can run `garden.py`, you need to install the required packages. You can do this by running the following command:

pip3 install -r requirements.txt


This will install the `spacy` package and its dependencies.

## Usage

### Running garden.py locally

To run `garden.py` locally, follow these steps:

1. Clone this repository:

git clone https://github.com/theohigham/Garden-Path-Sentences.git


2. Navigate to the project directory:

cd garden-path-sentences

3. Run the script:

python3 garden.py


This will run the `garden.py` script and output the entities found in the garden path sentences.

Note: If you want to modify the garden path sentences, you can edit the `garden.py` file before running the script.

### Running garden.py in a Docker container

If you prefer to run `garden.py` in a Docker container, follow these steps:

1. Clone this repository:

git clone https://github.com/theohigham/Garden-Path-Sentences.git

2. Navigate to the project directory:

cd garden-path-sentences

3. Build the Docker image:

docker build -t garden-path-sentences

4. Run the Docker container:

docker run garden-path-sentences

This will run the `garden.py` script in a Docker container and output the entities found in the garden path sentences.

Note: If you want to modify the garden path sentences, you can edit the `garden.py` file before building the Docker image.

## Garden Path Sentences

A garden path sentence is a grammatically correct sentence that is difficult to parse because it contains a structural ambiguity or unusual syntax. The term comes from the idea that the sentence leads the reader down a "garden path" that ends in a syntactic dead end.

Here are some examples of garden path sentences:

1. The horse raced past the barn fell.
2. The old man the boat.
3. The chicken is ready to eat.

In `garden.py`, we define a list of garden path sentences and use spaCy to tokenize and perform entity recognition on them. We print out the entities found in each sentence, along with their labels.

## Credits

This project was inspired by the following resources:

- [Wikipedia: Garden path sentence](https://en.wikipedia.org/wiki/Garden_path_sentence)
- [spaCy documentation](https://spacy.io/docs)

The garden path sentences used in this project were adapted from the following sources:

- [The University of Arizona Cognitive Science Program: Garden Path Sentences](http://cogsci.arizona.edu/~harnad/BAARS-HARNAD/bbs.squib.html)
- [The Atlantic: A Linguist Explains How We Write Sarcasm on the Internet](https://www.theatlantic.com/technology/archive/2014/09/how-to-write-sarcasm-on-the-internet/379866/)

