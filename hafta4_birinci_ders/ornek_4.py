kullaniciAdi = input("Kullanıcı adı :")
if kullaniciAdi == "Talha":
    sifre = input("Şifre :")
    if not sifre == "1234":print("Giriş engellendi")
    if sifre == "1234":
        print("Giriş başarılı.")
        
if not kullaniciAdi == "Talha":print("Giriş engellendi")
