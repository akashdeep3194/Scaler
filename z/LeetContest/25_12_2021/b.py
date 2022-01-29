from typing import List

class Solution:
    def canBeMade(self, re, ingredients, supplies):        
        for ele in ingredients:
            if ele not in supplies:
                if ele in re:
                    if self.canBeMade(ele,ingredients[ele],supplies)
                    
        else:
            return True

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ans = []
        for i, re in enumerate(recipes):
            if self.canBeMade(re, ingredients[i], supplies):
                ans.append(re)
                supplies.append(re)
        return ans
