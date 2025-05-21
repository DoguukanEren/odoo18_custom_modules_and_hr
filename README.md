# Quanimo 
---

## 📁 Modül 1: Quanimo Employers

**Konum:** `deneme_addons/quanimo_employers`

### İçerik:
- Yeni bir model: `employers.employer`
- Alanlar:
  - `name`: İsim
  - `employer_id`: Çalışan ID
  - `image`: Fotoğraf
  - `birthday`: Doğum Günü
  - `gender`: Cinsiyet (Seçilebilir: Kadın/Erkek)
  - `email`, `phone`, `address`: İletişim bilgileri
- Görünümler:
  - Liste (Tree) görünümü
  - Form görünümü sekmeli yapı ile

### Menü:
- "Çalışan Yönetimi" başlığı altında `"Çalışanlar"` menüsü

---

## 📁 Geliştirme: HR Modülü Üzerinde

**Konum:** `odoo\addons\hr\views\hr_employee_category_views.xml  ,odoo\addons\hr\models\hr_employee.py` Alanlarında değişiklik yapıldı.

### Yapılan Geliştirmeler:
- `hr.employee` modeline 3 sekme (tab) eklendi:
  1. **Ek Bilgiler**:
     - `extra_note`: Açıklama
     - `employment_start`: İşe Başlama Tarihi
     - `experience_years`: Yıl olarak deneyim
     - `is_certified`: Sertifika var mı?
  2. **Kişisel Hobi Bilgileri**:
     - `hobby`: Seçilebilir hobiler
     - `hobby_level`: 1–10 arası seviye
     - `hobby_cost`: Ortalama harcama
  3. **Kişisel Fobi Bilgileri**:
     - `fobby`: Serbest metin girişi

### Yetki Kısıtı:
- `manager_note` alanı sadece `hr.group_hr_manager` grubundaki yöneticiler tarafından görüntülenebilir.

---

## 🧪 Ek Bilgiler:
- Geliştirme ortamı: PyCharm
- Version Control: Git & GitHub kullanıldı.
- Alan türleri: `Char`, `Integer`, `Float`, `Selection`, `Date`, `Boolean`, `Binary`, `Text`
- XML sayfasında `group`, `field`, `page`, `notebook`, `widget` gibi Odoo bileşenleri aktif olarak kullanıldı.

---

## 🧠 Geliştirici Notu
Bu modül, Odoo geliştiriciliğine başlangıç yapan biri tarafından geliştirilmiştir.
