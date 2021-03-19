import solvers as slv

Tc = 37
Ts = 229
Tw = 591

Tc2 = 594
Ts2 = 11
N2 = 49


def main():
    channels_number = slv.task1_1_solve(Tc=Tc, Ts=Ts)
    # slv.task1_2_solve(Tc=Tc, Ts=Ts, channels_num=channels_number, q_len_max=10)
    # slv.task1_3_solve(Tc=Tc, Ts=Ts, channels_num=channels_number)
    # slv.task1_4_solve(Tc=Tc, Ts=Ts, Tw=Tw, channels_num=channels_number)
    slv.task2_solve(Tc=Tc2, Ts=Ts2, channels_num=N2)


if __name__ == '__main__':
    main()
