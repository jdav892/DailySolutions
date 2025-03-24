class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        cooks = {s:True for s in supplies}
        indexes = {r:i for i, r in enumerate(recipes)}

        def dfs(r):
            if r in cooks:
                return cooks[r]
            if r not in indexes:
                return False

            cooks[r] = False

            for n in ingredients[indexes[r]]:
                if not dfs(n):
                    return False
            
            cooks[r] = True
            return cooks[r]
        return [r for r in recipes if dfs(r)]