#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import requests

GOAL_API = "https://unstats.un.org/sdgapi/v1/sdg/Goal/List"
TARGET_API = "https://unstats.un.org/sdgapi/v1/sdg/Target/List"
SERIES_API = "https://unstats.un.org/sdgapi/v1/sdg/Series/List"
INDICATOR_API = "https://unstats.un.org/sdgapi/v1/sdg/Indicator/List"


def main():
    """UN SDGsのGoal, Target, Series, Indicatorの
    全てのList情報を取得
    """

    ofn = "../data/un_sdgs_list.xlsx"

    data_d = {
        "GOAL": GOAL_API,
        "TARGET": TARGET_API,
        "SERIES": SERIES_API,
        "INDICATOR": INDICATOR_API,
    }

    with pd.ExcelWriter(ofn) as writer:
        for k, api_url in data_d.items():
            r = requests.get(api_url)
            df = pd.json_normalize(r.json())
            df.to_excel(writer, sheet_name=k, index=False)


if __name__ == "__main__":
    main()
