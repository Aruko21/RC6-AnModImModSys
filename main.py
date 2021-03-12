import solvers as slv

Tc = 37
Ts = 229
Tw = 591


def main():
    channels_number = slv.task1_solve(Tc=Tc, Ts=Ts)
    slv.task2_solve(Tc=Tc, Ts=Ts, channels_num=channels_number, q_len_max=10)
    # slv.task3_solve(Tc=Tc, Ts=Ts)
    # slv.task4_solve(Tc=Tc, Ts=Ts, Tw=Tw)


if __name__ == '__main__':
    main()
