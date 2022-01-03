print(
    len(
        set(
            ' '.join(
                open(
                    'input.txt',
                    'r',
                    encoding='utf8'
                ).readlines()
            ).split()
        )
    )
)