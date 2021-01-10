from typing import List


def reorderLogFiles(self, logs: List[str]) -> List[str]:
    char_log: str = []
    int_log: str = []

    # 문자, 숫자로그 판별
    for s in logs:
        if s.split()[1].isdigit():
            int_log.append(s)
        else:
            char_log.append(s)

    char_log.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return char_log + int_log
