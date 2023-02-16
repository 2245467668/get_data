import get_scene_data


def main():
    url = "https://travel.qunar.com/p-cs299781-zhangzhou-jingdian-1-"
    file_name = "../data/zhangzhou_data.csv"
    pageSize = 75
    get_scene_data.get_data(url, file_name, pageSize)


if __name__ == '__main__':
    main()
