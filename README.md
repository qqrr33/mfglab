# introduce
- shared_memory, deep_learning, machine_learning for manufacturing
- Research and development library useful in manufacturing
- 0.01 is better than 0 : This library is more useful than performance
- numpy, pandas, csv
- txt, bmp, png, jpg, jpeg, onnx
- object detection : yolo style

</br>

# dev-env
- win 10, 11 / ubuntu 22.04
- cuda 11.8
- python 3.10
- C# 4.8.1

</br>

# set-up
- pip mode
``` shell
pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu118

pip install mfglab
```

</br>

- git
``` shell
git clone https://github.com/qqrr33/mfglab.git

cd mfglab

python -m venv _venv_mfglab

# windows
.\_venv_mfglab\Scripts\activate

python -m pip install --upgrade pip

pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu118

#setup mode
pip install .

or

# edit mode
pip install -e .
```


