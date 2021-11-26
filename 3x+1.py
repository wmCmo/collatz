import matplotlib.pyplot as plt

iter = int(input('How much number do you want for each loop?:'))

runner = 0
main_list = {}

while True:
    runner += 1
    main_list[runner] = []
    main_list[runner].append(runner)
    n = runner

    while n != 1:
        remain = n % 2

        if remain == 1:
            n = 3 * n + 1
        else:
            n = n / 2

        main_list[runner].append(n)

    plt.plot(main_list[runner])

    if runner % iter == 0:
        permission = input('Current digit is ' + str(runner) + ' Stop? y/n:')
        if permission == 'n':
            pass
        else:
            plt.show()
            break

        #this is the new comment