from collections import deque


eggs = deque([int(i) for i in input().split(", ")])
papers = deque([int(i) for i in input().split(", ")])
boxes = 0

while True:
    if len(papers) == 0 or len(eggs) == 0:
        break
    egg = eggs.popleft()
    if egg <= 0:
        egg = eggs.popleft()
    if egg == 13:
        first = papers.popleft()
        last = papers.pop()
        papers.appendleft(last)
        papers.append(first)
        continue
    paper = papers.pop()
    if egg + paper <= 50:
        boxes += 1
    if len(papers) == 0 or len(eggs) == 0:
        break

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")
if len(eggs) > 0:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if len(papers) > 0:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")
