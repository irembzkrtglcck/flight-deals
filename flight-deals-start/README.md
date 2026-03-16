# Flight Deals Finder / Ucuz Uçuş Bulucu

## 🇹🇷 Türkçe

Google Sheets'teki şehirlere en ucuz uçuşları bulan ve bütçenizin altında fiyat bulunduğunda email ile bildirim gönderen bir Python uygulaması.

### Nasıl Çalışır?

1. **Google Sheets'ten veri çekme** — Sheety API ile hedef şehirler ve bütçe bilgilerini alır
2. **IATA kodlarını bulma** — Amadeus API ile şehir adlarından havalimanı kodlarını otomatik bulur
3. **Uçuş arama** — Amadeus Flight Offers API ile her şehre en ucuz uçuşları arar
4. **Fiyat karşılaştırma** — Bulunan en ucuz fiyatı Google Sheets'teki bütçeyle karşılaştırır
5. **Email bildirimi** — Bütçenin altında uçuş bulunursa tüm fırsatları tek bir email ile gönderir

### Proje Yapısı

| Dosya | Açıklama |
|-------|----------|
| `main.py` | Ana program — tüm sınıfları birleştirir ve akışı yönetir |
| `data_manager.py` | Google Sheets ile iletişim (Sheety API) |
| `flight_search.py` | Amadeus API ile uçuş arama ve IATA kodu bulma |
| `flight_data.py` | Uçuş verilerini işleme ve en ucuz uçuşu bulma |
| `notification_manager.py` | Email ile bildirim gönderme (Gmail SMTP) |

### Kullanılan Teknolojiler

- Python
- Amadeus Travel API (uçuş arama)
- Sheety API (Google Sheets entegrasyonu)
- smtplib (email gönderimi)
- dotenv (ortam değişkenleri yönetimi)

---

## 🇬🇧 English

A Python application that finds the cheapest flights to cities listed in Google Sheets and sends email notifications when prices drop below your budget.

### How It Works

1. **Fetch data from Google Sheets** — Retrieves destination cities and budget via Sheety API
2. **Find IATA codes** — Automatically finds airport codes from city names using Amadeus API
3. **Search flights** — Searches cheapest flights to each city via Amadeus Flight Offers API
4. **Compare prices** — Compares the cheapest price found with the budget in Google Sheets
5. **Email notification** — Sends a single email with all deals found below budget

### Project Structure

| File | Description |
|------|-------------|
| `main.py` | Main program — orchestrates all classes and manages the flow |
| `data_manager.py` | Google Sheets communication (Sheety API) |
| `flight_search.py` | Flight search and IATA code lookup (Amadeus API) |
| `flight_data.py` | Flight data processing and cheapest flight finder |
| `notification_manager.py` | Email notifications (Gmail SMTP) |

### Technologies Used

- Python
- Amadeus Travel API (flight search)
- Sheety API (Google Sheets integration)
- smtplib (email sending)
- dotenv (environment variable management)

---

### Setup

1. Clone the repository
2. Create a `.env` file with the following variables:
```
SHEETY_ENDPOINT=your_sheety_endpoint
SHEETY_TOKEN=your_sheety_token
AMADEUS_API_KEY=your_amadeus_key
AMADEUS_API_SECRET=your_amadeus_secret
AMADEUS_ENDPOINT=https://test.api.amadeus.com/v1/security/oauth2/token
MY_EMAIL=your_email@gmail.com
MY_EMAIL_PASSWORD=your_app_password
```
3. Install dependencies: `pip install requests python-dotenv`
4. Run: `python main.py`
