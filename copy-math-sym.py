#!/usr/bin/env python
import unicodedata
import subprocess
import sys

COLS = 4


def get_unicode_range(ranges: range | list[range], remove=[]):
    data = {}
    if isinstance(ranges, range):
        ranges = [ranges]

    for range_ in ranges:
        for i in range_:
            char = chr(i)
            try:
                name = unicodedata.name(char).title()
                for rm in remove:
                    name = name.replace(rm, "")
            except:
                continue
            data[f"{char} {name}"] = f"{char}"
    return data


def categories():
    return {
        "letters": lambda: get_unicode_range(range(0x2100, 0x214F)),
        "numbers": lambda: get_unicode_range(range(0x2150, 0x218F)),
        "operators": lambda: get_unicode_range(range(0x2200, 0x22FF)),
        "arrows": lambda: get_unicode_range(
            range(0x2190, 0x21FF), remove=["wards", "Arrow ", "Arrow"]
        ),
        "misc": lambda: get_unicode_range(
            [range(0x27C0, 0x27EF), range(0x2980, 0x29FF), range(0x2B00, 0x2BFF)]
        ),
        "misc-a": lambda: get_unicode_range(range(0x27C0, 0x27EF)),
        "misc-b": lambda: get_unicode_range(range(0x2980, 0x29FF)),
        "misc-op": lambda: get_unicode_range(range(0x2B00, 0x2BFF)),
        "sup": lambda: get_unicode_range(
            [range(0x27F0, 0x27FF), range(0x2900, 0x297F)], remove="wards"
        ),
        "alnum": lambda: get_unicode_range(
            range(0x1D400, 0x1D7FF), remove=["Mathematical "]
        ),
    }


def run_wofi(input_str):
    proc = subprocess.Popen(
        [
            "wofi",
            f"--columns={COLS}",
            "--matching=fuzzy",
            "-dip",  # dmenu/icase/prompt
            "Math Symbols",
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
    )
    stdout, _ = proc.communicate(input=input_str)
    return stdout.strip()


def main():
    cats = categories()
    cat_name = "operators"
    if len(sys.argv) != 1:
        assert len(sys.argv) == 2
        assert (
            sys.argv[1] in cats.keys()
        ), f"Allowed symbol category: {list(cats.keys())}"
        cat_name = sys.argv[1]

    symbols = cats[cat_name]()
    selected_desc = run_wofi("\n".join(symbols.keys()))
    if selected_char := symbols.get(selected_desc):
        subprocess.run(["wl-copy", selected_char])


if __name__ == "__main__":
    open("/tmp/uo", "w").close()
    main()
