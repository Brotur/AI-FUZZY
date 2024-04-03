import pandas as pd
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Membaca file Excel
df = pd.read_excel('file.xlsx')

# Variabel input
nilai_rata_rata = ctrl.Antecedent(np.arange(0, 101, 1), 'nilai rata-rata')
prestasi = ctrl.Antecedent(np.arange(0, 101, 1), 'prestasi')
penghasilan_orangtua = ctrl.Antecedent(np.arange(500000, 3000001, 1), 'penghasilan orangtua')

# Variabel output
kelayakan = ctrl.Consequent(np.arange(0, 101, 1), 'kelayakan')

# Menentukan fungsi keanggotaan untuk masing-masing variabel
nilai_rata_rata['rendah'] = fuzz.trimf(nilai_rata_rata.universe, [0, 35, 50])
nilai_rata_rata['sedang'] = fuzz.trimf(nilai_rata_rata.universe, [0, 50, 70])
nilai_rata_rata['tinggi'] = fuzz.trimf(nilai_rata_rata.universe, [70, 100, 100])

prestasi['rendah'] = fuzz.trimf(prestasi.universe, [0, 35, 50])
prestasi['sedang'] = fuzz.trimf(prestasi.universe, [0, 50, 70])
prestasi['tinggi'] = fuzz.trimf(prestasi.universe, [70, 100, 100])

penghasilan_orangtua['tinggi'] = fuzz.trimf(penghasilan_orangtua.universe, [500000, 500000, 1750000])
penghasilan_orangtua['sedang'] = fuzz.trimf(penghasilan_orangtua.universe, [500000, 1750000, 3000000])
penghasilan_orangtua['rendah'] = fuzz.trimf(penghasilan_orangtua.universe, [1750000, 3000000, 3000000])

kelayakan['rendah'] = fuzz.trimf(kelayakan.universe, [0, 0, 25])
kelayakan['sedang'] = fuzz.trimf(kelayakan.universe, [0, 25, 75])
kelayakan['tinggi'] = fuzz.trimf(kelayakan.universe, [25, 100, 100])

# Membuat aturan fuzzy
rule1 = ctrl.Rule(nilai_rata_rata['rendah'] | prestasi['rendah'] | penghasilan_orangtua['rendah'], kelayakan['rendah'])
rule2 = ctrl.Rule(nilai_rata_rata['sedang'] | prestasi['sedang'] | penghasilan_orangtua['sedang'], kelayakan['sedang'])
rule3 = ctrl.Rule(nilai_rata_rata['tinggi'] | prestasi['tinggi'] | penghasilan_orangtua['tinggi'], kelayakan['tinggi'])
rule4 = ctrl.Rule(nilai_rata_rata['rendah'] & prestasi['rendah'] & penghasilan_orangtua['rendah'], kelayakan['rendah'])
rule5 = ctrl.Rule(nilai_rata_rata['tinggi'] & prestasi['tinggi'] & penghasilan_orangtua['tinggi'], kelayakan['tinggi'])
rule6 = ctrl.Rule(nilai_rata_rata['rendah'] & prestasi['tinggi'] & penghasilan_orangtua['tinggi'], kelayakan['tinggi'])
rule7 = ctrl.Rule(nilai_rata_rata['tinggi'] & prestasi['rendah'] & penghasilan_orangtua['rendah'], kelayakan['rendah'])

# Membuat kontrol sistem fuzzy
kelayakan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7])
kelayakan_sim = ctrl.ControlSystemSimulation(kelayakan_ctrl)

# Memasukkan input dari dataframe
hasil_kelayakan = []
keterangan_kelayakan = []
for index, row in df.iterrows():
    kelayakan_sim.input['nilai rata-rata'] = row['nilai rata-rata']
    kelayakan_sim.input['prestasi'] = row['prestasi']
    kelayakan_sim.input['penghasilan orangtua'] = row['penghasilan orangtua']

    # Memproses hasil fuzzy
    kelayakan_sim.compute()

    # Menyimpan hasil kelayakan dan keterangan
    kelayakan_level = kelayakan_sim.output['kelayakan']
    hasil_kelayakan.append(kelayakan_level)
    if kelayakan_level <= 35:
        keterangan = 'rendah'
    elif kelayakan_level <= 55:
        keterangan = 'sedang'
    else:
        keterangan = 'tinggi'
    keterangan_kelayakan.append(keterangan)

# Menambahkan kolom hasil kelayakan dan keterangan ke dalam dataframe
df['kelayakan'] = hasil_kelayakan
df['keterangan'] = keterangan_kelayakan

# Menyimpan dataframe ke file Excel
df.to_excel('hasil_kelayakan.xlsx', index=False)
