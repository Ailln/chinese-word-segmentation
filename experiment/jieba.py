import jieba
import torbjorn as tbn

from utils import data_utils


@tbn.run_time
def jieba_test():
    train_datas, test_datas = data_utils.get_datas()

    all_num = 0
    true_num = 0
    false_num = 0

    for data in train_datas:
        sample_list = data.split("  ")
        sample = "".join(sample_list)
        seg_list = list(jieba.cut(sample))

        sample_pos_list = []
        sample_len = 0
        for word in sample_list:
            word_len = len(word)
            sample_pos_list.append([sample_len, sample_len+word_len])
            sample_len += word_len

        jieba_pos_list = []
        jieba_len = 0
        for word in seg_list:
            word_len = len(word)
            jieba_pos_list.append([jieba_len, jieba_len+word_len])
            jieba_len += word_len

        true_word_num = 0
        false_word_num = 0
        for pos in sample_pos_list:
            if pos in jieba_pos_list:
                true_word_num += 1
            else:
                false_word_num += 1

        all_num += len(sample_pos_list)
        true_num += true_word_num
        false_num += false_word_num
    print(f"all: {all_num}, true: {true_num}, false: {false_num}, acc: {true_num/all_num}")


if __name__ == '__main__':
    jieba_test()

