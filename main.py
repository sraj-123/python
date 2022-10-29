class Solution:
    def solve(self, list_maps: list[dict]):
        hum_dict = dict()
        for data in list_maps:
            for key, value in data.items():
                if hum_dict.get(value):
                    hum_dict[value].append(key)
                    continue
                hum_dict[key] = [value]
        print(hum_dict)


Solution().solve(
    [
        {"Dg set": "Diesel generator"},
        {"Organization": "Organisation"},
        {"Group": "Organization"},
        {"Orange": "Kinnu"},
        {"Orange": "narangi"},
    ]
)