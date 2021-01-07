import csv
from features import features
import sys
import argparse
import random


def randint(high, size=1):
    """Generate size random integers x: 0 <= x < high."""
    return [random.randint(0, high - 1) for _ in range(size)]


def choice(elements, size=1):
    """Draw (with replacement) size elements from elements."""
    return random.choices(elements, k=size)


def generate_data(table_name, years, n, fn):
    data_all = []
    for year in years:
        df = {table_name[0].upper() + table_name[1:] + "Id": list(range(1, n+1))}

        df["year"] = [year for _ in range(n)]

        for f in features.features[table_name]:
            t = f._type
            col = f.name
            levels = f.options
            if levels is None:
                if t == int:
                    df[col] = randint(10, size=n)
                elif t == str:
                    df[col] = [''.join(chr(x + 97) for x in randint(26, size=2)) for _ in range(n)]
                else:
                    print ("error: " + col + " " + str(t))
            else:
                df[col] = choice(levels, size=n)
        # reformat dict
        data = [
            dict(row)
            for row in zip(*[
                list(zip(
                    [key for _ in value],
                    value,
                ))
                for key, value in df.items()
            ])
        ]

        data_all.extend(data)

    fieldnames = list(data_all[0].keys())
    with open(fn, "w") as stream:
        writer = csv.DictWriter(stream, fieldnames)
        writer.writeheader()
        writer.writerows(data_all)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('table', type=str)
    parser.add_argument('years', type=int, nargs="+")
    parser.add_argument('size', type=int)
    parser.add_argument('filename', type=str)

    args = parser.parse_args()
    t = args.table
    years = args.years
    n = args.size
    fn = args.filename

    generate_data(t, years, n, fn)
