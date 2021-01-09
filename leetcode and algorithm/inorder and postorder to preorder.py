in_order=[]
post_order=[]
def find_pre_order():
    if len(in_order)<=1:
        return in_order
    center=post_order[-1]
    index=in_order.index(center)
    left_in=in_order[:index]
    right_in=in_order[index+1:]
    index=len(left_in)
    left_post=post_order[:index]
    right_post=post_order[index:-1]
    return [center]+find_pre_order(left_in,left_post)+find_pre_order(right_in,right_post)