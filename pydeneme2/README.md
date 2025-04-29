# Döviz Kurları İndirme Betiği

Bu proje, Türkiye Cumhuriyet Merkez Bankası’nın (TCMB) **today.xml** kaynağından güncel döviz kurlarını **Selenium** ile çekip `doviz.csv` dosyasına kaydeden bir Python betiği içerir.

## Gereksinimler

- Python 3.7 ve üzeri
- Selenium kütüphanesi
- Chrome tarayıcısı
- Chromedriver (Chrome sürümünüzle uyumlu)

Gerekli Python paketlerini yüklemek için:

```bash
pip install selenium pandas
```

## Kurulum

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/kullanici/your-repo.git
   cd your-repo
   ```

````
2. Chromedriver dosyasını proje köküne kopyalayın veya `path` değişkenini kendi konumunuza göre güncelleyin.

---

## Kullanım

```bash
python fetch_rates.py
````

- Betik, `today.xml` adresine giderek tabloyu çeker.
- `doviz.csv` adlı dosyayı proje köküne kaydeder.

---

## Veri Kaynağı

- **Kaynak:** [TCMB today.xml](https://www.tcmb.gov.tr/kurlar/today.xml)
- Lisans: Kişisel ve akademik kullanım için kaynak gösterilerek paylaşılabilir. Ticari kullanım için TCMB'den yazılı izin alınması gerekir.
