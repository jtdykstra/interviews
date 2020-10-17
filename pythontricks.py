
# custom sorting based on various values
# string splitting in a specific way
class Solution:
    def cmpLogs(self, log):
        id, rest = log.split(" ", maxsplit=1)
        return (0, rest, id) if rest[0].isalpha() else (1, )
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=self.cmpLogs)