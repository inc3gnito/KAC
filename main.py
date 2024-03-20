from pyscript import Element

def noveld():
    output = Element('output').element
    ertek = output.innerHTML
    szam = int(ertek) +1
    output.innerHTML =szam
    print(szam)
    
