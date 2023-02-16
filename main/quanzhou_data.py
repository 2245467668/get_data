import get_scene_data


def main():
    url="https://travel.qunar.com/p-cs299779-quanzhou-jingdian-1-"
    file="../data/quanzhou_data.csv"
    pageSize = 100
    get_scene_data.get_data(url, file,pageSize)

if __name__ == '__main__':
    main()