class Solution:
    # O(N) / space O(N)
    # slide window
    # hashmap
    def totalFruit(self, tree: List[int]):
        if len(tree) <1:
            return -1
        max_fruit = 0
        type_count = [0]*len(tree) 
        fruit_index = set()
        l = 0
        r = 0 
        while r < len(tree):
            self.add_fruit(tree[r], type_count, fruit_index)
            while len(fruit_index) > 2:
                self.remove_fruit(tree[l], type_count, fruit_index)
                l += 1
            fruit_num = self.calculate_number_fruit(type_count, fruit_index)
            max_fruit = max(max_fruit, fruit_num)
            r+=1
        return max_fruit
        
    def add_fruit(self, fruit, type_count,fruit_index):
        if type_count[fruit] == 0 :
            fruit_index.add(fruit)
        type_count[fruit] += 1
        
    def remove_fruit(self, fruit, type_count,fruit_index):
        type_count[fruit] -= 1
        if type_count[fruit] == 0 :
            fruit_index.remove(fruit)
        
    def calculate_number_fruit(self, type_count, fruit_index):
        sum_fruit = 0
        for i in fruit_index:
            sum_fruit += type_count[i]
        return sum_fruit
        