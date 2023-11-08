# TP Docker - Price Calculator

The aim of this project is to obtain the all-inclusive price from a price and a tax.

## Prerequisites

- Docker
- Python 3.12

## How to dev

Create a docker image :

    docker build -t {image name} .

Run the command line in terminal :

    docker run -it {image name} python app.py {price} {percent}

Example :

    docker run -it test-calc python app.py 100 20

## How to test


Run the command line in terminal :

    docker run -it {image name} python test/test_calc_methods.py

Example :

    docker run -it test-calc python test/test_calc_methods.py
