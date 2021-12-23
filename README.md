# Tester zadania F

Skrypt odpala dwa programy ( twój i taki co przechodzi na 100% ) i porównuje wyjścia ich obu.

## Użycie:
* Clonujemy repozytorium z githuba:
```
git clone https://github.com/wmii-cs-2017/f-sprawdzarka.git
```
lub za pomocą ssh:
```
git clone git@github.com:wmii-cs-2017/f-sprawdzarka.git
```

* Przenosimy nasz skompilowany program w c++, do sklonowanego folderu `f-sprawdzarka`
* Odpalamy skrypt `check.py` z nazwą naszego programu jako argument wraz z ewentualnym rozszerzeniem. Wpisując w terminal:
```
python3 check.py [nazwa programu]
```
lub python zamiast python3, jeśli coś nie działa.


## Częste problemy:
* sprawdzcie czy macie zainstalowanego pythona
* sprawdzcie czy na pewno odpalacie pythonem3 a nie pythonem2
* podajemy skompilowany program jako argument a nie .cpp
* może wystąpic problem z uprawnieniami wykonywania dla binarek z prawidłowym wynikiem, musimy nadać im uprawnienie
na linuxie możemy nadać uprawnienie używając chmod:
```
chmod +x good
```
* na macu dodajemy uprawnienie wykonywania do `goodmac`, na windowsie do `good`

## Wymagania:
* python 3.6
