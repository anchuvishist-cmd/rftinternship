#Student Score Analyzer

marks = [78, 85, 90, 67, 85, 92, 78]

def analyze_scores(marks):
    total = 0
    highest = marks[0]
    lowest = marks[0]
    
    # Single pass loop
    for score in marks:
        total += score
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
    
    average = total / len(marks)
    
    # Count above average
    above_avg_count = sum(1 for score in marks if score > average)
    
    # Grade distribution
    grades = {"A":0, "B":0, "C":0, "FAIL":0}
    for score in marks:
        if score >= 85:
            grades["A"] += 1
        elif score >= 70:
            grades["B"] += 1
        elif score >= 50:
            grades["C"] += 1
        else:
            grades["FAIL"] += 1
    
    return average, highest, lowest, above_avg_count, grades


avg, high, low, above_avg, grade_dist = analyze_scores(marks)

print("Average Score:", avg)
print("Highest Score:", high)
print("Lowest Score:", low)
print("Students Above Average:", above_avg)
print("Grade Distribution:", grade_dist)