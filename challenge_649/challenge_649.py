from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # if senate contains 0 or 1 senate(s):
        if not senate:
            return None
        if len(senate) == 1:
            return "Radiant" if senate == "R" else "Dire"

        # initialize two queues to keep track of valid senates still in play
        rad_q = deque()
        dire_q = deque()

        # enumerate over senate input string and append index value to a dire and rad queue respectively
        for i, s in enumerate(senate):
            if s == "D":
                dire_q.append(i)
            if s == "R":
                rad_q.append(i)

        counter = 0
        while rad_q or dire_q:
            # return Radiant or Dire depending on whether rad or dire qeueu is empty
            if not rad_q and dire_q:
                return "Dire"
            if rad_q and not dire_q:
                return "Radiant"
            
            # depending on who wins, pop both loser and winner and append winner to the end of their respective queue
            if rad_q[counter] > dire_q[counter]:
                rad_q.popleft()
                dire_q.append(dire_q[counter] + len(senate))
                dire_q.popleft()
            elif rad_q[counter] < dire_q[counter]:
                dire_q.popleft()
                rad_q.append(rad_q[counter] + len(senate))
                rad_q.popleft()
            else:
                counter = counter + 1
