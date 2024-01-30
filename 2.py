from lokace import *class Hrad

inventar = {"klic": False}
skore = 0
kroky = 0

hrad = Hrad()
posta = Posta()

def hotovo(level):
    return sum(level.zlato) == 0

for level in [hrad, posta]:
    hrac = 0
    print("Vítej v levelu", level.jmeno)

    while not hotovo(level):
        print("hráč je v místnosti:", level.mistnosti[hrac])
        print("hráč má", skore, "zlata")
        print("zbývá zlata:", sum(level.zlato))

        kam_lze_jit = level.chodby[hrac]
        ok_vstupy = ["cheat"]

        for i, moznost in enumerate(kam_lze_jit):
            print("Moznost", i + 1, ": ", level.mistnosti[moznost])
            ok_vstupy.append(str(i + 1))

        if level.zlato[hrac] > 0:
            print("Moznost X : sebrat", level.zlato[hrac], "zlata")
            ok_vstupy.append("x")

        if hrac == level.klic:
            print("Moznost K : sebrat klíč")
            ok_vstupy.append("k")

        if inventar["klic"] and level.zamcene_chodby[hrac]:
            print("Moznost O : odemknout dveře ->", level.mistnosti[level.zamcene_chodby[hrac][-1]])
            ok_vstupy.append("o")

        vstup = input("> ")
        while not vstup in ok_vstupy:
            print("Špatný vstup.")
            vstup = input("> ")

        if vstup == "x":
            skore += level.zlato[hrac]
            level.zlato[hrac] = 0
        elif vstup == "k":
            inventar["klic"] = True
            level.klic = -1
        elif vstup == "o":
            cilova_mistnost = level.zamcene_chodby[hrac].pop()
            level.chodby[hrac].append(cilova_mistnost)
            print("Slyšíš jak cvaknul zámek a dveře se otevřely.")
            inventar["klic"] = False

        elif vstup == "cheat":
            print("Podvody jsou zakázaný hahaha")
        else:
            index_moznosti = int(vstup) - 1
            hrac = kam_lze_jit[index_moznosti]

        kroky += 1
        #break

    print("Level splněn!")

print("Gratuluju, sebral jsi celkem,", skore, "zlata za", kroky, "kroků")


