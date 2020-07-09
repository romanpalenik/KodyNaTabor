#zoznam musí byť tvare Meno	Priezvisko	Dátum narodenia	Ulica


def creatingCode(arr, criteria): #sortne to podla mena cez bubble sort
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j][criteria] > arr[j + 1][criteria]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def creatingCodeThirdLetter(arr, criteria): #sortne to podla mena cez bubble sort
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j][criteria][2] > arr[j + 1][criteria][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


with open('zoznam.txt', 'r', encoding='utf8') as file:
    arrayWithInfo = []
    for line in file:
        arrayWithInfo.append(line.split())

    #sortovanie podľa mena
    creatingCode(arrayWithInfo, 0)

    with open("podlaMena.txt", "a", encoding='utf8') as file2:
        for info in arrayWithInfo:
            file2.write(info[0] + " ")
            file2.write(info[1] + "\n")

    #sortovanie podľa priezviska
    creatingCode(arrayWithInfo, 1)

    with open("podlaPriezviska.txt", "a", encoding='utf8') as file3:
        for info in arrayWithInfo:
            file3.write(info[0] + " ")
            file3.write(info[1] + "\n")


    #sortovanie podľa mena 3-tie písmenko
    creatingCodeThirdLetter(arrayWithInfo, 0)

    with open("podlaMena3pismeno.txt", "a", encoding='utf8') as file4:
        for info in arrayWithInfo:
            file4.write(info[0] + " ")
            file4.write(info[1] + "\n")

    #sortovanie podľa priezvisko 3-tie písmenko
    creatingCodeThirdLetter(arrayWithInfo, 1)

    with open("podlaPriezviska3pismeno.txt", "a", encoding='utf8') as file5:
        for info in arrayWithInfo:
            file5.write(info[0] + " ")
            file5.write(info[1] + "\n")