### Wallet Python BSC

Este script en python es para poder crear una wallet en la BlockChain de BSC por medio de WEB3.

Aqui se va a ir desarrollando lo basico para poder crear y controlar la Wallet.

**Como usar el scrypt**
- Descargar python [Aqui](https://www.python.org/ "Aqui")
- Descargar y modificar el Archivo crear_wallet.py, el archivo lo puedes modificar con sublime text, el cual puedes descargar [Aqui](https://www.sublimetext.com/ "Aqui")
- Comentar la linea 4 y descomentar la linea 2 para usar la MainNet, ya que la linea 4 es la TestNet
```python
# MainNet
# bsc = "https://bsc-dataseed.binance.org"
# testnet
bsc = "https://data-seed-prebsc-1-s1.binance.org:8545"
```
- Una vez guardado el archivo debes ejecutarlo desde una terminal de windows o de tu sistema operativo que uses con el siguiente comando.
`python crear_wallet.py`
- Cuando termine de ejecutar el script veras que se crea un archivo wallet.txt, guarda bien ese archivo, ahi se encuentra tu wallet y el privateKey para poder acceder a ella.
