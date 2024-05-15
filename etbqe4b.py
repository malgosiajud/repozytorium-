lancuch = "Kognitywistyka - dziedzina nauki zajmująca się obserwacją i analizą działania zmysłów, mózgu i umysłu, w szczególności ich modelowaniem. Na jej określenie używane są też pojęcia: nauki kognitywne (ang. Cognitive Sciences)[1] bądź nauki o poznaniu. Kognitywistyka jest nauką interdyscyplinarną, znajduje się na pograniczu wielu dziedzin: psychologii poznawczej, neurobiologii, filozofii umysłu, sztucznej inteligencji, lingwistyki oraz logiki i fizyki. Główne obszary badawcze w obrębie tej dziedziny to reprezentacja wiedzy, język, uczenie się, myślenie, percepcja, świadomość, podejmowanie decyzji oraz inteligencja (tzw. inteligencja kognitywna). Konferencja MIT - 11 września 1956 roku (m.in. Claude E. Shannon, Allen Newell, Herbert A. Simon, Noam Chomsky, George Miller): \"dzień, w którym kognitywistyka wyskoczyła z łona cybernetyki i stała się szanowanym, interdyscyplinarnym przedsięwzięciem realizowanym na swój własny rachunek\" (George Miller, 1979). Kognitywistyka jako samodzielna dziedzina nauki wyodrębniła się w 1975 roku w Stanach Zjednoczonych. W 1976 roku zaczęto wydawać kwartalnik \"Cognitive Science\". Program badaczy kognitywistyki został przedstawiony w tym samym roku przez Allena Newella oraz Herberta Simona w artykule Informatyka jako badania empiryczne[2]. Kognitywistyka symboliczna nie jest dobrze zdefiniowana w naukowej literaturze światowej i koncentruje się na symbolicznym modelowaniu uświadamianych abstrakcyjnych funkcji myślowych uznawanych za takie same u wszystkich ludzi i dotyczy: samoświadomości (metakognitywistyka, ang. metacognition), kognitywnego podejmowania decyzji (cognitive decision-making) i inteligencji socjo-kognitywistycznej/kognitywnej jako uniwersalnych własności jednostki, grupy, organizacji ludzkich i robotów. Tego typu działalność naukowa prowadzi do rozwoju nowego podejścia integrującego paradygmaty teorii systemów, inżynierii, nauk społecznych i kognitywistyki, tzw. inżynierii socjokognitywistycznej (lub socio-kognitywistycznej) rozwijanej przez Adama Marię Gadomskiego w ramach meta-teorii TOGA[3]. Od strony zastosowanych technologii kognitywistyka symboliczna koncentruje się na rozbudowie tzw. baz wiedzy (KB - knowledge base) i budowie skomplikowanych Systemów Bazujących na Wiedzy (Knowledge Base System), które to realizują różne funkcje uważane za charakterystyczne dla systemów inteligentnych. Jednym z ważnych, a nierozwiązanych jeszcze wystarczająco problemów kognitywistyki jest definicja świadomości, czyli zdolności syntezy i myślenia o własnym myśleniu. Kognitywistyka subsymboliczna bazuje głównie na wyjaśnianiu procesów myślowych w mózgu ludzkim opartych na własnościach sieci neuronowych. Coraz popularniejszym paradygmatem kognitywistyki subsymbolicznej staje się nauka, w której łączy się wzorce i modele pochodzące z tradycyjnych nauk o poznawaniu, psychologii, neurobiologii i wielu innych subdyscyplin nauk przyrodniczych. Jednym z najbardziej znanych specjalistów w tej dziedzinie w Polsce jest Włodzisław Duch."

lancuch = lancuch.lower()
print(lancuch)

lancuch = list(lancuch)
print(lancuch)

for i in lancuch[:]:
    if i == ".":
        lancuch.remove(i)
    if i == ",":
        lancuch.remove(i)
    if i == " ":
        lancuch.remove(i)
    if i == "(":
        lancuch.remove(i)
    if i == ")":
        lancuch.remove(i)
    if i == "[":
        lancuch.remove(i)
    if i == "]":
        lancuch.remove(i)
    if i == "1":
        lancuch.remove(i)
    if i == "2":
        lancuch.remove(i)
    if i == ":":
        lancuch.remove(i)


# i = 1
# for i in lancuch:
#     if i-1 == " " and i+1 == " ":
#         lancuch.remove(i)

jest = 0

# print(lancuch)
# szukane = input()
# for element in lancuch:
#     if szukane == element:
#         jest = 1
# if jest == 1:
#     print("jest")
# else:
#     print("nie ma")

ilość_wystąpień = 0

for litera in lancuch:
    if "w" == litera:
        ilość_wystąpień += 1

print(ilość_wystąpień)

#śmieszna zmiana nananana na na







