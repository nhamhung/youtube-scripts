# Install Anaconda

## Install Homebrew

- `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

## Install anaconda using Homebrew

- `brew install --cask anaconda`
- `echo 'export PATH=/usr/local/anaconda3/bin:$PATH' >> ~/.zshrc`
- `echo 'export PATH=/opt/homebrew/anaconda3/bin:$PATH' >> ~/.zshrc`
- `source ~/.zshrc`
- `conda` to verify
- `conda init zsh`

## Create virtual environment

- `conda create --name spark_env`
- `conda activate spark_env`
- `conda install -c conda-forge pyspark`
