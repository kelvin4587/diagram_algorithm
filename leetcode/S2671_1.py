from collections import Counter


class FrequencyTracker:

    def __init__(self):
        self.freq = Counter()
        self.freq_cnt = Counter()

    def add(self, number: int) -> None:
        self.freq_cnt[self.freq[number]] -= 1
        self.freq[number] += 1
        self.freq_cnt[self.freq[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.freq[number] == 0:
            return
        self.freq_cnt[self.freq[number]] -= 1
        self.freq[number] -= 1
        self.freq_cnt[self.freq[number]] += 1
        return

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_cnt[frequency] > 0


if __name__ == '__main__':
    s = FrequencyTracker()
    s.add(3)
    s.add(3)
    print(s.hasFrequency(3))
