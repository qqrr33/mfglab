# dev-env
- win 10, 11 / ubuntu 22.04
- cuda 11.8
- python 3.10
- C# 4.8.1

</br>

# introduce
- research and development library useful in manufacturing.
- numpy, pandas, csv
- txt, bmp, png, jpg, jpeg, onnx
- object detection : yolo style

</br>

# requirements
``` txt
- numpy==1.26.4
- pandas==2.2.2
- opencv-python==4.10.0.82
- torch==2.2.2
  - pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu118
```

</br>

# set-up
- pip mode
``` shell
pip install mfglab
```

</br>

- edit mode
``` shell
git clone https://github.com/qqrr33/mfglab.git

cd mfglab

python -m venv _venv_mfglab

# windows
.\_venv_mfglab\Scripts\activate

# linux

python -m pip install --upgrade pip

pip install -e .
```

</br>

- raw mode : 삭제 예정
``` shell
git clone https://github.com/qqrr33/mfglab.git

cd mfglab

python -m venv _venv_mfglab

# windows
.\_venv_mfglab\Scripts\activate

# linux

python -m pip install --upgrade pip

pip install -r requirement.txt
```


