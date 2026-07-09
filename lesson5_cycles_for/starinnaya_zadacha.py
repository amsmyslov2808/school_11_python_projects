for bik in range(1, 10 + 1):
    for korova in range(1, 20 + 1):
        for telenok in range(1, 100 + 1):
            if (
                bik * 10 + korova * 5 + telenok * 0.5 == 100
                and bik + korova + telenok == 100
            ):
                print(f"bik = {bik} korova = {korova} telenok = {telenok}")
