import download

if __name__ == "__main__":
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("--queries_file_name", type=str, nargs=1,
                        help='')
    args = parser.parse_args()
    with open(args.queries_file_name[0]) as f:
        lis=[line.split(", ") for line in f]        # create a list of lists
        for j, x in enumerate(lis):
            s = 0
            for i in x :
                if s != 0:
                    i = i.replace('\n','')
                    # print(i)
                    # print(len(i))
                    download.download(i,10,x[0])
                else:
                    s =s + 1


