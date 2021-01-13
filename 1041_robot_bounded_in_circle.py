class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        if len(instructions)==0:
            return False
        pos = [0,0,0]
        for i in range(4):
            self.move(pos, instructions)
        if pos[0] == 0 and pos[1]==0:
            return True
        return False
        
    def move(self, pos, instructions):
        # pos: x, y, direction
        for i in instructions:
            if i in ['L', 'R']:
                if i == 'L':
                    pos[2] -= 1
                else:
                    pos[2] += 1
                pos[2] = pos[2]+4 if pos[2] <0 else pos[2]
                pos[2] = pos[2]-4 if pos[2] >3 else pos[2]
            if i == 'G':
                if pos[2] == 0:
                    pos[0] -= 1
                elif pos[2] == 1:
                    pos[1] -= 1
                elif pos[2] == 2:
                    pos[0] += 1
                else:
                    pos[1] += 1