import numpy as np
import pandas as pd

# transformatörün verilerini tanıtalım
nominal_guc = 25e3 
primer_gerilim = 33000
seconder_gerilim = 400
frekans = 50  
hedef_pf = 0.97  
kondansator_degerleri = np.array([50 , 60 , 70 , 80, 90, 100 , 110, 120, 136 , 145 ]) * 1e-6  # Farad cinsinden

def kompanzasyon(yuk_orani, guc_faktoru):
    gorunur_guc = nominal_guc * yuk_orani
    phi_y = np.arccos(guc_faktoru)  
    reaktif_guc = gorunur_guc * np.sin(phi_y) 

    # Hedef reaktif güç
    phi_hedef = np.arccos(hedef_pf)  
    reaktif_hedef = gorunur_guc * np.sin(phi_hedef)  
    delta_reaktif = reaktif_guc - reaktif_hedef

    # Uygun kondansatörü seçmek
    for i, C in enumerate(kondansator_degerleri):
        reaktif_c = seconder_gerilim**2 * 2 * np.pi * frekans * C  # Kondansatörün sağladığı reaktif güç

        if reaktif_c >= delta_reaktif:  # Eğer yeterli reaktif güç sağlanıyorsa
            yeni_pf = np.cos(np.arctan((reaktif_guc - reaktif_c) / gorunur_guc)) 
            return i + 1, C * 1e6, yeni_pf  # Kondansatör numarası, kapasitans (μF), yeni güç faktörü
   
    return len(kondansator_degerleri), kondansator_degerleri[-1] * 1e6, hedef_pf  # En büyük kondansatör

np.random.seed(2)
yuk_oranlari = np.random.uniform(0.5, 1, 10)  
guc_faktorleri = np.random.uniform(0.6, 0.9, 10) 

# Hesaplamalar ve tablo oluşturma
sonuclar = []
for yo, gf in zip(yuk_oranlari, guc_faktorleri):
    no, C, yeni_pf = kompanzasyon(yo, gf)
    sonuclar.append([yo, gf, no, C, yeni_pf])

tablo = pd.DataFrame(sonuclar, columns=["Yük Orani", "Eski Güç Faktörü", 
                                         "Kondansatör Numarasi", "Kapasitans (μF)", 
                                         "Yeni Güç Faktörü"])

print(tablo)
