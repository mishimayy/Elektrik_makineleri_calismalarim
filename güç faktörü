import numpy as np
import pandas as pd

# transformatörün verilerini tanıtalım
nominal_guc = 25e3
primer_gerilim = 33000
seconder_gerilim = 400
R_eqs = 0.037
X_eqs = 0.024

#Akımı hesaplayalımı
I_nominal = nominal_guc/seconder_gerilim

def hesaplama(yük_orani,güç_faktorü):
    I_yuk = I_nominal*yük_orani
    phi = np.arccos(güç_faktorü) #faz açısı
    I_yuk_kompleks = I_yuk * (np.cos(phi) + 1j*np.sin(phi))

    V_giris_gerilimi = seconder_gerilim + (R_eqs + 1j*X_eqs)*I_yuk_kompleks
    # gerilim ayarlamasında açıyla işimiz yok o yüzden mutlak değer ifadesi yeterli olacaktır pythonda abs kullanabiliriz
    gerilim_ayarlamasi = (np.abs(V_giris_gerilimi) - seconder_gerilim) / seconder_gerilim*100

    #verim için çıkış gücüne ve kayıp güçlere ihtiyacımız var
    P_out = seconder_gerilim*I_yuk*güç_faktorü
    P_cu = I_yuk**2 * R_eqs
    P_cekirdek = (np.abs(V_giris_gerilimi)**2 ) / 266.52 # eş değer devreden geliyor

    #verimi hesaplayalım
    verim = P_out / (P_out + P_cu + P_cekirdek) * 100

    return np.abs(V_giris_gerilimi), gerilim_ayarlamasi , verim

np.random.seed(2)
yük_oranlari = np.random.uniform(0.5, 1, 10)  # Yük oranları (tam yük yüzdesi)
güç_faktörleri = np.random.choice([0.8, -0.8, 0.9, -0.9], 10)  # Rastgele güç faktörleri

# Hesaplamaları yapmak ve tablo oluşturmak
sonuclar = []
for yo, gf in zip(yük_oranlari, güç_faktörleri):
    V_g, VR, verim = hesaplama(yo, gf)
    sonuclar.append([yo, gf, V_g, VR, verim])

tablo = pd.DataFrame(sonuclar, columns=["Yük Orani", "Güç Faktörü", "Giriş Gerilimi (V)", 
                                     "Gerilim Ayarlamasi (%)", "Verim (%)"])
print(tablo)


