# %%
from lib.scraper import scraper_keiba_net
import requests
from tqdm import tqdm
import time
from bs4 import BeautifulSoup
import pandas as pd
import sys
from typing import List

URL = "https://race.netkeiba.com/?pid=schedule"
BASE_URL = "https://race.netkeiba.com"


class Scraper:
    def __init__(self):
        self.data = []

    def get_data(self):
        """dataを取得するメソッド."""
        return self.data

    def save_data(self, file_name: str):
        """指定されたファイル名でdataを保存するメソッド."""
        df = pd.DataFrame(self.data)
        df.to_csv(file_name + ".csv", encoding="utf_8")

    def scraping_2014(self):
        """"２０１４年のレース結果をスクレイピングするメソッド."""
        target_2014 = [
            [[1, 8], [2, 6]],  # 札幌競馬場のレースの情報　[[第何回, 何日]]
            [[1, 6], [2, 6]],  # 函館競馬場のレースの情報　[[第何回, 何日]]
            [[1, 6], [2, 8], [3, 6], [4, 4]],  # 福岡競馬場のレースの情報[　[[第何回, 何日]]
            [[1, 8], [2, 12], [3, 8]],  # 新潟競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 12], [3, 8], [4, 9], [5, 9]],  # 東京競馬場のレースの情報　[[第何回, 何日]]
            [[1, 9], [2, 8], [3, 8], [4, 8]],  # 中山競馬場のレースの情報　[[第何回, 何日]]
            [[1, 4], [2, 6], [3, 8], [4, 6]],  # 中京競馬場のレースの情報　[[第何回, 何日]]
            [[1, 9], [2, 8], [3, 12], [4, 9], [5, 9]],  # 京都競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 8], [3, 8], [4, 8], [5, 8]],  # 阪神競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 12]]  # 小倉競馬場のレースの情報　[[第何回, 何日]]
        ]

        self.scraping(target_2014, 2014)

    def scraping_2011(self):
        """"２０１１年のレース結果をスクレイピングするメソッド."""
        target_2011 = [
            [[1, 8, ], [2, 8]],  # 札幌競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 8]],  # 函館競馬場のレースの情報　[[第何回, 何日]]
            [],  # 福島競馬場のレースの情報[　[[第何回, 何日]]

            # 新潟競馬場のレースの情報　[[第何回, 何日]]
            [[1, 10], [2, 6], [3, 8], [4, 8], [5, 12]],
            [[1, 8], [2, 8], [3, 8], [4, 9], [5, 8]],  # 東京競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 4], [3, 8], [4, 8], [5, 8]],  # 中山競馬場のレースの情報　[[第何回, 何日]]
            [],  # 中京競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 8], [3, 12], [4, 8], [5, 8],
                [6, 8]],  # 京都競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8, [6]], [2, 8], [3, 4], [4, 4], [5, 8],
                [6, 8]],  # 阪神競馬場のレースの情報　[[第何回, 何日]], 1, 8, ６レース目をスキップする
            # 小倉競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 12], [3, 2], [4, 12], [5, 10, [1, 2]]]
        ]
        self.scraping(target_2011, 2011)

    def scraping_2012(self):
        """2012年のレース結果をスクレピングするメソッド."""
        target_2012 = [
            [[1, 8], [2, 6]],  # 札幌競馬場のレースの情報　[[第何回, 何日]]
            [[1, 6], [2, 6]],  # 函館競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 8], [3, 6]],  # 福島競馬場のレースの情報[　[[第何回, 何日]]

            # 新潟競馬場のレースの情報　[[第何回, 何日]]
            [[1, 6], [2, 8], [3, 8], [4, 6]],
            # 東京競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 12], [3, 4], [4, 9], [5, 8]],
            # 中山競馬場のレースの情報　[[第何回, 何日]]
            [[1, 7], [2, 8], [3, 8], [4, 9], [5, 9]],
            [[1, 8], [2, 8], [3, 6]],  # 中京競馬場のレースの情報　[[第何回, 何日]]
            [[1, 7], [2, 8], [3, 12], [4, 9], [5, 8]],  # 京都競馬場のレースの情報　[[第何回, 何日]]
            # 阪神競馬場のレースの情報　[[第何回, 何日]], 1, 8, ６レース目をスキップする
            [[1, 8], [2, 8], [3, 8], [4, 9], [5, 9]],
            # 小倉競馬場のレースの情報　[[第何回, 何日]]
            [[1, 10], [2, 12]]
        ]
        self.scraping(target_2012, 2012)

    def scraping_2013(self):
        """2013年のレース結果をスクレピングするメソッド."""
        target_2013 = [
            [],  # 札幌競馬場のレースの情報　[[第何回, 何日]]
            [[1, 6], [2, 6], [3, 6], [4, 6]],  # 函館競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 8], [3, 6]],  # 福島競馬場のレースの情報[　[[第何回, 何日]]

            # 新潟競馬場のレースの情報　[[第何回, 何日]]
            [[1, 6], [2, 12], [3, 6]],
            # 東京競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 12], [3, 8], [4, 9], [5, 8]],
            # 中山競馬場のレースの情報　[[第何回, 何日]]
            [[1, 7], [2, 8], [3, 8], [4, 9], [5, 9]],
            [[1, 6], [2, 6], [3, 8], [4, 6]],  # 中京競馬場のレースの情報　[[第何回, 何日]]
            [[1, 7], [2, 8], [3, 12], [4, 9], [5, 8]],  # 京都競馬場のレースの情報　[[第何回, 何日]]
            # 阪神競馬場のレースの情報　[[第何回, 何日]], 1, 8, ６レース目をスキップする
            [[1, 8], [2, 8], [3, 8], [4, 9], [5, 9]],
            # 小倉競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 12]]
        ]
        self.scraping(target_2013, 2013)

    def scraping_2015(self):
        """2015年のレース結果をスクレピングするメソッド."""
        target_2015 = [
            [[1, 6], [2, 6]],  # 札幌競馬場のレースの情報　[[第何回, 何日]]
            [[1, 6], [2, 6]],  # 函館競馬場のレースの情報　[[第何回, 何日]]
            [[1, 6], [2, 8], [3, 6]],  # 福島競馬場のレースの情報[　[[第何回, 何日]]

            # 新潟競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 12], [3, 4]],
            # 東京競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 12], [3, 8], [4, 9], [5, 9]],
            # 中山競馬場のレースの情報　[[第何回, 何日]]
            [[1, 9], [2, 8], [3, 8], [4, 9], [5, 8]],
            [[1, 4], [2, 6], [3, 8], [4, 6]],  # 中京競馬場のレースの情報　[[第何回, 何日]]
            [[1, 9], [2, 8], [3, 12], [4, 9], [5, 9]],  # 京都競馬場のレースの情報　[[第何回, 何日]]
            # 阪神競馬場のレースの情報　[[第何回, 何日]], 1, 8, ６レース目をスキップする
            [[1, 8], [2, 8], [3, 8], [4, 9], [5, 8]],
            # 小倉競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 12]]
        ]
        self.scraping(target_2015, 2015)

    def scraping_2016(self):
        """2016年のレース結果をスクレピングするメソッド."""
        target_2016 = [
            [[1, 6], [2, 6]],  # 札幌競馬場のレースの情報　[[第何回, 何日]]
            [[1, 6], [2, 6]],  # 函館競馬場のレースの情報　[[第何回, 何日]]
            [[1, 6], [2, 8], [3, 6]],  # 福島競馬場のレースの情報[　[[第何回, 何日]]

            # 新潟競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 12], [3, 6]],
            # 東京競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 12], [3, 8], [4, 9], [5, 8]],
            # 中山競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 8], [3, 8], [4, 8], [5, 9]],
            [[1, 6], [2, 6], [3, 8], [4, 6]],  # 中京競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 8], [3, 12], [4, 9], [5, 8]],  # 京都競馬場のレースの情報　[[第何回, 何日]]
            # 阪神競馬場のレースの情報　[[第何回, 何日]], 1, 8, ６レース目をスキップする
            [[1, 8], [2, 8], [3, 8], [4, 8], [5, 9]],
            # 小倉競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 12]]
        ]
        self.scraping(target_2016, 2016)

    def scraping_2017(self):
        """2017年のレース結果をスクレピングするメソッド."""
        target_2017 = [
            [[1, 6], [2, 6]],  # 札幌競馬場のレースの情報　[[第何回, 何日]]
            [[1, 6], [2, 6]],  # 函館競馬場のレースの情報　[[第何回, 何日]]
            [[1, 6], [2, 8], [3, 6]],  # 福島競馬場のレースの情報[　[[第何回, 何日]]

            # 新潟競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 12], [3, 6]],
            # 東京競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 12], [3, 8], [4, 9], [5, 8]],
            # 中山競馬場のレースの情報　[[第何回, 何日]]
            [[1, 7], [2, 8], [3, 8], [4, 9], [5, 9]],
            [[1, 6], [2, 6], [3, 8], [4, 6]],  # 中京競馬場のレースの情報　[[第何回, 何日]]
            [[1, 7], [2, 8], [3, 12], [4, 9], [5, 8]],  # 京都競馬場のレースの情報　[[第何回, 何日]]
            # 阪神競馬場のレースの情報　[[第何回, 何日]], 1, 8, ６レース目をスキップする
            [[1, 8], [2, 8], [3, 8], [4, 9], [5, 9]],
            # 小倉競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 12]]
        ]
        self.scraping(target_2017, 2017)

    def scraping_2018(self):
        """2018年のレース結果をスクレピングするメソッド."""
        target_2018 = [
            [[1, 6], [2, 6]],  # 札幌競馬場のレースの情報　[[第何回, 何日]]
            [[1, 6], [2, 6]],  # 函館競馬場のレースの情報　[[第何回, 何日]]
            [[1, 6], [2, 8], [3, 6]],  # 福島競馬場のレースの情報[　[[第何回, 何日]]

            # 新潟競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 12], [3, 6]],
            # 東京競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 12], [3, 8], [4, 9], [5, 8]],
            # 中山競馬場のレースの情報　[[第何回, 何日]]
            [[1, 7], [2, 8], [3, 8], [4, 9], [5, 9]],
            [[1, 6], [2, 6], [3, 8], [4, 6]],  # 中京競馬場のレースの情報　[[第何回, 何日]]
            [[1, 7], [2, 8], [3, 12], [4, 9], [5, 8]],  # 京都競馬場のレースの情報　[[第何回, 何日]]
            # 阪神競馬場のレースの情報　[[第何回, 何日]], 1, 8, ６レース目をスキップする
            [[1, 8], [2, 8], [3, 8], [4, 9], [5, 9]],
            # 小倉競馬場のレースの情報　[[第何回, 何日]]
            [[1, 8], [2, 12]]
        ]
        self.scraping(target_2018, 2018)

    def scraping(self, target: List[List[int]], year: int):
        """特定の年のレース結果をスクレイピングするメソッド."""
        # 10個のの開催場所
        assert len(target) == 10, "length of target is not 10."

        for i, days in tqdm(enumerate(target)):
            spot = i + 1
            self.spot_scraping(year, spot, days)

    def spot_scraping(self, year: int, spot: int, days):
        """spot: 競馬場, 第何回とレース何日めのペアの配列を受け取る."""
        for pair in tqdm(days):
            siries = pair[0]
            races = pair[1]
            if len(pair) == 2:
                self.race_scraping(year, spot, siries, races)
            elif len(pair) == 3:
                assert isinstance(
                    pair[2], list), "type of pair[2] is not List[int]."
                skiplst = pair[2]
                self.race_scraping(year, spot, siries, races, skiplst)

    def race_scraping(self, year: int, spot: int, siries: int, races: int, skiplst=[]):
        """spot: 競馬場, siries: 第何回、race:何日目、 レーススクレイピングする, skip: 何レース目をスキップするか、デフォルトは空リスト."""
        for race in tqdm(range(1, races+1)):
            url = BASE_URL + "/?pid=race&id=c" + \
                str(year) + str(spot).zfill(2) + \
                str(siries).zfill(2) + str(race).zfill(2) + "11&mode=result"
            print(url + "\n")
            if race in skiplst:
                continue
            else:
                time.sleep(1)
                res = scraper_keiba_net(url)
                time.sleep(1)
                self.data.append(res)


if __name__ == "__main__":

    year = sys.argv[1]
    scp = Scraper()
    if year == "2014":
        scp.scraping_2014()
    elif year == "2011":
        scp.scraping_2011()
    elif year == "2012":
        scp.scraping_2012()
    elif year == "2013":
        scp.scraping_2013()
    elif year == "2015":
        scp.scraping_2015()
    elif year == "2016":
        scp.scraping_2016()
    elif year == "2017":
        scp.scraping_2017()
    elif year == "2018":
        scp.scraping_2018()
    scp.save_data("sample_" + year)

# %%
