def solution(new_id):
    answer = ''
    
    # 1
    new_id = new_id.lower()
    
    
    # 2
    ch = ['-', '_', '.']
    tmp = ''
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ch:
            tmp += c
    new_id, tmp = tmp, ''
    
    
    # 3
    dots = ['.' * i for i in range(2, len(new_id) + 1)]
    for dot in dots[::-1]:
        new_id = new_id.replace(dot, '.')            
            
    
    # 4
    if new_id[0] == '.' and len(new_id) > 1 : new_id = new_id[1:]
    if new_id[len(new_id) - 1] == '.': new_id = new_id[:len(new_id) - 1]
    
    # 5
    if not new_id: new_id = 'a'
    
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.': new_id = new_id[:len(new_id) - 1]
    
    #7
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
    
    answer = new_id        
        
    return answer