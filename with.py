class WordsFinder:
    file_name = []
    def __init__(self, *args):
        self.args = args
        for i in args:
            self.file_name.append(i)

    def get_all_words(self):
        all_words = {}
        bad_value = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in WordsFinder.file_name:
            with open(i, 'r+', encoding= 'utf -8') as file:
                temp = file.read().lower().split()
                for q in range(len(temp)):
                    for v in temp[q]:
                        if v in bad_value:
                            temp[q] = temp[q].replace(v, '')
                all_words[i] = temp
        return all_words

    def find(self,word):
        result = self.get_all_words()
        answer = {}
        for i in result:
            for q in result[i]:
                if q == word.lower():
                    answer[i] = result[i].index(q) + 1
        return answer

    def count(self, word):
        result = self.get_all_words()
        answer = {}
        for i in result:
            count = 0
            for q in result[i]:
                if q == word.lower():
                    count += 1
            answer[i] = count
        return answer

if __name__ == '__main__':

    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())

    print(finder2.find('TEXT'))

    print(finder2.count('teXT'))