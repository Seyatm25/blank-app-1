import streamlit as st

st.title("🎈 LIT VALO")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import streamlit as st

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        raise ValueError("Pembagian dengan nol tidak diperbolehkan.")
    return a / b

def modulus(a, b):
    if b == 0:
        raise ValueError("Modulus dengan nol tidak diperbolehkan.")
    return a % b

def main():
    print("=== Kalkulator Sederhana ===")
    print("1. Penambahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Modulus (%)")

    try:
        pilihan = int(input("Pilih operasi (1-5): "))
        if pilihan not in range(1, 6):
            print("Pilihan tidak valid.")
            return

        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))

        if pilihan == 1:
            hasil = tambah(a, b)
        elif pilihan == 2:
            hasil = kurang(a, b)
        elif pilihan == 3:
            hasil = kali(a, b)
        elif pilihan == 4:
            hasil = bagi(a, b)
        elif pilihan == 5:
            hasil = modulus(a, b)

        print(f"Hasil: {hasil}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()   
