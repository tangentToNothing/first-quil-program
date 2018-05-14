# First Quil Program

* Rigetti's Forest API: [http://pyquil.readthedocs.io/en/latest/index.html](forest)
* Rigetti's Grove Library: [http://grove-docs.readthedocs.io/en/latest/index.html](grove)

## Goals

* Implement simple rsa which supports weak cryptographic strength for the purposes of testing classical vs quantum prime facrotization methods
* Implement an efficient classical cracking process
* Implement a quantum or hybrid cracking process

## Usage

Use [https://anaconda.org/](conda) to create a python 3 virtual environment:
<br>
`conda create -n quil_basic python=3`
<br>
Activate your conda environment
<br>
`source activate quil_basic`
<br>
Install dependencies:
<br>
`pip install -r requirements.txt`
<br>
Run the program with `python main.py`. It will ask you how many bits you want your `p` and `q` variables in the RSA function to use (roughly 2x your input will be the final bit strength of your resulting RSA keypair). Input larger than `32` will not be accepted, because this will probably confuse and/or harm your laptop.

<b>WARNING:</b> Selecting bit strength greater than 30 can result in longer execution times of this program, on the order of minutes, depending on hardware. 