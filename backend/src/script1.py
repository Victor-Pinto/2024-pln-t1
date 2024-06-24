from nltk.tokenize import WhitespaceTokenizer
tk = WhitespaceTokenizer()
texto = "¿Cuanto tiempo ha pasado desde que iniciamos clase?"
tokenizado = tk.tokenize(texto)
print(tokenizado)