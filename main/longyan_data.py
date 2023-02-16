
import get_scene_data

def main():
  url="https://travel.qunar.com/p-cs299821-longyan-jingdian-1-"
  file_name= "../data/longyan_data.csv"
  pageSize = 35
  get_scene_data.get_data(url,file_name,pageSize)

if __name__ == '__main__':
    main()
