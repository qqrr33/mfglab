# dev-env
- win 11 / ubuntu 22.04
- cuda 11.8
- python 3.10

</br>

# introduce
- research and development library useful in manufacturing.
- numpy, pandas, csv
- txt, bmp, png, jpg, jpeg, onnx

</br>

# requirements
- numpy==1.26.4
- pandas==2.2.2
- opencv-python==4.10.0.82
- torch==2.2.1

</br>

# set-up
- pip mode
``` shell
pip install mfglab
```

</br>

- edit mode
``` shell
pip install -e .
```

</br>

- raw mode
``` shell
python -m venv _venv_mfglab

.\_venv_mfglab\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirement.txt
```

