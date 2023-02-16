import get_meishi_data


def main():
    url = "https://travel.qunar.com/p-cs299782-xiamen-meishi?page="
    file_name = "../../data/meishi_data/xiamen_meishi.csv"
    pageSize = 200
    get_meishi_data.get_data(url, file_name, pageSize)


if __name__ == '__main__':
    main()
