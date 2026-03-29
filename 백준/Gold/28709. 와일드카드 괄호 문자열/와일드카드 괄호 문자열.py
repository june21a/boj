import sys
input = sys.stdin.readline


def find_all_indices(s, char):
    return [i for i, c in enumerate(s) if c == char]

def solve(s):
    l = len(s)
    
    if s.startswith(')') or s.endswith('('):
        return False
    
    wildcard_indices = find_all_indices(s, '*')
    cnt_dict = {
        '(': 0,
        ')': 0,
        '?': 0
    }
    
    if wildcard_indices:
        for i in range(wildcard_indices[0]):
            if s[i] in ['(', '?']:
                cnt_dict['('] += 1
            else:
                if cnt_dict['('] == 0:
                    return False
                else:
                    cnt_dict['('] -= 1
                    
        cnt_dict['('] = cnt_dict[')'] = cnt_dict['?'] = 0
        for i in range(wildcard_indices[-1]+1, len(s)):
            if s[i] == '(':
                cnt_dict['('] += 1
            else:
                if cnt_dict['('] == 0:
                    cnt_dict[')'] += 1
                else:
                    cnt_dict['('] -= 1
            
        if cnt_dict['('] != 0:
            return False
        else:
            return True
        
    else:
        if l % 2:
            return False
        
        for c in s:
            if c != '?':
                cnt_dict[c] += 1
        
        if cnt_dict['('] > l//2 or cnt_dict[')'] > l//2:
            return False
        
        cnt = 0
        for c in s:
            if c == '?':
                if cnt_dict['('] < l//2:
                    c = '('
                    cnt_dict['('] += 1
                else:
                    c = ')'
            
            if c == '(':
                cnt += 1
            elif c == ')' and cnt > 0:
                cnt -= 1
        
        if cnt != 0:
            return False
        return True
        
        
        

N = int(input())
for i in range(N):
    s = input().strip()
    if solve(s):
        print("YES")
    else:
        print("NO")