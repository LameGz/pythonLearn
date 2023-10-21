novels = ["gone_girl", "davinci_code", "games_of_thrones", "gone_girl",
          "davinci_code"]


def main():
    count_items = dict()
    for novel in novels:
        count_items[novel] = count_items.get(novel, 0) + 1
        # 如果字典 count_items 中已经有了键 novel，则将其对应的值加1，如果没有，则将键 novel 添加到字典中，并将其对应的值设置为1。
    print("Number of times a novel appears in the list is")
    print(count_items)

if __name__ == "__main__":
    main()
