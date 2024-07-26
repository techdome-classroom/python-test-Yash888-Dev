def decode_message( s: str, p: str) -> bool:

# write your code here
    def decode_message(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    
    # Create a 2D DP table with dimensions (m+1) x (n+1)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # An empty pattern matches an empty message
    dp[0][0] = True
    
    # Fill in the first row for patterns that only consist of '*'
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the rest of the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # '*' matches an empty sequence or any sequence of characters
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                # '?' matches any single character or exact character match
                dp[i][j] = dp[i - 1][j - 1]
    
    # The result is whether the entire message matches the entire pattern
    return dp[m][n]
   return False