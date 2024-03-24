def linearize(hierarchy):
    result = []
    
    while hierarchy:
        next_cls = None
        for cls in hierarchy:
            if not any(cls[0] in other_cls[1:] for other_cls in hierarchy):
                next_cls = cls
                break
            
        if not next_cls:
            raise ValueError("Error")
            
        result.append(next_cls[0])
        
        hierarchy = [cls for cls in hierarchy if cls[0] != next_cls[0]]
        for cls in hierarchy:
            if next_cls[0] in cls[1:]:
                cls.remove(next_cls[0])

    if result[-1] != 'object':
        result.append('object')

    return result

hierarchy = [
    ["A", "О"],
    ["B", "А"],
    ["C", "B"],
    ["D", "B"],
    ["E", "C", ]
]

mro = linearize(hierarchy)
print("MRO:", mro)




