from nltk.tokenize import TreebankWordTokenizer
tk = TreebankWordTokenizer()
texto = "¿Cuanto tiempo ha pasado desde que iniciamos clase?"
tokenizado = tk.tokenize(texto)

print(tokenizado)