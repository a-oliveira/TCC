### Configuração do Ambiente (Windows/Linux)

1. Instalar o Anaconda

- [Anaconda para Windows 64-bit](https://repo.anaconda.com/archive/Anaconda3-2020.07-Windows-x86_64.exe)
- [Anaconda para Linux](https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh)

2. Após a instalação, execute no Anaconda Prompt:

```
conda create -n tf tensorflow
conda activate tf
```

3. Em seguida, instale a versão 2.0 do tensorflow:

```
pip install tensorflow==2.0
```

4. Para testar, execute o comando:

```
python capsulenet.py -t -w result/trained_model-11-19.h5
```