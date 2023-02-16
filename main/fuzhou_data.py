
import get_scene_data

def main():
  url="https://travel.qunar.com/p-cs299826-fuzhou-jingdian-1-"
  file_name= "../data/fuzhou_data.csv"
  pageSize = 10
  get_scene_data.get_data(url,file_name,pageSize)

if __name__ == '__main__':
    main()
