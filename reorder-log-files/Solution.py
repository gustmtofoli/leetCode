class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(log):
            id_, rest = log.split(" ", 1)
            if rest[0].isalpha():
                return (0, rest, id_)
            return (1,)
        return sorted(logs, key = f)