from packages import yakit
from packages import doviz
if __name__ == "__main__":
    print("\n")
    try:
        doviz.fiyatOgren()
    except:
        print("Döviz verileri çekilemedi. yanlış bir şeyler var. Lütfen doğru girildiğinden emin olun.")
    print("\n")
    yakit.fiyatlar()