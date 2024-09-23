def sayi_al(mesaj):
    while True:
        try:
            return float(input(mesaj))  # Sayıyı al ve float'a dönüştür
        except ValueError:
            print("Hatalı giriş! Lütfen bir sayı giriniz.")  # Hata durumunda tekrar sor

def hesap_makinesi():
    print("Hesap Makinesine Hoş Geldiniz")
    print(" 1. Toplama\n 2. Çıkarma\n 3. Çarpma\n 4. Bölme")

    while True:
        islem = input("Yapmak istediğiniz işlemi seçiniz (1-4): ")
        if islem in ['1', '2', '3', '4']:  # İşlem seçiminin doğru olup olmadığını kontrol et
            break
        else:
            print("Hatalı işlem seçimi! Lütfen 1 ile 4 arasında bir işlem seçiniz.")

    sayi1 = sayi_al("İlk sayıyı giriniz: ")
    sayi2 = sayi_al("İkinci sayıyı giriniz: ")

    if islem == '1':
        print(f"{sayi1} + {sayi2} = {sayi1 + sayi2}")
    elif islem == '2':
        print(f"{sayi1} - {sayi2} = {sayi1 - sayi2}")
    elif islem == '3':
        print(f"{sayi1} * {sayi2} = {sayi1 * sayi2}")
    elif islem == '4':
        while sayi2 == 0:  # Bölme işlemi için 0 kontrolü
            print("Bölme işleminde ikinci sayı sıfır olamaz!")
            sayi2 = sayi_al("Lütfen 0'dan farklı bir ikinci sayı giriniz: ")
        print(f"{sayi1} / {sayi2} = {sayi1 / sayi2}")

# Hesap makinesi fonksiyonunu çağır
hesap_makinesi()