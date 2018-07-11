def feature_to_text(feature_name, feature_qualifier):
    return feature_name + " " + feature_qualifier["operator"] + " " + str(feature_qualifier["value"])


def table_to_text(columns, rows):
    rows = list(map(lambda i: list(map(str, i)), rows))
    print(columns, rows)
    if len(rows) == 0:
        by_column = [[] for _ in columns]
    else
        by_column = zip(*rows)
    maxlens = [max(len(a), *list(map(len, b))) for (a, b) in zip(columns, by_column)]
    string = "|".join([b.ljust(a) for (a, b) in zip(maxlens, columns)])
    string += "\n"
    string += "=" * len(string)
    string += "\n"
    for row in rows:
        string += "|".join([b.ljust(a) for (a, b) in zip(maxlens, row)])
        string += "\n"
    return string


def format_tabular(term, data):
    tables = []
    format_tables(data, tables)
    string = term
    string += "\n"
    for table in tables:
        string += table_to_text(table[0], table[1])
        string += "\n"
    return string


def format_tables(data, tables):
    if "features" in data:
        columns = ["cohort_id", "size", "features"]
        features = ",".join([feature_to_text(a, b) for (a, b) in data["features"].items()])
        rows = [[data["cohort_id"], data["size"], features]]
        tables.append([columns, rows])
    elif "cohort_id" in data:
        columns = ["cohort_id", "size"]
        rows = [[data["cohort_id"], data["size"]]]
        tables.append([columns, rows])
    elif "feature_a" in data:
        feature_a = data["feature_a"]
        feature_b = data["feature_b"]
        feature_a_feature_name = feature_a["feature_name"]
        feature_a_feature_qualifiers = feature_a["feature_qualifiers"]
        feature_b_feature_name = feature_b["feature_name"]
        feature_b_feature_qualifiers = feature_b["feature_qualifiers"]

        columns = ["feature"] + list(map(lambda x: feature_to_text(feature_a_feature_name, x), feature_a_feature_qualifiers))
        rows = [[a] + b for (a, b) in zip(list(map(lambda x: feature_to_text(feature_b_feature_name, x), feature_b_feature_qualifiers)), data["feature_matrix"])]
        tables.append([columns, rows])

        columns = ["p_value", "chi_squared"]
        rows = [[data["p_value"], data["chi_squared"]]]
        tables.append([columns, rows])
    elif "feature" in data:
        feature = data["feature"]
        feature_feature_name = feature["feature_name"]
        feature_feature_qualifiers = feature["feature_qualifiers"]

        columns = ["feature", "count"]
        rows = [[a, b] for (a, b) in
                zip(list(map(lambda x: feature_to_text(feature_feature_name, x), feature_feature_qualifiers)), data["feature_matrix"])]
        tables.append([columns, rows])

        columns = ["p_value", "chi_squared"]
        rows = [[data["p_value"], data["chi_squared"]]]
        tables.append([columns, rows])
    elif isinstance(data, list):
        for d in data:
            format_tables(d, tables)
    elif isinstance(data, dict):
        columns = ["features"]
        rows = [[feature_to_text(a, b)] for (a, b) in data.items()]
        tables.append([columns, rows])

    else:
        columns = ["error"]
        rows = [[str(data)]]
        tables.append([columns, rows])





