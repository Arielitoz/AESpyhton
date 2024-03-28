# Links de refs. - https://codeigo.com/python/aes-criptografarion-and-decriptografarion-in-python-64-128-256/ , https://onboardbase.com/blog/aes-criptografarion-decriptografarion/, https://stackoverflow.com/questions/20852664/python-pycrypto-criptografar-decriptografar-text-files-with-aes, https://www.delftstack.com/howto/python/python-aes-criptografarion/ , https://femionewin.medium.com/aes-criptografarion-with-python-step-by-step-3e3ab0b0fd6c, https://medium.com/wearesinch/building-aes-128-from-the-ground-up-with-python-8122af44ebf9, https://medium.com/quick-code/aes-implementation-in-python-a82f582f51c2, https://onboardbase.com/blog/aes-encryption-decryption/
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
 
def criptografar(msg, chave):
    # Gera um vetor de inicialização aleatório (IV)
    iv = get_random_bytes(AES.block_size)
    # Cria uma cifra AES com a chave e o AES.MODE_CBC (Modo CBC)
    cifra = AES.new(chave, AES.MODE_CBC, iv)
    # Adiciona o Padding no bloco e criptografa
    textocifrado = cifra.encrypt(pad(msg, AES.block_size))
    # Concatena o IV ao texto cifrado
    dados_criptografados = iv + textocifrado
    # retorna os dados criptografados
    return dados_criptografados
 
def decriptografar(textocifrado, chave):
    # Extrai o IV do texto cifrado
    iv = textocifrado[: AES.block_size]
    # Cria uma cifra AES com a chave, o (modo cbc) AES.MODE_CBC e a chave extraida
    cifra = AES.new(chave, AES.MODE_CBC, iv)
    # Decriptografa o texto cifrado e remove o IV
    dados_originais = unpad(cifra.decrypt(textocifrado[AES.block_size :]), AES.block_size)
    return dados_originais
 
# Exemplo de uso -  prefixo b-seq. de bytes
msg = b"oi prfeosser"
# Gera uma chave aleatória de 256-bit (32-byte)
# Tamanho de chave suportado: 16, 24, and 32 bytes.
# 128-bit (16 bytes), 192-bit (24 bytes). 256-bit (32 bytes)

chave = get_random_bytes(32)
print("chave:", chave.hex())
# criptografarion
dados_criptografados = criptografar(msg, chave)
print("Dados criptografados:", dados_criptografados)
# decriptografarion
dados_originais = decriptografar(dados_criptografados, chave)
print("Dados originais:", dados_originais)