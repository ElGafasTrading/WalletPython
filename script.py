from web3 import Web3

# MainNet
# bsc = "https://bsc-dataseed.binance.org"
# testnet
bsc = "https://data-seed-prebsc-1-s1.binance.org:8545"

wallet = '0x8A0A9E678bDb50F9816bD450461AABa5797C7B0d'

web3 = Web3(Web3.HTTPProvider(bsc))
if web3.isConnected():
    print('Conexion exitosa')

    # CREAR WALLET
    print('')
    print('Creando nueva Wallet')
    create_wallet = web3.eth.account.create()

    new_wallet_address = create_wallet.address
    new_wallet_key = create_wallet.key.hex()

    print('Wallet:    ' + new_wallet_address)
    print('WalletKey: ' + new_wallet_key)

    # CONFIRMAR CUENTA CON SECRETKEY
    print('')
    print('Confirmando cuanta con Secret Key')
    cuenta = web3.eth.account.privateKeyToAccount(new_wallet_key)
    if cuenta.address == new_wallet_address:
        print('SecretKey Valida')
        print('Wallet:    ' + str(cuenta.address))

        # GUARDAR EN ARVHICO TXT
        file = open('wallet.txt', 'w')
        file.write('Wallet: ' + new_wallet_address + '\n')
        file.write('Key:    ' + new_wallet_key)
        file.close()

        print('')
        print('Wallet creada con exito')
        print('La wallet y la private key fueron guardadas en wallet.txt')
    else:
        print('La secret Key no es Valida')
else:
    print('No se pudo conectar a la red')
