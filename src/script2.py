from nltk.tokenize import WordPunctTokenizer
tk = WordPunctTokenizer()
texto = "¿Cuanto tiempo ha pasado desde que iniciamos clase?"
tokenizado = tk.tokenize(texto)
print(tokenizado)