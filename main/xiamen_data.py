import get_scene_data


def main():
    url = "https://travel.qunar.com/p-cs299782-xiamen-jingdian-1-"
    file_name = "../data/xiamen_data.csv"
    pageSize = 120
    get_scene_data.get_data(url, file_name, pageSize)


if __name__ == '__main__':
    main()
