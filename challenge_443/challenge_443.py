from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        group_s = ""

        if len(chars) == 1:
            return len(chars)
        elif not chars:
            return 0

        for idx in range(len(chars)):
            if not group_s:
                group_s = group_s + chars[idx]
            elif chars[idx] not in group_s:
                if len(group_s) == 1:
                    s = s + group_s[0]
                else:
                    s = s + group_s[0] + str(len(group_s))
                group_s = ""
                group_s = group_s + chars[idx]
                if idx == len(chars) - 1:
                    s = s + group_s
            elif idx == len(chars) - 1:
                s = s + group_s[0] + str(len(group_s) + 1)
            else:
                group_s = group_s + chars[idx]


        # need to slice in order to update the original input chars list
        # cannot use list comprehension here because it will create a new local list
        chars[:] = list(s)

        return len(chars)
