def level_order(root):
    queue=[root]
    while len(queue)!=0:
        ele=queue.pop(0)
        if ele.left!=None:
            queue.append(ele.left)
        if ele.right!=None:
            queue.append(ele.right)
        print(ele.data)